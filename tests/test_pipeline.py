from unittest.mock import patch

from app.pipeline import load_dataset, DATA_FILE




import pytest
from unittest.mock import patch

from app.pipeline import load_dataset, DATA_FILE

from app.pipeline import (
    load_dataset,
    validate_dataset,
    calculate_statistics,
    DATA_FILE
)


def test_sample_dataframe(sample_titanic_df):
    assert len(sample_titanic_df) == 5
    assert "Survived" in sample_titanic_df.columns
    assert "Age" in sample_titanic_df.columns


def test_survival_count(sample_titanic_df):
    survived = sample_titanic_df["Survived"].sum()
    assert survived == 3


def test_average_age(sample_titanic_df):
    average_age = sample_titanic_df["Age"].mean()
    assert average_age == 29.8


def test_average_fare(sample_titanic_df):
    average_fare = sample_titanic_df["Fare"].mean()
    assert round(average_fare, 2) == 34.90


def test_passenger_count_by_gender(sample_titanic_df):
    gender_counts = sample_titanic_df["Sex"].value_counts()
    assert gender_counts["male"] == 3
    assert gender_counts["female"] == 2


@pytest.mark.parametrize(
    "column, value, expected_count",
    [
        ("Sex", "male", 3),
        ("Sex", "female", 2),
        ("Pclass", 1, 2),
        ("Pclass", 3, 2),
        ("Embarked", "S", 3),
        ("Embarked", "C", 2)
    ]
)
def test_value_counts(sample_titanic_df, column, value, expected_count):
    actual_count = sample_titanic_df[column].value_counts()[value]
    assert actual_count == expected_count


@patch("app.pipeline.pd.read_parquet")
def test_load_dataset(mock_read_parquet, sample_titanic_df):

    # Provide a fake DataFrame instead of reading the actual file
    mock_read_parquet.return_value = sample_titanic_df

    # Call the actual function
    result = load_dataset()

    # Verify that read_parquet was called with the correct path
    mock_read_parquet.assert_called_once_with(DATA_FILE)

    # Verify the returned DataFrame
    assert result.equals(sample_titanic_df)


def test_validate_dataset_success(sample_titanic_df):
    result = validate_dataset(sample_titanic_df)

    assert result is None


def test_validate_empty_dataset(sample_titanic_df):
    empty_df = sample_titanic_df.iloc[0:0]

    with pytest.raises(ValueError, match="Dataset is empty"):
        validate_dataset(empty_df)


def test_validate_missing_columns(sample_titanic_df):
    invalid_df = sample_titanic_df.drop(columns=["Age"])

    with pytest.raises(ValueError, match="Missing required columns"):
        validate_dataset(invalid_df)


def test_validate_missing_values(sample_titanic_df):
    invalid_df = sample_titanic_df.copy()
    invalid_df.loc[0, "Age"] = None

    with pytest.raises(ValueError, match="missing values"):
        validate_dataset(invalid_df)


def test_validate_invalid_survival_values(sample_titanic_df):
    invalid_df = sample_titanic_df.copy()
    invalid_df.loc[0, "Survived"] = 5

    with pytest.raises(ValueError, match="only 0 and 1"):
        validate_dataset(invalid_df)




def test_calculate_statistics(sample_titanic_df):

    result = calculate_statistics(sample_titanic_df)

    assert result["total_passengers"] == 5
    assert result["survived"] == 3
    assert result["not_survived"] == 2
    assert result["survival_rate"] == 60.0
    assert result["average_age"] == 29.8
    assert result["average_fare"] == 34.9