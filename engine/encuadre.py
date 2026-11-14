#!/usr/bin/python3
"""Lo que de verdad ve una pose de cámara en 1080x1920, sin abrir el HTML. Para el aterrizaje: las cuentas de Argon no valen hasta medirlas.
  encuadre.py --fov 44 --distancia 8 --ancho 6.7 [--alto 3] [--margen 64]
fov es el vertical de Three.js; distancia, de la cámara al plano del objeto; ancho y alto, lo que debe caber, en unidades del mundo;
margen, los pixeles laterales de zona segura de MARCA.json. Solo biblioteca estándar."""
import argparse
import math

ANCHO_PX, ALTO_PX = 1080, 1920


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--fov', type=float, required=True)
    p.add_argument('--distancia', type=float, required=True)
    p.add_argument('--ancho', type=float)
    p.add_argument('--alto', type=float)
    p.add_argument('--margen', type=float, default=64)
    args = p.parse_args(argv)
    tangente = 2 * math.tan(math.radians(args.fov) / 2)
    alto = args.distancia * tangente
    ancho = alto * ANCHO_PX / ALTO_PX
    util = (ANCHO_PX - 2 * args.margen) / ANCHO_PX
    print('Ve {:.2f} de ancho ({:.2f} sin los márgenes) y {:.2f} de alto.'.format(ancho, ancho * util, alto))
    minimas = []
    if args.ancho:
        minimas.append(args.ancho / (tangente * ANCHO_PX / ALTO_PX * util))
    if args.alto:
        minimas.append(args.alto / tangente)
    if minimas:
        minima = max(minimas)
        print('{}: distancia mínima {:.2f} con fov {:g} (esta pose: {:g}).'.format(
            'CABE' if args.distancia >= minima else 'NO CABE', minima, args.fov, args.distancia))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
