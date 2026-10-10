import mlflow
import mlflow.sklearn
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

# 1. Configurar experimento en MLflow
mlflow.set_experiment("churn_experiment_mvp")

with mlflow.start_run():
  # 2. Generar datos de prueba para el Churn MVP
  X, y = make_classification(
      n_samples=1000, n_features=10, random_state=42
  )
  X_train, X_test, y_train, y_test = train_test_split(
      X, y, test_size=0.2, random_state=42
  )

  # 3. Definir parámetros del modelo
  n_estimators = 100
  max_depth = 5

  # Registrar parámetros en MLflow
  mlflow.log_param("n_estimators", n_estimators)
  mlflow.log_param("max_depth", max_depth)

  # 4. Entrenar modelo
  model = RandomForestClassifier(
      n_estimators=n_estimators, max_depth=max_depth, random_state=42
  )
  model.fit(X_train, y_train)

  # 5. Evaluar métricas
  predictions = model.predict(X_test)
  acc = accuracy_score(y_test, predictions)
  f1 = f1_score(y_test, predictions)

  # Registrar métricas en MLflow
  mlflow.log_metric("accuracy", acc)
  mlflow.log_metric("f1_score", f1)

  # 6. Guardar artefacto del modelo
  mlflow.sklearn.log_model(
    model, "model", skops_trusted_types=["sklearn.tree._tree.Tree"]
)

  print(
      f"¡Entrenamiento exitoso! Accuracy: {acc:.4f}, F1-Score: {f1:.4f}"
  )