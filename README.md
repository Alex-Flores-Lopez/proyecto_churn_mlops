# Proyecto Churn ML-Ops

Este proyecto implementa una estructura básica de ML-Ops para un modelo de predicción de abandono de clientes.

## Objetivo

Organizar un flujo reproducible, trazable y versionable para un modelo de Machine Learning.

## Instalación

pip install -r requirements.txt

## Ejecución del entrenamiento

python src/entrenar_modelo.py

## Ejecución de la API

uvicorn api.main:app --reload

## Estructura

- data/: descripción del dataset.
- src/: código de preparación, entrenamiento y evaluación.
- models/: modelos entrenados.
- api/: servicio de predicción.
- tests/: pruebas.
- docs/: métricas y documentación técnica.