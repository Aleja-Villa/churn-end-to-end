from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_read_root():
  response = client.get("/")
  assert response.status_code == 200
  assert "mensaje" in response.json()


def test_predict_churn():
  response = client.post(
      "/predict",
      json={"features": [0.5, 1.2, 0.0, 1.5, 0.8, 0.3, 1.1, 0.4, 0.9, 0.2]},
  )
  assert response.status_code == 200
  data = response.json()
  assert "churn_prediccion" in data
  assert "probabilidad_fuga" in data