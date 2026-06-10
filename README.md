<<<<<<< HEAD
# Restful Booker API Automation

This project contains automated API tests for the Restful Booker API.

## Tech Stack

- Python
- Pytest
- Requests
- JSON Schema
- Pytest HTML Reporting
- GitHub Actions

## Project Structure

```text
tests/                 Automated test cases
schemas/               API response schemas
utils/                 Reusable API client and schema validator
test_data/             Test payloads
.github/workflows/     CI pipeline
.vscode/               VS Code pytest configuration
conftest.py            Pytest fixtures and shared setup
pytest.ini             Pytest configuration
reports/               HTML test report output
```

## Setup

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Tests

```bash
pytest
```

The project is configured to automatically generate:

```text
reports/report.html
```

You can also run explicitly:

```bash
pytest --html=reports/report.html --self-contained-html
```

## Test Data Cleanup

The `booking` fixture in `conftest.py` creates a booking before a test and deletes it after the test using pytest's `yield` fixture pattern.

## Booking Test Data Reference

A detailed description of the booking payloads used by tests is available in `test_data/booking_data.md`.

## Exploratory Finding Tests

Additional exploratory negative tests are in:

```text
tests/test_exploratory_findings.py
```

Some tests are marked with `pytest.mark.xfail` because they document known behaviours of the public demo API without failing the whole suite.

## Assumptions

1. The public API is available during test execution.
2. Authentication token remains valid for the test run.
3. Created bookings can be deleted after test execution.
4. Some validation behaviour may be weak because this is a public demo API.
5. Performance testing is out of scope.
6. The API documentation does not specify minimum or maximum lengths for firstname and lastname. For demonstration of contract validation, minLength=1 and maxLength=100 were assumed as reasonable business constraints.

## CI/CD

The CI version includes:

```text
.github/workflows/api-tests.yml
```

It installs dependencies, runs pytest, generates an HTML report, and uploads the report as a GitHub Actions artifact.
=======
# Camascope-test-assessment
API test assessment for Camascope
>>>>>>> d23f76b167f651e3891c7ed748775234f7001c6d
