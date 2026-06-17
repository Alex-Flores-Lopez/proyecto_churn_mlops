# Riesgo de drift

| Elemento | Respuesta |
|---|---|
| Riesgo identificado | Incremento sostenido del cargo mensual o aumento de reclamos en los clientes recientes. |
| Tipo de drift | Data drift. |
| Impacto | El modelo podría generar predicciones menos representativas si las variables actuales se alejan de los datos usados en entrenamiento. |
| Señal de alerta | Variación sostenida en el promedio de cargo_mensual o aumento en la proporción de alto_riesgo. |
| Respuesta operativa | Revisar datos recientes, comparar distribuciones y evaluar reentrenamiento del modelo. |