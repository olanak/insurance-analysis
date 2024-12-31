from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Load the trained model
model = joblib.load('../models/best_model_xgb.pkl')

@app.get("/")
def read_root():
    return {"message": "Insurance Claims Prediction API is running!"}

@app.post("/predict/")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    
    # Convert numpy.float32 to native Python float
    return {"prediction": float(prediction[0])}
