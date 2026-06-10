# Restful Booker API Automation

This project contains API automation tests for the Restful Booker API as part of the Camascope assessment.

## Tech Stack

* Python
* Pytest
* Requests
* JSON Schema validation
* Pytest HTML report
* GitHub Actions

## Project Structure

```text
tests/                 API test cases
schemas/               JSON schemas for response validation
utils/                 Common API client and helper methods
test_data/             Test payloads
conftest.py            Shared pytest fixtures
pytest.ini             Pytest settings
requirements.txt       Project dependencies
```

## Setup

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Tests

```bash
pytest
```

To generate the HTML report manually:

```bash
pytest --html=reports/report.html --self-contained-html
```

## Notes

* The tests use the public Restful Booker demo API.
* Some exploratory tests are marked as expected failures where the API behaviour is weak or inconsistent.
* Test data is kept separately to make the tests easier to update.
* The booking fixture creates test data before the test and cleans it up afterwards where possible.

## Assumptions

* The public API is available during test execution.
* Test bookings can be created, updated, and deleted.
* Performance testing is not included in this assessment.
* Some validation rules are assumed because the API documentation does not define all limits clearly.
