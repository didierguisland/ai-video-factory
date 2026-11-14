#!/usr/bin/python3
"""Copia ligera para redes y para el chat: copia-ligera.py <video.mp4> <ligero.mp4> [--max-mb 28].
Empieza en crf 23 (FALLA 22) y sube hasta que quepa; si ni en crf 32 cabe, falla con el peso real."""
import argparse
import os
from pathlib import Path
import subprocess
import sys

FFMPEG = os.environ.get('HUMANIFY_FFMPEG', str(Path(__file__).resolve().parent.parent / 'node_modules/ffmpeg-static/ffmpeg'))


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('video')
    p.add_argument('ligero')
    p.add_argument('--max-mb', type=float, default=28)
    args = p.parse_args(argv)
    destino = Path(args.ligero)
    for crf in (23, 26, 29, 32):
        salida = subprocess.run([FFMPEG, '-y', '-loglevel', 'error', '-i', args.video, '-c:v', 'libx264', '-preset', 'slow',
                                 '-crf', str(crf), '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart',
                                 str(destino)], stdin=subprocess.DEVNULL, capture_output=True, text=True)
        if salida.returncode:
            print('copia-ligera: ' + salida.stderr[-400:], file=sys.stderr)
            return 1
        megas = destino.stat().st_size / 1e6
        if megas <= args.max_mb:
            print('{}: {:.1f} MB (crf {}).'.format(destino.name, megas, crf))
            return 0
    print('copia-ligera: {} pesa {:.1f} MB aun en crf 32 (tope {} MB).'.format(destino.name, megas, args.max_mb), file=sys.stderr)
    return 1


if __name__ == '__main__':
    sys.exit(main())
