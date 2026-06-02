# Métricas del modelo

## Mini experimento: Random Forest

Nombre de la rama creada: feature/random-forest-v2  
Archivo modificado: src/entrenar_modelo.py  
Archivo de documentación modificado: docs/metricas_modelo.md  

## Resultados obtenidos

Accuracy: 0.9700  
Precision: 0.9904  
Recall: 0.9537  
F1-score: 0.9717  

## Explicación del cambio

Se realizó una modificación controlada dentro del proyecto ML-Ops mediante la creación de una rama independiente denominada feature/random-forest-v2.

El cambio consistió en entrenar un segundo algoritmo de Machine Learning utilizando Random Forest Classifier. Además, se agregaron métricas adicionales como Precision, Recall y F1-score para complementar la evaluación del modelo.

## Interpretación

Los resultados obtenidos muestran un Accuracy de 0.9700 y un F1-score de 0.9717, lo que indica un buen desempeño del modelo sobre el conjunto de prueba.

La métrica Precision de 0.9904 indica que el modelo tiene una alta exactitud al clasificar clientes positivos, mientras que el Recall de 0.9537 muestra que logra identificar correctamente la mayoría de los casos positivos.

Este experimento permite evidenciar trazabilidad, versionamiento y control de cambios dentro del flujo ML-Ops.