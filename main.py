
from pathlib import Path

import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# Locate the dataset
BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "titanic_cleaned.parquet"

# Load dataset
df = pd.read_parquet(DATASET_PATH)

# Create FastAPI application
app = FastAPI(
    title="Titanic Dashboard API",
    description="API providing Titanic dataset statistics",
    version="1.0.0"
)


# Pydantic response model
class DatasetStats(BaseModel):
    total_passengers: int
    survived: int
    not_survived: int
    survival_rate: float
    average_age: float
    average_fare: float


# Home route
@app.get("/")
def home():
    return {
        "message": "Titanic Dashboard API is running!",
        "stats_endpoint": "/stats",
        "documentation": "/docs"
    }


# Statistics route
@app.get("/stats", response_model=DatasetStats)
def get_stats():

    total = int(len(df))
    survived = int(df["Survived"].sum())
    not_survived = total - survived

    return {
        "total_passengers": total,
        "survived": survived,
        "not_survived": not_survived,
        "survival_rate": round((survived / total) * 100, 2) if total else 0.0,
        "average_age": round(float(df["Age"].mean()), 2),
        "average_fare": round(float(df["Fare"].mean()), 2)
    }
