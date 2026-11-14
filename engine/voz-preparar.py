#!/usr/bin/python3
"""La voz, de punta a punta y sin modelo. Dos pasos de la ruta video-fabrica:

  voz-preparar.py texto <carpeta>     De 03-SPEECH.md (bloque VOZ:/FIN-VOZ) deja VOZ-AI-STUDIO.md: voz, tono y texto para pegar.
  voz-preparar.py preparar <carpeta>  De voz-original.wav deja, sin cambiarle nada a lo que dijo:
      timing-original/   words.json, TIMING.md y SRT de Whisper, tal como salieron
      VOZ-REPORTE.md     qué dijo la voz distinto del texto (solo reporta, no corrige)
      voz.wav            la voz con los silencios que el speech declara (mismas muestras; los tiempos se recorren)
      voz-limpia.wav     voz.wav pasada por la receta de voz limpia (la que va a la mezcla)
      voz.srt            subtítulos por frase: las palabras y la ortografía del bloque SPEECH aprobado, con los tiempos de voz.wav
      timing/            words.json y TIMING.md por palabra, con los tiempos de voz.wav

Silencios en 03-SPEECH.md, un bloque entre 'SILENCIOS:' y 'FIN-SILENCIOS':
  después de «frase exacta»: 1.5     agrega 1.5 s justo después de la última palabra de esa frase
  al final: 2                        deja la cola sin voz en 2 s (tope: --tope-final, 3.5 s)
Lo que no se encuentre en la voz se reporta y no se inserta.

Whisper corre con uv y su caché, sin red (no descarga ni instala nada); si la caché no alcanza, lo dice.
Solo biblioteca estándar."""
import argparse
import difflib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
import wave

AQUI = Path(__file__).resolve().parent
BASE = AQUI.parent
FFMPEG = os.environ.get('HUMANIFY_FFMPEG', str(Path(__file__).resolve().parent.parent / 'node_modules/ffmpeg-static/ffmpeg'))
RECETA = AQUI / 'receta-voz-limpia.sh'
VOZ_FICHA = BASE / 'craft/biblioteca/VOZ-NARRADORA.md'
TOPE_FINAL = 3.5
TOPE_LINEA = 30   # caracteres por renglón de subtítulo: a 60 px caben unos 30 en los 952 px útiles, y se leen en 2 renglones


class Falla(Exception):
    pass


def bloque(texto, inicio, fin):
    hallado = re.search(r'^\s*\**{}:?\**\s*$(.*?)^\s*\**{}\**\s*$'.format(inicio, fin), texto, re.M | re.S)
    return hallado.group(1).strip() if hallado else None


def sin_etiquetas(texto):
    return re.sub(r'<[^>]*>', ' ', texto)


def normal(palabra):
    """Para comparar: sin acentos, signos ni mayúsculas."""
    plana = unicodedata.normalize('NFD', palabra.lower())
    return ''.join(c for c in plana if c.isalnum())


def palabras_de(texto):
    return [n for n in (normal(p) for p in sin_etiquetas(texto).replace('-', ' ').split()) if n]


UNIDADES = ('cero uno dos tres cuatro cinco seis siete ocho nueve diez once doce trece catorce quince dieciseis diecisiete '
            'dieciocho diecinueve veinte veintiuno veintidos veintitres veinticuatro veinticinco veintiseis veintisiete '
            'veintiocho veintinueve').split()
DECENAS = {30: 'treinta', 40: 'cuarenta', 50: 'cincuenta', 60: 'sesenta', 70: 'setenta', 80: 'ochenta', 90: 'noventa'}
CIENTOS = {100: 'ciento', 200: 'doscientos', 300: 'trescientos', 400: 'cuatrocientos', 500: 'quinientos',
           600: 'seiscientos', 700: 'setecientos', 800: 'ochocientos', 900: 'novecientos'}


