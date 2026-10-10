# 🚀 ChurnGuard: Sistema de Machine Learning End-to-End

Sistema MLOps completo para la predicción de fuga de clientes (Customer Churn) en tiempo real, desarrollado como proyecto final.

---

## 📂 Estructura del Repositorio
```text
churn-end-to-end/
│
├── data/                  # Datos del proyecto
├── src/
│   ├── train.py           # Script de entrenamiento y tracking con MLflow
│   └── pipeline.py        # Pipeline de orquestación con Prefect
├── tests/
│   └── test_app.py        # Pruebas unitarias de calidad (pytest)
├── app.py                 # API de despliegue en tiempo real con FastAPI
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Documentación y guía de reproducción


Instrucciones de Reproducción:
1. Instalar las dependencias ejecutando el comando: pip install -r requirements.txt
2. Ejecutar el script de entrenamiento y tracking con MLflow escribiendo: python src/train.py
3. Ejecutar las pruebas unitarias de calidad con pytest usando: $env:PYTHONPATH="."; pytest
4. Iniciar el despliegue del Web Service con FastAPI ejecutando: uvicorn app:app --reload
Una vez que el servidor esté activo, puedes abrir la documentación interactiva en tu navegador en la dirección: http://127.0.0.1:8000/docs


USO DE LA APP 

1. Para poner en marcha la aplicación, ejecutamos el servidor Uvicorn con el comando uvicorn app:app --reload en la terminal. 

2. ACCEDER A LA INTERFAZ
Una vez que el servidor está activo, la API despliega automáticamente una interfaz interactiva basada en Swagger UI a la cual accedemos abriendo nuestro navegador web en la ruta http://127.0.0.1:8000/docs. 

3. PRUEBA - SIMULACIÓN 
Dentro de esta interfaz, seleccionamos el endpoint de predicción, hacemos clic en "Try it out" e introducimos un arreglo JSON con las 10 variables numéricas normalizadas del cliente que queremos evaluar. 

4. INTERPRETACIÓN DEL RESULTADO
Finalmente, al hacer clic en "Execute", el modelo procesa los datos en tiempo real y nos devuelve el resultado de la predicción de fuga junto con su probabilidad matemática, permitiendo que cualquier sistema externo consuma esta información al instante.