from fastapi import FastAPI
from pydantic import BaseModel
import joblib


app = FastAPI(
    title="MLOps Model API",
    description="Machine Learning model deployment API",
    version="1.0.0"
)


# Load trained model
model = joblib.load("model/model.pkl")


class PredictionRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/")
def home():
    return {
        "message": "MLOps Model API is running successfully"
    }


@app.post("/predict")
def predict(request: PredictionRequest):
    features = [[
        request.sepal_length,
        request.sepal_width,
        request.petal_length,
        request.petal_width
    ]]

    prediction = model.predict(features)[0]

    return {
        "prediction": int(prediction)
    }
