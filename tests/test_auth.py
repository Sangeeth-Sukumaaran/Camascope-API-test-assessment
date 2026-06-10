import requests

from conftest import BASE_URL
from schemas.auth_schema import AUTH_SCHEMA
from utils.schema_validator import validate_schema


def test_generate_auth_token():
    # Authenticate with valid credentials and verify the API returns a valid token.
    response = requests.post(
        f"{BASE_URL}/auth",
        json={"username": "admin", "password": "password123"},
        timeout=10
    )

    assert response.status_code == 200
    response_data = response.json()
    validate_schema(response_data, AUTH_SCHEMA)
    assert response_data["token"]


def test_invalid_login_does_not_return_token():
    # Use invalid credentials to confirm authentication fails and no token is issued.
    response = requests.post(
        f"{BASE_URL}/auth",
        json={"username": "wrong", "password": "wrong"},
        timeout=10
    )

    # The API returns a 200 response with an error payload for invalid login attempts.
    assert response.status_code == 200
    response_data = response.json()
    assert "token" not in response_data
    assert response_data.get("reason") == "Bad credentials"
