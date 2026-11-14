#!/usr/bin/env python3
"""Base de ruiditos y mezcla: copia este archivo a la carpeta del video como ruidos.py y escribe SOLO la sección de eventos.
Viene del primer video que gustó de oído (Opus medium, «200 % mejor» en el A/B de Didier): síntesis por código, con semilla,
ducking contra la voz y un seguro para que los ruidos nunca queden a menos de 15 dB de la voz mientras habla.
Los eventos son de cada mundo: cada material suena a lo suyo. Nada descargado y sin música.

Uso: python3 ruidos.py voz.wav voz-limpia.wav ruidos.wav audio-final.wav
- voz.wav solo sirve para saber cuándo habla. audio-final.wav = voz-limpia + ruidos, con las mismas muestras que la voz.
"""
import math, random, struct, sys, wave

SR = 48000
VOZ_ORIG, VOZ_LIMPIA, OUT_RUIDOS, OUT_FINAL = sys.argv[1:5]


def leer(path):
    with wave.open(path, "rb") as w:
        ch, sw, sr, n = w.getnchannels(), w.getsampwidth(), w.getframerate(), w.getnframes()
        raw = w.readframes(n)
    if sw == 2:
        vals = [v / 32768 for v in struct.unpack("<%dh" % (len(raw) // 2), raw)]
    elif sw == 3:
        vals = [int.from_bytes(raw[i:i + 3], "little", signed=True) / 8388608 for i in range(0, len(raw), 3)]
    else:
        raise SystemExit("formato no soportado")
    return vals[::ch], sr


def escribir(path, x):
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(struct.pack("<%dh" % len(x), *(int(max(-1, min(1, v)) * 32767) for v in x)))


voz, _ = leer(VOZ_LIMPIA)
N = len(voz)
DUR = N / SR
buf = [0.0] * N
rng = random.Random(11)


def db(g):
    return 10 ** (g / 20)


def svf(x, fc, q, modo="band"):
    """Filtro de estado variable; fc puede ser número o función del índice."""
    low = band = 0.0
    out = []
    fija = not callable(fc)
    f = 2 * math.sin(math.pi * min(fc, SR / 7) / SR) if fija else 0
    for i, v in enumerate(x):
        if not fija:
            f = 2 * math.sin(math.pi * min(fc(i), SR / 7) / SR)
        high = v - low - band / q
        band += f * high
        low += f * band
        out.append(band if modo == "band" else low if modo == "low" else high)
    return out


def ruido(n, r=rng):
    return [r.uniform(-1, 1) for _ in range(n)]


def poner(t, x, g_db):
    i0, g = int(t * SR), db(g_db)
    for k, v in enumerate(x):
        if 0 <= i0 + k < N:
            buf[i0 + k] += v * g


def env_ad(n, ataque, caida):
    a = max(1, int(ataque * SR))
    return [(k / a) if k < a else math.exp(-(k - a) / (caida * SR)) for k in range(n)]


def norm(x):
    p = max(1e-9, max(abs(v) for v in x))
    return [v / p for v in x]


# ---------- piezas ----------
def golpe_resonante(freqs, decs, dur, ruido_ms=4, fc_ruido=2500):
    n = int(dur * SR)
    out = [0.0] * n
    for f, d in zip(freqs, decs):
        fase = rng.random() * 6.28
        for k in range(n):
            out[k] += math.sin(2 * math.pi * f * k / SR + fase) * math.exp(-k / (d * SR)) / len(freqs)
    nr = int(ruido_ms / 1000 * SR)
    clic = svf(ruido(nr), fc_ruido, 1.2)
    for k in range(nr):
        out[k] += clic[k] * (1 - k / nr) * 0.8
    return norm(out)


def madera(f=520):  # toc de madera
    return golpe_resonante([f, f * 2.3, f * 3.9], [0.035, 0.018, 0.01], 0.18)


def whoosh(dur, f0, f1, pico=0.45):
    n = int(dur * SR)
    fc = lambda i: f0 * (f1 / f0) ** (i / n)
    x = svf(ruido(n), fc, 1.4)
    out = []
    for k, v in enumerate(x):
        u = k / n
        e = (u / pico) if u < pico else (1 - u) / (1 - pico)
        out.append(v * math.sin(e * math.pi / 2) ** 2)
    return norm(out)


def papel_pop(firme=1.0):  # cartulina que se abre: crujido + golpecito
    n = int(0.22 * SR)
    cruj = svf(ruido(n), 3200, 0.9)
    out = []
    for k in range(n):
        t = k / SR
        e = math.exp(-t / 0.05) * (1 + 0.6 * math.sin(t * 2 * math.pi * 55))
        out.append(cruj[k] * e * 0.7)
    th = golpe_resonante([180, 410], [0.03, 0.015], 0.12, 2, 1500)
    for k in range(len(th)):
        out[k] += th[k] * 0.5 * firme
    return norm(out)


def karplus(f, dur, brillo=0.5):  # cuerda pulsada tensa
    n, L = int(dur * SR), int(SR / f)
    linea = svf(ruido(L), 4000 * brillo + 800, 0.7, "low")
    out = []
    for k in range(n):
        v = linea[k % L]
        linea[k % L] = 0.996 * 0.5 * (v + linea[(k + 1) % L])
        out.append(v)
    e = env_ad(n, 0.002, dur / 3)
    return norm([a * b for a, b in zip(out, e)])


def siseo(dur, fc, q, mod_hz, mod_prof, ataque=0.05, salida=0.2):
    n = int(dur * SR)
    x = svf(ruido(n), fc, q)
    out = []
    for k, v in enumerate(x):
        t = k / SR
        e = min(1, t / ataque, (dur - t) / salida)
        m = 1 - mod_prof * (0.5 + 0.5 * math.sin(2 * math.pi * mod_hz * t + math.sin(t * 3.1)))
        out.append(v * max(0, e) * m)
    return norm(out)


# ---------- EVENTOS DE ESTE VIDEO: solo esto se escribe ----------
# Fondo continuo del mundo, bajito (mételo en buf con un bucle o con poner(0, x, -44)).
# Un ruido por cada cosa que aparece, en el segundo exacto de timing/TIMING.md:
#   poner(5.46, papel_pop(), -30)
# Golpes y clics: golpe_resonante y madera. Aire y cámara: whoosh (muy bajo, del largo del viaje). Tensión: karplus. Roce: siseo.
# Un solo sonido dominante: el del momento sagrado.

# ---------- ducking: cuándo habla (de la voz original) ----------
orig, sr0 = leer(VOZ_ORIG)
paso = sr0 // 100  # ventanas de 10 ms
habla = []
for i in range(0, len(orig), paso):
    w = orig[i:i + paso]
    habla.append(math.sqrt(sum(v * v for v in w) / max(1, len(w))) > db(-42))
# relleno: huecos menores a 250 ms cuentan como habla (respiros entre palabras)
k = 0
while k < len(habla):
    if not habla[k]:
        j = k
        while j < len(habla) and not habla[j]:
            j += 1
        if 0 < k and j < len(habla) and j - k < 25:
            for m in range(k, j):
                habla[m] = True
        k = j
    else:
        k += 1
g, gan = 1.0, []
for h in habla:
    obj = db(-8) if h else 1.0
    g += (obj - g) * (0.25 if obj < g else 0.04)  # baja en ~40 ms, sube en ~250 ms
    gan.append(g)
per = SR // 100
for i in range(N):
    buf[i] *= gan[min(len(gan) - 1, i // per)]

# ---------- seguro: los ruidos nunca a menos de 15 dB de la voz mientras habla ----------
W = int(0.4 * SR)
seg = []
for i in range(0, N, W):
    hv = any(habla[i // per:(i + W) // per])
    rv = math.sqrt(sum(v * v for v in voz[i:i + W]) / W)
    rr = math.sqrt(sum(v * v for v in buf[i:i + W]) / W) + 1e-12
    lim = rv * db(-17) / rr if hv else 1.0
    seg.append(min(1.0, lim))
for i in range(N):
    buf[i] *= seg[i // W]

escribir(OUT_RUIDOS, buf)

# ---------- mezcla y medición ----------
mix = [a + b for a, b in zip(voz, buf)]
pico = max(abs(v) for v in mix)
if pico > db(-1.5):
    mix = [v * db(-1.5) / pico for v in mix]
escribir(OUT_FINAL, mix)
peor = 99
for i in range(0, N, W):
    if any(habla[i // per:(i + W) // per]):
        rv = math.sqrt(sum(v * v for v in voz[i:i + W]) / W)
        rr = math.sqrt(sum(v * v for v in buf[i:i + W]) / W) + 1e-12
        peor = min(peor, 20 * math.log10(rv / rr))
print("muestras %d (%.3f s), pico mezcla %.1f dBFS, peor distancia voz-ruidos al hablar %.1f dB"
      % (N, N / SR, 20 * math.log10(max(abs(v) for v in mix)), peor))
