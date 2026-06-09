from fastapi import FastAPI

app = FastAPI(title="Servicio ML-Ops - Churn")

@app.get("/")
def inicio():
    return {
        "mensaje": "Servicio ML-Ops activo",
        "estado": "ok",
        "autor": "Alex Flores López"
    }