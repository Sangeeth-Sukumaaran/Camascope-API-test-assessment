import pytest

from schemas.booking_schema import CREATE_BOOKING_RESPONSE_SCHEMA
from utils.schema_validator import validate_schema


def cleanup_if_created(response, authenticated_client):
    # If a booking was created despite invalid input, remove it to keep the test environment clean.
    try:
        response_data = response.json()
        booking_id = response_data.get("bookingid")
        if booking_id:
            authenticated_client.delete(f"/booking/{booking_id}", timeout=10)
    except Exception:
        pass


@pytest.mark.negative
@pytest.mark.exploratory
@pytest.mark.xfail(reason="Known issue: API currently accepts negative totalprice", strict=False)
def test_negative_price_should_be_rejected(api_client, authenticated_client, booking_data):
    # Verify negative pricing is rejected. This is exploratory because the API may not enforce it.
    response = api_client.post("/booking", booking_data["negative_price_booking"], timeout=10)
    cleanup_if_created(response, authenticated_client)
    assert response.status_code == 400


@pytest.mark.negative
@pytest.mark.exploratory
@pytest.mark.xfail(reason="Known issue: API may accept non-boolean depositpaid values", strict=False)
def test_invalid_boolean_type_should_be_rejected(api_client, authenticated_client, booking_data):
    response = api_client.post("/booking", booking_data["invalid_boolean_booking"], timeout=10)
    cleanup_if_created(response, authenticated_client)
    assert response.status_code == 400


@pytest.mark.negative
@pytest.mark.exploratory
@pytest.mark.xfail(reason="Known issue: API does not validate checkout date is after checkin date", strict=False)
def test_checkout_before_checkin_should_be_rejected(api_client, authenticated_client, booking_data):
    response = api_client.post("/booking", booking_data["invalid_date_logic_booking"], timeout=10)
    cleanup_if_created(response, authenticated_client)
    assert response.status_code == 400


@pytest.mark.negative
@pytest.mark.exploratory
@pytest.mark.xfail(reason="Known issue: API stores script-like input in string fields", strict=False)
def test_xss_payload_should_not_be_stored(api_client, authenticated_client, booking_data):
    response = api_client.post("/booking", booking_data["xss_booking"], timeout=10)
    cleanup_if_created(response, authenticated_client)
    assert response.status_code == 400


@pytest.mark.negative
@pytest.mark.exploratory
@pytest.mark.xfail(reason="Known issue: API does not appear to enforce length limits", strict=False)
def test_long_firstname_should_be_rejected(api_client, authenticated_client, booking_data):
    response = api_client.post("/booking", booking_data["long_name_booking"], timeout=10)
    cleanup_if_created(response, authenticated_client)
    assert response.status_code == 400


@pytest.mark.negative
@pytest.mark.exploratory
@pytest.mark.xfail(reason="Known issue: API may return 500 instead of 400 for bad input", strict=False)
def test_malformed_input_should_return_400_not_500(api_client, booking_data):
    # Confirm malformed types are handled as client errors, not server errors.
    response = api_client.post("/booking", booking_data["malformed_type_booking"], timeout=10)
    assert response.status_code == 400


@pytest.mark.negative
@pytest.mark.exploratory
@pytest.mark.xfail(reason="Known issue: API may not enforce Content-Type validation", strict=False)
def test_invalid_content_type_should_be_rejected(api_client):
    payload = '{"firstname":"Text","lastname":"Plain","totalprice":100,"depositpaid":true,"bookingdates":{"checkin":"2026-08-01","checkout":"2026-08-05"},"additionalneeds":"Breakfast"}'

    response = api_client.session.post(
        f"{api_client.base_url}/booking",
        data=payload,
        headers={"Content-Type": "text/plain", "Accept": "application/json"},
        timeout=10
    )

    assert response.status_code == 415


@pytest.mark.negative
@pytest.mark.exploratory
@pytest.mark.xfail(reason="Known issue: API may return 405 instead of 404 for missing resource", strict=False)
def test_update_non_existing_booking_should_return_404(authenticated_client, booking_data):
    response = authenticated_client.put(
        "/booking/999999999",
        booking_data["updated_booking"],
        timeout=10
    )
    assert response.status_code == 404


@pytest.mark.negative
@pytest.mark.exploratory
@pytest.mark.xfail(reason="Known issue: API may return 405 instead of 404 for missing resource", strict=False)
def test_delete_non_existing_booking_should_return_404(authenticated_client):
    response = authenticated_client.delete("/booking/999999999", timeout=10)
    assert response.status_code == 404


@pytest.mark.negative
@pytest.mark.exploratory
@pytest.mark.xfail(reason="Known issue examples: negative price or invalid types may be accepted and violate stricter contract", strict=False)
def test_negative_price_response_should_not_match_strict_contract(api_client, authenticated_client, booking_data):
    response = api_client.post("/booking", booking_data["negative_price_booking"], timeout=10)
    cleanup_if_created(response, authenticated_client)

    assert response.status_code == 200
    validate_schema(response.json(), CREATE_BOOKING_RESPONSE_SCHEMA)
