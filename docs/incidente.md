# Escenario de error o incidente

| Elemento | Respuesta |
|---|---|
| Síntoma | El endpoint /health devolvía {"detail":"Not Found"}. |
| Posible causa | El contenedor estaba ejecutando una imagen Docker antigua que no incluía los endpoints actualizados. |
| Forma de detección | Se comparó el código actualizado con la respuesta obtenida desde el navegador y Swagger. |
| Evidencia que revisaría | Respuesta de /health, Swagger, docker ps y docker logs del contenedor. |
| Acción correctiva | Detener y eliminar el contenedor, reconstruir la imagen y ejecutar nuevamente el contenedor actualizado. |
| Acción preventiva | Reconstruir la imagen después de cambios importantes y verificar /health antes de realizar pruebas. |