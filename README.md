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

# Proyecto Final ML-Ops - API Predictiva de Churn

## Descripción
Este proyecto implementa una API predictiva para estimar el riesgo de abandono de clientes mediante FastAPI. La solución incluye un modelo serializado, endpoints de consulta y predicción, ejecución local y ejecución contenerizada con Docker.

## Endpoints principales
- GET / : verifica que la API responde.
- GET /health : verifica el estado del servicio y modelo.
- POST /predict : recibe datos del cliente y devuelve una predicción.
- GET /info : mejora técnica incorporada para consultar versión del modelo, autor y variables utilizadas.

## Ejecución local
```bash
python -m uvicorn api.main:app --host 127.0.0.1 --port 8000