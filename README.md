# Proyecto Final ML-Ops - API Predictiva de Churn

## Descripción

Este proyecto implementa una API predictiva para estimar el riesgo de abandono de clientes (churn) utilizando FastAPI. La solución incluye un modelo serializado, validaciones de entrada, endpoints de consulta y predicción, ejecución local y despliegue mediante Docker.

Como mejora técnica se incorporó un endpoint informativo que permite consultar la versión del modelo, el autor del proyecto y las variables utilizadas por el servicio.

---

## Objetivo

Desarrollar una API reproducible, trazable y portable para exponer un modelo de Machine Learning mediante servicios REST, aplicando principios básicos de ML-Ops.

---

## Estructura del proyecto

```text
proyecto_churn_mlops/
│
├── api/
├── data/
├── docs/
├── models/
├── notebooks/
├── src/
├── tests/
├── Dockerfile
├── .dockerignore
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Endpoints disponibles

### GET /

Verifica que la API se encuentra disponible.

### GET /health

Permite consultar el estado del servicio y la versión del modelo.

### POST /predict

Recibe información de un cliente y devuelve una predicción de riesgo de abandono.

### GET /info

Endpoint adicional implementado como mejora técnica para consultar:

* versión del modelo;
* autor;
* variables utilizadas;
* descripción del servicio.

---

## Entrenamiento del modelo

```bash
python src/entrenar_modelo.py
```

Archivos generados:

```text
models/modelo_churn_v1.joblib
models/modelo_churn_v1_metadata.json
docs/metricas_modelo.md
```

---

## Ejecución local

```bash
python -m uvicorn api.main:app --host 127.0.0.1 --port 8000
```

Swagger:

```text
http://localhost:8000/docs
```

---

## Ejecución con Docker

Construcción de imagen:

```bash
docker build -t churn-api-flores .
```

Ejecución del contenedor:

```bash
docker run -d --name churn-api-flores-container -p 8000:8000 churn-api-flores
```

Verificación:

```bash
docker ps
docker logs churn-api-flores-container
```

---

## Mejora técnica implementada

Se incorporó el endpoint GET `/info` para mejorar la trazabilidad operativa de la API, permitiendo consultar información relevante del servicio sin necesidad de revisar el código fuente.

---

## Monitoreo propuesto

Métricas técnicas:

* disponibilidad del endpoint `/health`;
* cantidad de errores 422.

Métricas del modelo:

* proporción de predicciones de alto riesgo;
* probabilidad promedio generada por el modelo.

---

## Escenario de incidente analizado

Durante la práctica se presentó un incidente donde el endpoint `/health` devolvía una respuesta de tipo `Not Found` debido a que Docker estaba utilizando una imagen antigua.

La solución consistió en reconstruir la imagen y recrear el contenedor con la versión actualizada del servicio.

---

## Riesgo de drift identificado

Se identificó como riesgo principal un posible cambio en la distribución de variables como cargo mensual y cantidad de reclamos, lo cual podría afectar el comportamiento esperado del modelo y requerir reentrenamiento.

---

## Autor

Alex Flores López
