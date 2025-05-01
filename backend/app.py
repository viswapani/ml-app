from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the model
model = joblib.load("model.joblib")

app = FastAPI()

# Define input format
class IrisRequest(BaseModel):
    features: list  # expecting list of 4 numbers

@app.post("/predict")
def predict_species(request: IrisRequest):
    features = np.array(request.features).reshape(1, -1)
    prediction = model.predict(features)
    return {"prediction": int(prediction[0])}
