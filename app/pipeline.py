from pathlib import Path
import pandas as pd
import logging
logger = logging.getLogger(__name__)

DATA_FILE = (
    Path(__file__).resolve().parent.parent
    / "titanic_cleaned.parquet"
)


def load_dataset():
    """Load the cleaned Titanic dataset."""

    logger.info("Loading Titanic dataset")

    df = pd.read_parquet(DATA_FILE)

    logger.info(
        "Dataset loaded successfully. Shape: %s",
        df.shape
    )

    return df


def validate_dataset(df: pd.DataFrame) -> None:
    logger.info("Validating Titanic dataset")
    """Validate the cleaned Titanic dataset."""

    required_columns = [
        "PassengerId",
        "Survived",
        "Pclass",
        "Sex",
        "Age",
        "Fare"
    ]

    # Check whether the DataFrame is empty
    if df.empty:
        raise ValueError("Dataset is empty.")

    # Check whether required columns exist
    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # Check for missing values in important columns
    if df[required_columns].isnull().any().any():
        raise ValueError(
            "Dataset contains missing values in required columns."
        )

    # Check valid survival values
    if not df["Survived"].isin([0, 1]).all():
        raise ValueError(
            "Survived column must contain only 0 and 1."
        )
        logger.info("Dataset validation successful")
    return None



def calculate_statistics(df: pd.DataFrame) -> dict:
    logger.info("Calculating Titanic statistics")
    """Calculate summary statistics for Titanic passengers."""

    validate_dataset(df)
    logger.info("Dataset is valid. Starting statistics calculation")

    total_passengers = len(df)

    survived = int(df["Survived"].sum())

    not_survived = total_passengers - survived

    survival_rate = round(
        (survived / total_passengers) * 100, 2
    )

    average_age = round(df["Age"].mean(), 2)

    average_fare = round(df["Fare"].mean(), 2)

    return {
        "total_passengers": total_passengers,
        "survived": survived,
        "not_survived": not_survived,
        "survival_rate": survival_rate,
        "average_age": average_age,
        "average_fare": average_fare
    }