# Riesgo de drift

El modelo de churn puede verse afectado si los datos actuales de los clientes cambian respecto a los datos usados durante el entrenamiento.

| Elemento | Respuesta |
|---|---|
| Riesgo identificado | Incremento sostenido del `cargo_mensual` o aumento de `reclamos` en clientes recientes. |
| Tipo de drift | Data drift. |
| Impacto | El modelo podría empezar a generar predicciones menos representativas, clasificando más clientes como alto riesgo sin que necesariamente el patrón original se mantenga. |
| Señal de alerta | Cambio sostenido en el promedio de `cargo_mensual`, aumento de `reclamos` o variación anormal de predicciones `alto_riesgo`. |
| Respuesta operativa | Revisar datos recientes, comparar distribuciones contra los datos originales y evaluar reentrenamiento si el cambio se mantiene. |