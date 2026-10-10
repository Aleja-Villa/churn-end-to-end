from prefect import flow, task
import mlflow
import mlflow.sklearn
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split


@task(name="Generar y Preparar Datos")
def get_data():
  X, y = make_classification(n_samples=1000, n_features=10, random_state=42)
  return train_test_split(X, y, test_size=0.2, random_state=42)


@task(name="Entrenar Modelo")
def train_model(X_train, y_train):
  model = RandomForestClassifier(
      n_estimators=100, max_depth=5, random_state=42
  )
  model.fit(X_train, y_train)
  return model


@task(name="Validar Modelo y Registrar en MLflow")
def evaluate_and_log(model, X_test, y_test):
  mlflow.set_experiment("churn_prefect_experiment")
  with mlflow.start_run():
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)

    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("f1_score", f1)
    mlflow.sklearn.log_model(
        model, "model", skops_trusted_types=["sklearn.tree._tree.Tree"]
    )
    print(
        f"Pipeline Ejecutado - Accuracy: {acc:.4f}, F1-Score: {f1:.4f}"
    )


@flow(name="Churn MLOps Pipeline")
def main_pipeline():
  X_train, X_test, y_train, y_test = get_data()
  model = train_model(X_train, y_train)
  evaluate_and_log(model, X_test, y_test)


if __name__ == "__main__":
  main_pipeline()