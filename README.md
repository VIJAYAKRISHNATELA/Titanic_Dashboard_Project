# Titanic Dashboard & REST API

A Python data analysis project that explores the Titanic passenger dataset, generates interactive visualizations, and provides dataset statistics through a FastAPI REST API.

## Features

- Data analysis and processing using Pandas.
- Five visualizations using Matplotlib, Seaborn, and Plotly.
- Interactive dashboard exported as HTML.
- Dashboard image exported as PNG.
- FastAPI REST API for Titanic dataset statistics.
- Pydantic response validation.
- Application logging.
- Automated tests using pytest.
- Test coverage measurement using pytest-cov.
- Editable Python package installation.

## Project Structure

```text
Titanic_Dashboard_Project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── pipeline.py
│   ├── logging_config.py
│   └── schemas.py
├── tests/
│   ├── conftest.py
│   ├── test_pipeline.py
│   ├── test_logging.py
│   ├── test_api.py
│   └── test_services.py
├── logs/
├── dashboard.py
├── titanic_cleaned.parquet
├── titanic_dashboard.html
├── titanic_dashboard.png
├── requirements.txt
└── pyproject.toml
```

## Installation

Clone the repository:

```bash
git clone https://github.com/VIJAYAKRISHNATELA/Titanic_Dashboard_Project.git
cd Titanic_Dashboard_Project
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the project and development dependencies:

```bash
python -m pip install -e ".[dev]"
```

## Run the FastAPI Application

```bash
python -m uvicorn app.main:app --reload
```

Open these URLs in your browser:

- API home: http://127.0.0.1:8000/
- Dataset statistics: http://127.0.0.1:8000/stats
- Interactive API documentation: http://127.0.0.1:8000/docs

## Run Tests

Run all tests:

```bash
python -m pytest -v
```

Run tests with coverage:

```bash
python -m pytest --cov=app --cov-report=term-missing
```

## API Statistics

The `/stats` endpoint returns:

- Total passengers
- Number of survivors
- Number of passengers who did not survive
- Survival rate
- Average passenger age
- Average ticket fare

## Technologies Used

Python, Pandas, Matplotlib, Seaborn, Plotly, FastAPI, Pydantic, Uvicorn, Pytest, pytest-cov, and Git.

## Test Results

The project currently passes **24 automated tests with 100% code coverage for the `app` package**.

## Author

Titanic Dashboard Project — Python Track 1 Capstone.
