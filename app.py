from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="ChurnGuard API",
    description="API de Predicción de Fuga de Clientes con Datos Reales",
)


# 1. Definimos los datos reales y legibles que el usuario va a ingresar
class ClienteReal(BaseModel):
  antiguedad_meses: int  # Ej: 12 meses
  facturacion_mensual: float  # Ej: 75.5
  reclamos_soporte: int  # Ej: 2 reclamos
  consumo_datos_gb: float  # Ej: 15.0 GB
  dias_mora_pago: int  # Ej: 3 días de retraso
  tipo_contrato: int  # 0: Mensual, 1: Anual
  servicios_adicionales: int  # Ej: 2 servicios extra
  accesos_app_mes: int  # Ej: 10 veces al mes
  satisfaccion_nps: int  # Ej: 8 (de 1 a 10)
  descuentos_recibidos: float  # Ej: 10.0


@app.get("/")
def read_root():
  return {
      "mensaje": (
          "Bienvenido a la API de Predicción de Churn con Datos Reales 🚀"
      )
  }


@app.post("/predict")
def predecir_churn_real(cliente: ClienteReal):
  # Aquí simulamos la lógica del modelo basada en las reglas de negocio reales:
  # (Si tiene muchos reclamos, mora alta y baja antigüedad, el riesgo sube)
  riesgo_calculado = (
      (cliente.reclamos_soporte * 0.25)
      + (cliente.dias_mora_pago * 0.15)
      - (cliente.antiguedad_meses * 0.02)
  )

  # Determinamos la probabilidad simulada entre 0 y 1
  probabilidad = min(max(riesgo_calculado, 0.05), 0.95)
  prediccion = 1 if probabilidad > 0.5 else 0

  # Generamos una recomendación comercial automática según el resultado
  if prediccion == 1:
    mensaje = (
        "¡Alerta! El cliente tiene alto riesgo de fuga. Se recomienda ofrecer"
        " un descuento o soporte prioritario."
    )
  else:
    mensaje = "El cliente se encuentra estable y satisfecho con el servicio."

  return {
      "datos_ingresados": cliente.dict(),
      "churn_prediccion": prediccion,
      "probabilidad_fuga": round(probabilidad, 2),
      "recomendacion": mensaje,
  }