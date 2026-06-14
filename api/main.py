from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Servicio ML-Ops - Churn")

AUTOR = "Alex Flores López"
VERSION_MODELO = "modelo_churn_v1"


# Modelo de entrada para /predict
class Cliente(BaseModel):
    antiguedad: int
    cargo_mensual: float
    reclamos: int


# Endpoint raíz
@app.get("/")
def inicio():
    return {
        "mensaje": "Servicio ML-Ops activo",
        "estado": "ok",
        "autor": AUTOR
    }


# Endpoint health
@app.get("/health")
def health():
    return {
        "estado": "ok",
        "modelo": VERSION_MODELO,
        "autor": AUTOR
    }


# Endpoint predict
@app.post("/predict")
def predict(cliente: Cliente):

    # Validación simple
    if cliente.antiguedad < 0 or cliente.antiguedad > 120:
        return {
            "error": "La antigüedad debe estar entre 0 y 120"
        }

    if cliente.reclamos < 0:
        return {
            "error": "Los reclamos no pueden ser negativos"
        }

    # Regla académica simple
    riesgo = (
        cliente.cargo_mensual > 100
        or cliente.reclamos >= 3
        or cliente.antiguedad < 12
    )

    return {
        "prediccion": "alto_riesgo" if riesgo else "bajo_riesgo",
        "probabilidad": 0.82 if riesgo else 0.18,
        "version_modelo": VERSION_MODELO,
        "autor": AUTOR
    }


# Mejora técnica personal
@app.get("/info")
def info():
    return {
        "servicio": "API predictiva de churn",
        "version_modelo": VERSION_MODELO,
        "autor": AUTOR,
        "variables": [
            "antiguedad",
            "cargo_mensual",
            "reclamos"
        ]
    }