def en_letras(n):
    """Número entero a palabras comparables (sin acentos), hasta 999,999. Solo para cotejar speech contra voz."""
    if n < 30:
        return UNIDADES[n]
    if n < 100:
        decena, unidad = n // 10 * 10, n % 10
        return DECENAS[decena] + (' y ' + UNIDADES[unidad] if unidad else '')
    if n == 100:
        return 'cien'
    if n < 1000:
        resto = n % 100
        return CIENTOS[n // 100 * 100] + (' ' + en_letras(resto) if resto else '')
    miles, resto = n // 1000, n % 1000
    return ('mil' if miles == 1 else en_letras(miles) + ' mil') + (' ' + en_letras(resto) if resto else '')


def numeros_a_letras(texto):
    def cambia(m):
        limpio = m.group(0).replace(',', '')
        return en_letras(int(limpio)) if limpio.isdigit() and int(limpio) < 1000000 else m.group(0)
    return re.sub(r'\d[\d,]*', cambia, texto)


def leer_speech(carpeta):
    archivo = Path(carpeta) / '03-SPEECH.md'
    try:
        return archivo.read_text(encoding='utf-8')
    except OSError as error:
        raise Falla('no pude leer {}: {}'.format(archivo, error))


def descripcion_voz():
    ficha = VOZ_FICHA.read_text(encoding='utf-8')
    voz = re.search(r'\*\*Voz:\*\*\s*(\S+?)\.?\s*$', ficha, re.M)
    tono = re.search(r'```\n(.*?)\n```', ficha, re.S)
    if not voz or not tono:
        raise Falla('{} no trae voz y descripción'.format(VOZ_FICHA))
    return voz.group(1), tono.group(1).strip()


def comando_texto(carpeta):
    crudo = leer_speech(carpeta)
    texto = bloque(crudo, 'VOZ', 'FIN-VOZ')
    speech = bloque(crudo, 'SPEECH', 'FIN')
    if not texto or not speech:
        raise Falla('03-SPEECH.md debe traer los bloques SPEECH:/FIN y VOZ:/FIN-VOZ')
    if re.search(r'\d', sin_etiquetas(texto)):
        raise Falla('el bloque VOZ trae cifras: van en letras. Linea: ' + next(l for l in texto.splitlines() if re.search(r'\d', sin_etiquetas(l))))
    silencios_de(crudo, TOPE_FINAL)  # un silencio mal escrito se dice aquí, antes de grabar, no después
    a, b = palabras_de(numeros_a_letras(speech)), palabras_de(texto)
    if a != b:
        distintas = sum(max(i2 - i1, j2 - j1) for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if op != 'equal')
        print('Aviso: el bloque VOZ difiere del SPEECH en {} palabras; manda el VOZ.'.format(distintas))
    voz, tono = descripcion_voz()
    salida = ('# Para Google AI Studio (aistudio.google.com, generar voz)\n\n**Voz:** {}\n\n**Descripción de la voz (pégala tal cual):**\n'
              '```\n{}\n```\n\n**Texto:**\n```\n{}\n```\n\nBaja el WAV y déjalo aquí en el chat. Con eso sigo yo hasta el MP4.\n').format(voz, tono, ' '.join(texto.split()))
    (Path(carpeta) / 'VOZ-AI-STUDIO.md').write_text(salida, encoding='utf-8')
    print('VOZ-AI-STUDIO.md listo ({} palabras).'.format(len(b)))


def silencios_de(crudo, tope_final):
    """([(frase, segundos)], segundos de cola o None)."""
    texto = bloque(crudo, 'SILENCIOS', 'FIN-SILENCIOS')
    if not texto:
        return [], None
    frases, cola = [], None
    for linea in texto.splitlines():
        linea = linea.strip().lstrip('-* ').strip()
        if not linea or linea.startswith(('#', '//', '<!--')):
            continue
        despues = re.match(r'despu[eé]s de\s*[«"“](.+?)[»"”]\s*:?\s*(\d+(?:[.,]\d+)?)\s*s?\s*$', linea, re.I)
        final = re.match(r'al final\s*:?\s*(\d+(?:[.,]\d+)?)\s*s?\s*$', linea, re.I)
        if despues:
            frases.append((despues.group(1), float(despues.group(2).replace(',', '.'))))
        elif final:
            cola = min(float(final.group(1).replace(',', '.')), tope_final)
        else:
            raise Falla('no entiendo esta línea de SILENCIOS: ' + linea)
    return frases, cola


def transcribir(wav, destino, texto_guia):
    """Whisper local con la caché de uv y de Hugging Face, sin red."""
    destino.mkdir(parents=True, exist_ok=True)
    guia = destino / '_guia.txt'
    guia.write_text(texto_guia, encoding='utf-8')
    uv = shutil.which('uv')
    comando = ([uv] if uv else ['python3', '-m', 'uv']) + [
        'run', '--no-project', '--offline', '--python', '3.12', '--with', 'faster-whisper', '--with', 'numpy', 'python',
        str(AQUI / 'transcribe.py'), str(wav), str(destino), '--texto', str(guia)]
    env = dict(os.environ, HF_HUB_OFFLINE='1', UV_OFFLINE='1', PYTHONWARNINGS='ignore')
    try:
        salida = subprocess.run(comando, env=env, cwd=str(tempfile.gettempdir()), capture_output=True, text=True, timeout=840)
    except (OSError, subprocess.SubprocessError) as error:
        raise Falla('Whisper no corrió: {}'.format(error))
    if salida.returncode:
        raise Falla('Whisper falló (corre sin red: si falta su caché, dile a Didier este comando sin --offline): {}\n{}'.format(
            ' '.join(comando), ' '.join((salida.stderr or salida.stdout).split())[-500:]))
    guia.unlink(missing_ok=True)
    return json.loads((destino / 'words.json').read_text(encoding='utf-8'))


def fichas_de(dicho):
    """[(palabra comparable, índice en dicho)]: «12» cuenta como «doce» y «Ana-Luisa» como dos palabras."""
    return [(t, i) for i, (w, *_) in enumerate(dicho) for t in palabras_de(numeros_a_letras(w))]


def cotejar(dicho, esperado):
    """Lista de diferencias entre lo esperado y lo que dijo la voz. Solo palabras: la puntuación la pone Whisper."""
    a, b = palabras_de(numeros_a_letras(esperado)), [t for t, _ in fichas_de(dicho)]  # «doce» y «12» son lo mismo
    diferencias = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op != 'equal':
            diferencias.append('- texto: «{}» · voz: «{}»'.format(' '.join(a[i1:i2]) or '(nada)', ' '.join(b[j1:j2]) or '(nada)'))
    return diferencias


def ubicar_frase(dicho, frase):
    """Índice de la última palabra dicha de la frase, o None. Tolera números dichos en letras."""
    buscadas = palabras_de(numeros_a_letras(frase))
    fichas = fichas_de(dicho)
    planas = [t for t, _ in fichas]
    if not buscadas:
        return None
    for i in range(len(planas) - len(buscadas), -1, -1):  # si se repite, la última vez: es la que suele cerrar la idea
        if planas[i:i + len(buscadas)] == buscadas:
            return fichas[i + len(buscadas) - 1][1]
    return None


def cortes(dicho, frases):
    """[(segundo del corte, segundos a insertar)], [frases no halladas]. Se corta a la mitad del hueco tras la palabra."""
    lista, perdidas = [], []
    for frase, segundos in frases:
        i = ubicar_frase(dicho, frase)
        if i is None:
            perdidas.append(frase)
            continue
        fin = dicho[i][2]
        siguiente = dicho[i + 1][1] if i + 1 < len(dicho) else fin
        lista.append((fin + max(0.0, siguiente - fin) / 2, segundos))
    return sorted(lista), perdidas


def recorrer(t, lista):
    return t + sum(s for corte, s in lista if corte <= t)


def insertar_silencios(origen, destino, lista, cola, ultima_palabra):
    """Copia las muestras tal cual y mete ceros en cada corte. La cola se recorta o se alarga hasta `cola` segundos."""
    with wave.open(str(origen), 'rb') as w:
        p = w.getparams()
        datos = w.readframes(p.nframes)
    ancho = p.nchannels * p.sampwidth
    tasa = p.framerate
    if cola is not None:
        fin_voz = int(round(ultima_palabra * tasa)) * ancho
        if len(datos) > fin_voz:
            datos = datos[:fin_voz + int(0.05 * tasa) * ancho]  # el aire de la última palabra se queda
    salida, previo = [], 0
    for corte, segundos in lista:
        k = min(int(round(corte * tasa)), p.nframes) * ancho
        k = min(k, len(datos))
        salida += [datos[previo:k], b'\0' * (int(round(segundos * tasa)) * ancho)]
        previo = k
    salida.append(datos[previo:])
    if cola is not None:
        relleno = max(0.0, cola - 0.05)
        salida.append(b'\0' * (int(round(relleno * tasa)) * ancho))
    with wave.open(str(destino), 'wb') as w:
        w.setparams(p)
        w.writeframes(b''.join(salida))
    with wave.open(str(destino), 'rb') as w:
        return w.getnframes() / w.getframerate()


def marca_srt(x):
    ms = int(round(x * 1000))
    return '{:02}:{:02}:{:02},{:03}'.format(ms // 3600000, ms // 60000 % 60, ms // 1000 % 60, ms % 1000)


def limpia_de_whisper(palabras):
    """Sin speech que alinear: quita comillas inventadas y pega al final de la palabra los signos que Whisper dejó sueltos."""
    salida = []
    for w, s, e in palabras:
        w = re.sub(r'[«»"“”]', '', w).strip()
        if not w:
            continue
        if salida and not normal(w):
            salida[-1] = (salida[-1][0] + w, salida[-1][1], e)
        else:
            salida.append((w, s, e))
    return salida


def subtitulos_del_speech(speech, palabras):
    """Las palabras del SPEECH aprobado con los tiempos de lo que dijo la voz: Whisper da el cuándo, el speech la ortografía.
    Regresa (lista, tramos donde la voz dijo otra cosa). Lo que la voz no dijo no sale; lo que agregó sale como lo oyó Whisper."""
    escritas = speech.split()
    a = [(t, i) for i, w in enumerate(escritas) for t in palabras_de(numeros_a_letras(w))]
    b = fichas_de(palabras)
    tiempos, agregadas, distintos = {}, [], 0
    def toma(i_a, i_b):
        s, e = palabras[b[i_b][1]][1:3]
        previo = tiempos.get(a[i_a][1])
        tiempos[a[i_a][1]] = (min(previo[0], s), max(previo[1], e)) if previo else (s, e)
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, [t for t, _ in a], [t for t, _ in b], autojunk=False).get_opcodes():
        if op != 'equal':
            distintos += 1
        if op in ('equal', 'replace') and j2 > j1:
            for k in range(i1, i2):  # en un reemplazo, el tiempo del tramo se reparte parejo
                primero = j1 + (k - i1) * (j2 - j1) // (i2 - i1)
                ultimo = max(primero, j1 + (k - i1 + 1) * (j2 - j1) // (i2 - i1) - 1)
                toma(k, primero)
                toma(k, ultimo)
        elif op == 'insert':
            agregadas += sorted({b[j][1] for j in range(j1, j2)})
    salida = [(escritas[i], s, e) for i, (s, e) in tiempos.items()]
    salida += limpia_de_whisper([palabras[i] for i in agregadas])
    return sorted(salida, key=lambda x: x[1]), distintos


def frases_srt(palabras):
    """Subtítulos por frase: corta en punto, signo o pausa larga; una coma corta si ya hay texto de sobra."""
    grupos, actual = [], []
    for i, (w, s, e) in enumerate(palabras):
        actual.append((w, s, e))
        largo = len(' '.join(x[0] for x in actual))
        hueco = palabras[i + 1][1] - e if i + 1 < len(palabras) else 9
        if re.search(r'[.?!…][»"”)]*$', w) or hueco > 0.6 or largo >= TOPE_LINEA * 2 - 4 or (re.search(r'[,;:]$', w) and largo >= TOPE_LINEA - 12):
            grupos.append(actual)
            actual = []
    if actual:
        grupos.append(actual)
    return grupos


def escribir_srt(palabras, archivo):
    bloques = []
    for n, grupo in enumerate(frases_srt(palabras), 1):
        bloques.append('{}\n{} --> {}\n{}\n'.format(n, marca_srt(grupo[0][1]), marca_srt(max(grupo[-1][2], grupo[0][1] + 0.01)),
                                                     ' '.join(x[0] for x in grupo)))
    archivo.write_text('\n'.join(bloques), encoding='utf-8')
    return len(bloques)


def escribir_timing(palabras, carpeta, duracion):
    carpeta.mkdir(parents=True, exist_ok=True)
    (carpeta / 'words.json').write_text(json.dumps([[w, round(s, 3), round(e, 3)] for w, s, e in palabras], ensure_ascii=False), encoding='utf-8')
    lineas, actual = ['Duración total: {:.2f} s · palabras: {} (tiempos de voz.wav, ya con silencios)'.format(duracion, len(palabras)), ''], []
    for w, s, e in palabras:
        actual.append('{} {:.2f}–{:.2f}'.format(w, s, e))
        if re.search(r'[.?!…]$', w):
            lineas += [' · '.join(actual), '']
            actual = []
    if actual:
        lineas += [' · '.join(actual), '']
    (carpeta / 'TIMING.md').write_text('\n'.join(lineas), encoding='utf-8')


def a_wav_pcm(origen, trabajo):
    """Si no es WAV PCM (AI Studio a veces da otra cosa), lo convierte sin tocar el original."""
    try:
        with wave.open(str(origen), 'rb') as w:
            w.getparams()
        return origen
    except (wave.Error, EOFError):
        destino = Path(trabajo) / 'voz-original-pcm.wav'
        salida = subprocess.run([FFMPEG, '-y', '-v', 'error', '-i', str(origen), '-c:a', 'pcm_s16le', str(destino)], capture_output=True, text=True)
        if salida.returncode:
            raise Falla('{} no se pudo leer como audio: {}'.format(origen, salida.stderr[-300:]))
        return destino


def comando_preparar(carpeta, tope_final, palabras_dadas=None):
    carpeta = Path(carpeta).resolve()  # Whisper corre en otra carpeta: una ruta relativa ya no se encontraría
    original = carpeta / 'voz-original.wav'
    if not original.exists():
        raise Falla('falta ' + str(original))
    crudo = leer_speech(carpeta)
    esperado = bloque(crudo, 'VOZ', 'FIN-VOZ') or numeros_a_letras(bloque(crudo, 'SPEECH', 'FIN') or '')
    frases, cola = silencios_de(crudo, tope_final)
    with tempfile.TemporaryDirectory(prefix='voz-') as temporal:
        fuente = a_wav_pcm(original, temporal)
        if palabras_dadas is not None:
            dicho = json.loads(Path(palabras_dadas).read_text(encoding='utf-8'))
        else:
            dicho = transcribir(fuente, carpeta / 'timing-original', ' '.join(sin_etiquetas(esperado).split()))
        if not dicho:
            raise Falla('Whisper no sacó palabras de ' + str(original))
        lista, perdidas = cortes(dicho, frases)
        duracion = insertar_silencios(fuente, carpeta / 'voz.wav', lista, cola, dicho[-1][2])
    nuevas = [(w, recorrer(s, lista), recorrer(e, lista)) for w, s, e in dicho]
    # El efecto debe ser exacto: cada palabra se movió lo mismo que se insertó antes de ella.
    limpia = subprocess.run(['/bin/bash', str(RECETA), str(carpeta / 'voz.wav'), str(carpeta / 'voz-limpia.wav')], capture_output=True, text=True)
    if limpia.returncode:
        raise Falla('la receta de voz limpia falló: ' + limpia.stderr[-400:])
    speech = bloque(crudo, 'SPEECH', 'FIN')
    if speech:
        para_srt, tramos = subtitulos_del_speech(speech, nuevas)
        origen_srt = 'del speech aprobado' + (' ({} tramos donde la voz dijo otra cosa llevan el texto del speech)'.format(tramos) if tramos else '')
    else:
        para_srt, origen_srt = limpia_de_whisper(nuevas), 'de Whisper: no hay bloque SPEECH'
    subtitulos = escribir_srt(para_srt, carpeta / 'voz.srt')
    escribir_timing(nuevas, carpeta / 'timing', duracion)
    diferencias = cotejar(dicho, esperado)
    cola_real = duracion - nuevas[-1][2]
    habladas = sum(e - s for _, s, e in nuevas)
    reporte = ['# Reporte de la voz', '',
               'DIFERENCIAS: {}'.format(len(diferencias)),
               'Duración de voz.wav: {:.2f} s · palabras: {} · por segundo (con silencios): {:.2f} · hablando: {:.2f}'.format(
                   duracion, len(nuevas), len(nuevas) / duracion, len(nuevas) / habladas if habladas else 0),
               'Silencios insertados: {} · cola sin voz: {:.2f} s (tope {} s) · subtítulos: {}, con el texto {}'.format(
                   len(lista), cola_real, tope_final, subtitulos, origen_srt), '']
    if perdidas:
        reporte += ['## Silencios que no se pudieron poner (la frase no está en la voz)'] + ['- «{}»'.format(f) for f in perdidas] + ['']
    if diferencias:
        reporte += ['## Lo que la voz dijo distinto (no se corrigió)'] + diferencias + ['']
    if cola_real > tope_final + 0.05:
        reporte.append('AVISO: la cola sin voz pasa del tope. Declara `al final` en SILENCIOS.')
    (carpeta / 'VOZ-REPORTE.md').write_text('\n'.join(reporte) + '\n', encoding='utf-8')
    print('voz.wav {:.2f} s, {} palabras, {} silencios, {} diferencias con el texto.'.format(duracion, len(nuevas), len(lista), len(diferencias)))


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('paso', choices=('texto', 'preparar'))
    p.add_argument('carpeta')
    p.add_argument('--tope-final', type=float, default=TOPE_FINAL)
    p.add_argument('--palabras', help='words.json ya transcrito (para pruebas): no corre Whisper')
    args = p.parse_args(argv)
    try:
        if args.paso == 'texto':
            comando_texto(args.carpeta)
        else:
            comando_preparar(args.carpeta, args.tope_final, args.palabras)
    except Falla as error:
        print('voz-preparar: {}'.format(error), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
