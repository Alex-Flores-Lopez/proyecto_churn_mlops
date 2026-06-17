# Propuesta de monitoreo aplicada

| Métrica seleccionada | Tipo | Señal de alerta | Acción propuesta |
|---|---|---|---|
| Estado de /health | Técnica | El endpoint no responde | Revisar estado del contenedor y reiniciar servicio |
| Errores 422 | Técnica | Aumento abrupto de solicitudes inválidas | Revisar integración o formato de datos enviados |
| Proporción de alto riesgo | Modelo | Cambio anormal en la distribución de predicciones | Analizar datos recientes y validar comportamiento |
| Probabilidad promedio | Modelo | Variación sostenida respecto al comportamiento esperado | Evaluar posible drift y considerar reentrenamiento |