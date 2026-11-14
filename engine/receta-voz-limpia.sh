#!/bin/bash
# Voz limpia (sin efecto celular). Uso: receta-voz-limpia.sh entrada.wav salida.wav
# Cadena ligera: 48 kHz, pasa-altos suave, -1.5 dB de zona turbia, +1.5 dB presencia,
# de-esser suave, compresor suave (2:1) y nivel final parejo (-18 LUFS). Sin eco, reverb ni saturacion.
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
FF="${HUMANIFY_FFMPEG:-$ROOT/node_modules/ffmpeg-static/ffmpeg}"
IN="$1"; OUT="$2"
DUR=$("$FF" -i "$IN" 2>&1 | awk -F'[:, ]+' '/Duration/{print $3*3600+$4*60+$5}')
NS=$(awk "BEGIN{printf \"%d\", $DUR*48000+0.5}")
"$FF" -y -v error -i "$IN" -af "aresample=48000,highpass=f=70:poles=2,equalizer=f=300:t=q:w=1:g=-1.5,equalizer=f=3500:t=q:w=0.8:g=1.5,deesser=i=0.3:m=0.5:f=0.5,acompressor=threshold=-24dB:ratio=2:attack=15:release=150:makeup=2,loudnorm=I=-18:TP=-3:LRA=9,aresample=48000,apad=pad_len=96000,atrim=end_sample=$NS" -ar 48000 -ac 1 -c:a pcm_s16le "$OUT"
