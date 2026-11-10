import pandas as pd
import pytest


@pytest.fixture
def sample_titanic_df():
    """Provide a small Titanic DataFrame for testing."""

    data = {
        "PassengerId": [1, 2, 3, 4, 5],
        "Survived": [0, 1, 1, 0, 1],
        "Pclass": [3, 1, 2, 3, 1],
        "Sex": ["male", "female", "female", "male", "male"],
        "Age": [22, 38, 26, 35, 28],
        "Fare": [7.25, 71.28, 7.92, 8.05, 80.0],
        "Embarked": ["S", "C", "S", "S", "C"]
    }

    return pd.DataFrame(data)