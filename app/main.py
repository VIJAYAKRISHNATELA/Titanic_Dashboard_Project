
from fastapi import FastAPI, HTTPException

from app.pipeline import load_dataset, calculate_statistics
from app.schemas import DatasetStats
from app.logging_config import setup_logging

# Configure application logging
setup_logging()

# Create FastAPI application
app = FastAPI(
    title="Titanic Dashboard API",
    description="API providing Titanic dataset statistics",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Titanic Dashboard API is running!",
        "stats_endpoint": "/stats",
        "documentation": "/docs"
    }


@app.get("/stats", response_model=DatasetStats)
def get_stats():

    try:
        logger_message = "Fetching Titanic dataset statistics"
        import logging
        logging.getLogger(__name__).info(logger_message)

        df = load_dataset()

        stats = calculate_statistics(df)

        return stats

    except (FileNotFoundError, ValueError) as error:
        import logging
        logging.getLogger(__name__).exception(
            "Unable to calculate Titanic statistics"
        )
        raise HTTPException(
            status_code=500,
            detail=str(error)
        ) from error
