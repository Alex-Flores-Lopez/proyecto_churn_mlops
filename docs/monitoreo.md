# Propuesta de monitoreo aplicada

Para operar la API predictiva de churn no basta con verificar que el servicio responda. También es necesario observar el comportamiento técnico del servicio y el comportamiento de las predicciones generadas por el modelo.

| Métrica seleccionada | Tipo | Señal de alerta | Acción propuesta |
|---|---|---|---|
| Estado de `/health` | Técnica | El endpoint no responde o devuelve error | Revisar el estado del contenedor y consultar los logs |
| Errores 422 | Técnica | Aumento abrupto de solicitudes inválidas | Revisar el formato de datos enviado por el sistema consumidor |
| Proporción de predicciones `alto_riesgo` | Modelo | Cambio anormal en la cantidad de clientes clasificados como alto riesgo | Analizar los datos recientes y validar si cambió el comportamiento de los clientes |
| Probabilidad promedio | Modelo | Variación sostenida en la probabilidad promedio de churn | Evaluar posible drift y considerar reentrenamiento del modelo |

Como alerta prioritaria se considera que `/health` deje de responder, ya que esto indica que el servicio no está disponible para otros sistemas. La acción inicial sería revisar el contenedor, consultar `docker logs` y reiniciar el servicio si corresponde.