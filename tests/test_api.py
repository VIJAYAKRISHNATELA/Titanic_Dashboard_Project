from unittest.mock import patch
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Titanic Dashboard API is running!"
    assert data["stats_endpoint"] == "/stats"
    assert data["documentation"] == "/docs"


def test_stats_endpoint():
    response = client.get("/stats")

    assert response.status_code == 200

    data = response.json()

    assert data["total_passengers"] == 891
    assert data["survived"] == 342
    assert data["not_survived"] == 549
    assert data["survival_rate"] == 38.38
    assert data["average_age"] == 29.36
    assert data["average_fare"] == 32.2


def test_stats_response_structure():
    response = client.get("/stats")

    data = response.json()

    expected_fields = {
        "total_passengers",
        "survived",
        "not_survived",
        "survival_rate",
        "average_age",
        "average_fare"
    }

    assert set(data.keys()) == expected_fields


def test_stats_handles_missing_dataset():

    with patch(
        "app.main.load_dataset",
        side_effect=FileNotFoundError("Dataset not found")
    ):
        response = client.get("/stats")

    assert response.status_code == 500
    assert response.json()["detail"] == "Dataset not found"


def test_stats_handles_invalid_dataset():

    with patch(
        "app.main.load_dataset",
        return_value=None
    ), patch(
        "app.main.calculate_statistics",
        side_effect=ValueError("Dataset is empty.")
    ):
        response = client.get("/stats")

    assert response.status_code == 500
    assert response.json()["detail"] == "Dataset is empty."
