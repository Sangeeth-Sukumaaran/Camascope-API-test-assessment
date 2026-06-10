import json
from pathlib import Path

import pytest
import requests

from utils.api_client import APIClient

# Base URL for the API under test.
BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture(scope="session")
def api_client():
    # Use a shared API client for the test session 
    return APIClient(BASE_URL)


@pytest.fixture(scope="session")
def booking_data():
    #  Reusable booking payloads from JSON
    data_path = Path(__file__).parent / "test_data" / "booking_data.json"
    with open(data_path, "r", encoding="utf-8") as file:
        return json.load(file)


@pytest.fixture(scope="session")
def auth_token():
    # Authenticate once for the test session 
    response = requests.post(
        f"{BASE_URL}/auth",
        json={"username": "admin", "password": "password123"},
        timeout=10
    )

    assert response.status_code == 200, "Auth token was not generated"
    token = response.json().get("token")
    assert token, "Auth response did not include token"

    return token


@pytest.fixture(scope="session")
def auth_session(auth_token):
    # Create a session with authentication headers for endpoints .
    session = requests.Session()
    session.headers.update({
        "Cookie": f"token={auth_token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    return session


@pytest.fixture(scope="session")
def authenticated_client(auth_session):
    return APIClient(BASE_URL, session=auth_session)


@pytest.fixture
def booking(api_client, authenticated_client, booking_data):
    # Create a temporary booking for tests that need an existing booking.
    response = api_client.post("/booking", booking_data["valid_booking"], timeout=10)

    assert response.status_code == 200, "Test booking was not created"
    booking_id = response.json().get("bookingid")
    assert booking_id, "Create booking response did not include bookingid"

    yield booking_id

    # Ensure the booking is cleaned up after tests
    cleanup_response = authenticated_client.delete(f"/booking/{booking_id}", timeout=10)
    assert cleanup_response.status_code in [201, 404, 405], (
        f"Unexpected cleanup response: {cleanup_response.status_code}"
    )
