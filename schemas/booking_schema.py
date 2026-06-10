# This schema defines the expected structure for a booking object.
# It is used to validate booking responses and ensure the API returns the correct fields and types.
BOOKING_SCHEMA = {
    "type": "object",
    "properties": {
        "firstname": {
            "type": "string",
            "minLength": 1,
            "maxLength": 100
        },
        "lastname": {
            "type": "string",
            "minLength": 1,
            "maxLength": 100
        },
        "totalprice": {
            "type": "integer",
            "minimum": 0
        },
        "depositpaid": {"type": "boolean"},
        "bookingdates": {
            "type": "object",
            "properties": {
                "checkin": {
                    "type": "string",
                    "format": "date"
                },
                "checkout": {
                    "type": "string",
                    "format": "date"
                }
            },
            "required": ["checkin", "checkout"]
        },
        "additionalneeds": {
            "type": "string",
            "maxLength": 500
        }
    },
    "required": [
        "firstname",
        "lastname",
        "totalprice",
        "depositpaid",
        "bookingdates"
    ]
}

# Response schema for creating a booking. The API should return a bookingid plus the saved booking details.
CREATE_BOOKING_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "bookingid": {"type": "integer"},
        "booking": BOOKING_SCHEMA
    },
    "required": ["bookingid", "booking"]
}

# Generic error schema for any API responses that return a structured error payload.
ERROR_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "reason": {"type": "string"},
        "message": {"type": "string"},
        "error": {"type": "string"}
    }
}
