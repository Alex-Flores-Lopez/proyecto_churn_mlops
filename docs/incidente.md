# Escenario de error o incidente

Durante la práctica se presentó un incidente real relacionado con la actualización del contenedor Docker.

| Elemento | Respuesta |
|---|---|
| Síntoma | El endpoint `/health` devolvía `{"detail":"Not Found"}`. |
| Posible causa | El contenedor estaba ejecutando una imagen Docker antigua que no tenía los cambios recientes del archivo `api/main.py`. |
| Forma de detección | Se comparó el código actualizado con la respuesta obtenida desde el navegador y Swagger. |
| Evidencia que revisaría | Respuesta de `/health`, Swagger, `docker ps` y `docker logs churn-api-flores-container`. |
| Acción correctiva | Detener y eliminar el contenedor, reconstruir la imagen y volver a ejecutar el contenedor actualizado. |
| Acción preventiva | Reconstruir la imagen después de cambios importantes y validar `/health`, `/docs` y `/info` antes de considerar la API lista. |