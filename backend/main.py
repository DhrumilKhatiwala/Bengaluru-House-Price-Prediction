from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
import os
from models import PredictionRequest, PredictionResponse
import random

app = FastAPI(title="Bengaluru House Price Prediction API")

# Allow CORS for the frontend React app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "data", "model.pkl")
model = None

import pickle

CSV_PATH = os.path.join(os.path.dirname(__file__), "data", "bengaluru_house_prices.csv")
unique_options = {
    "locations": [],
    "sizes": [],
    "availabilities": []
}

@app.on_event("startup")
def load_model_and_data():
    global model, unique_options
    if os.path.exists(MODEL_PATH):
        try:
            with open(MODEL_PATH, 'rb') as f:
                model = pickle.load(f)
            print("Model loaded successfully.")
        except Exception as e:
            print(f"Error loading model: {e}")
    else:
        print(f"Warning: Model not found at {MODEL_PATH}. Using fallback predictions.")
        
    if os.path.exists(CSV_PATH):
        try:
            df = pd.read_csv(CSV_PATH)
            unique_options["locations"] = sorted(list(set([str(x).strip() for x in df['location'].dropna().tolist() if str(x).strip()])))
            
            # Filter and sort sizes (keep only BHK <= 10)
            import re
            raw_sizes = set([str(x).strip() for x in df['size'].dropna().tolist() if str(x).strip()])
            valid_sizes = [s for s in raw_sizes if "BHK" in s and re.match(r'^\d+', s) and int(re.match(r'^\d+', s).group()) <= 10]
            unique_options["sizes"] = sorted(valid_sizes, key=lambda s: (int(re.match(r'^\d+', s).group()), s))
            
            # Filter availability to only specific options
            avail_options = ["Ready To Move", "Immediate Possession"]
            unique_options["availabilities"] = [opt for opt in avail_options if opt in df['availability'].values]
            if not unique_options["availabilities"]:
                unique_options["availabilities"] = avail_options # Fallback just in case
            print("CSV options loaded successfully.")
        except Exception as e:
            print(f"Error loading CSV data: {e}")

@app.get("/api/options")
def get_options():
    return unique_options
@app.post("/api/predict", response_model=PredictionResponse)
def predict_price(request: PredictionRequest):
    # In a real scenario, we'd use the loaded model:
    # features = pd.DataFrame([request.model_dump()])
    # prediction = model.predict(features)[0]
    
    # Using placeholder logic if real model predicting fails or isn't there
    if model is not None:
        try:
            features = pd.DataFrame([request.model_dump()])
            prediction = model.predict(features)[0]
            return PredictionResponse(predicted_price=round(float(prediction), 2))
        except Exception as e:
            print(f"Prediction failed with real model, falling back. Error: {e}")
            
    # Fallback to a placeholder random price between 30 and 300 (Lakhs)
    # Adds some basic deterministic behavior based on total_sqft if possible
    try:
        # Extract numeric from something like '1056'
        sqft_val = float(request.total_sqft.split('-')[0].strip())
        placeholder_price = sqft_val * 0.05 + random.uniform(-10, 10)
    except:
        placeholder_price = random.uniform(30.0, 300.0)
        
    return PredictionResponse(predicted_price=round(placeholder_price, 2))

@app.get("/")
def read_root():
    return {"message": "Welcome to the Bengaluru House Price Prediction API"}
