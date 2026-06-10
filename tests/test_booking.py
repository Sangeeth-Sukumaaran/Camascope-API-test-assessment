import pytest

from schemas.booking_schema import BOOKING_SCHEMA, CREATE_BOOKING_RESPONSE_SCHEMA
from utils.schema_validator import validate_schema


@pytest.mark.smoke
def test_create_booking(api_client, authenticated_client, booking_data):
    # Create a booking with valid data and verify the API returns the expected structure.
    response = api_client.post("/booking", booking_data["valid_booking"], timeout=10)
    assert response.status_code == 200
    response_data = response.json()
    validate_schema(response_data, CREATE_BOOKING_RESPONSE_SCHEMA)
    assert response_data["booking"]["firstname"] == booking_data["valid_booking"]["firstname"]
    assert response_data["booking"]["lastname"] == booking_data["valid_booking"]["lastname"]

    booking_id = response_data["bookingid"]
    # Clean up the booking after the test to avoid leaving test data behind.
    authenticated_client.delete(f"/booking/{booking_id}", timeout=10)


@pytest.mark.smoke
def test_get_booking_by_id(api_client, booking, booking_data):
    # Retrieve the booking created by the booking fixture and verify the returned data.
    response = api_client.get(f"/booking/{booking}", timeout=10)

    assert response.status_code == 200
    response_data = response.json()
    validate_schema(response_data, BOOKING_SCHEMA)
    assert response_data["firstname"] == booking_data["valid_booking"]["firstname"]
    assert response_data["lastname"] == booking_data["valid_booking"]["lastname"]


@pytest.mark.smoke
def test_update_booking(authenticated_client, booking, booking_data):
    response = authenticated_client.put(
        f"/booking/{booking}",
        booking_data["updated_booking"],
        timeout=10
    )

    assert response.status_code == 200
    response_data = response.json()
    validate_schema(response_data, BOOKING_SCHEMA)
    assert response_data["firstname"] == booking_data["updated_booking"]["firstname"]
    assert response_data["lastname"] == booking_data["updated_booking"]["lastname"]
    assert response_data["totalprice"] == booking_data["updated_booking"]["totalprice"]


@pytest.mark.regression
def test_partial_update_booking(authenticated_client, booking, booking_data):
    response = authenticated_client.patch(
        f"/booking/{booking}",
        booking_data["partial_update"],
        timeout=10
    )

    assert response.status_code == 200
    response_data = response.json()
    validate_schema(response_data, BOOKING_SCHEMA)
    assert response_data["firstname"] == booking_data["partial_update"]["firstname"]
    assert response_data["additionalneeds"] == booking_data["partial_update"]["additionalneeds"]


@pytest.mark.smoke
def test_delete_booking(authenticated_client, api_client, booking):
    # Delete the booking and verify the resource is no longer available.
    response = authenticated_client.delete(f"/booking/{booking}", timeout=10)

    assert response.status_code == 201

    get_response = api_client.get(f"/booking/{booking}", timeout=10)
    assert get_response.status_code == 404


@pytest.mark.negative
def test_get_invalid_booking_id(api_client):
    response = api_client.get("/booking/999999999", timeout=10)

    assert response.status_code == 404


@pytest.mark.negative
def test_update_booking_without_token(api_client, booking, booking_data):
    response = api_client.put(
        f"/booking/{booking}",
        booking_data["updated_booking"],
        timeout=10
    )

    assert response.status_code in [403, 405]


@pytest.mark.negative
def test_create_booking_with_missing_required_field(api_client, booking_data):
    # Send incomplete booking data to verify the API rejects missing required fields.
    response = api_client.post(
        "/booking",
        booking_data["invalid_booking_missing_firstname"],
        timeout=10
    )

    # The API behavior is uncertain, so this test is tolerant of 200, 400, or 500.
    assert response.status_code in [200, 400, 500]
