# Mundos: cómo se escoge uno nuevo y cuáles ya se usaron

Didier (4-nov): «no en la misma mesa, no los mismos elementos… libertad completa para colores, texturas». Se hereda cómo pensamos y elegimos, nunca el mundo.

## Método en 7 pasos
1. **Oración física.** Sujeto, verbo y giro de la idea, sin nombrar el tema: «algo grande resulta chico, pero se queda».
2. **El lugar del gancho.** ¿Dónde vive esa escena en la vida de la señora? Se saca del gancho, no del dato.
3. **Cinco materiales y sus verbos.** Material y lo que sabe hacer: el agua sube, el metal se abolla, la luz se cuela. Si no da un verbo que la metáfora use, se cambia. Un objeto chico del oficio de ese material suele dar la mejor acción.
4. **Protagonista.** El único objeto de material distinto; le pasan al menos 4 cosas.
5. **Escala y punto de vista.** Juguete, hormiga, vista de pájaro, interior. Decide la cámara dominante.
6. **Paleta y luz.** Un neutro, hasta 5 colores de trabajo y un acento solo para el protagonista. Una luz con una idea.
7. **Toma que paga y salida.** ¿Qué se revela al final? Debe explicar la idea sin palabras. No tiene que ser abrir la cámara: puede ser un corte, una luz que cambia o algo que cae.

## Regla contra la repetición
**PROHIBIDOS: mesa, tren, pesita, vestido, camino, papel, cartulina, lino, tela, manta**
Es la línea que lee el motor: mesa, tren, pesita y vestido los vetó Didier (4-nov); lo demás es el mundo del primer video. Valen para la metáfora de `01-CONCEPTO.md` y para el bloque MUNDO. El motor las revisa por palabras en las etapas `tema` y `direccion`, junto con el registro de abajo: da una vuelta para cambiarlas y lo que quede lo ve el orquestador como alerta. Cada veto nuevo de Didier se agrega aquí y en `ENCARGO-DIRECCION.md`.

Cada mundo cambia al menos **5 de los 8 ejes** contra el anterior y no repite **material base, protagonista ni columna** de ninguno de los de abajo. Tampoco repite sus objetos grandes. Material de **otra familia, no un sinónimo**: papel y lino contra cartulina y manta es el mismo mundo. Un cambio de escala no alcanza: la escala se puede repetir. Lo que no cambia: método, ritmo, zonas, voz, marca. El encargo no adjunta imágenes de mundos anteriores: el método viaja en palabras. Riesgo vigilado: caer siempre en «un viaje por un camino»; cambiar la columna ayuda.

Vetos fijos de estilo: 3D genérico o de plástico, y el estilo del video del pelo («cero me gustó», 01:55).

## Límites técnicos
**Comprobado:** Three.js r159, `render(t)` puro; Extrude, Lathe, Tube, Box, Cylinder, Torus, Sphere, Capsule; `MeshStandardMaterial` con grano y bump; telas con `CanvasTexture` y normales; metal con envMap; sombras PCFSoft 4096, ACES; `InstancedMesh` (195 piezas sin costo visible); aditivo para halos; capa 2D que sigue objetos proyectando el punto; texto en `CanvasTexture`; recortes de foto con borde y sombra. Render 1080×1920: unos 158 s por 59 s de video.

**Comprobado que falla:** recortes con cámara rodeando (dorso blanco); tejido muy de cerca (petate); rojo brillante (plástico); globo por gajos (calabaza); objeto grande sin referencia (la pesa parecía campana); elemento chico en plano general (no se lee); coordenadas sin ver el cuadro.

**No probado, con prueba de un cuadro y alternativa escrita:** vidrio y hielo con refracción, agua o líquidos, humo volumétrico, clearcoat, emisivos en masa (más de 100), noche con poca luz, comida 100 % en geometría, cuerpos o caras en 3D, simulación física (no cabe en `render(t)` puro si acumula estado). Regla: si un supuesto es lo único que descarta una idea, primero la prueba mínima (REGLAS.md).

## Registro de mundos usados
`herramientas/mundo-registrar.py` agrega la fila al cerrar cada video.

| Video | Material base | Luz | Paleta | Escala | Columna | Cámara | Protagonista | Salida | Objetos grandes |
|---|---|---|---|---|---|---|---|---|---|
| 01-medio-kilo-fantasma | Papel y lino | Rasante, cálida, de día | Hueso, coral, salvia, vino | Juguete sobre mesa | Camino en S, horizontal | Lateral, sube a cenital | Pesita de latón | Baja y entra por ventana | Tren, vestido, globo, mesa, camino |
| 01-pilot-1 | Acero esmaltado mate y madera de haya imantada | Cenital de recibidor con contraluz frío de mañana | Petróleo, crema haya, mandarina, ámbar, menta, cian | Mural vertical a altura de pecho | Cuadrícula mural vertical de 7 columnas y 4 semanas | Frontal de muro con pull-back perpendicular | Tenis corredor de malla cian y suela de goma | Cuadro quieto en casilla del martes con tarjeta y topper imantado | Pizarra de acero, calendario, fichas imantadas, tenis |
