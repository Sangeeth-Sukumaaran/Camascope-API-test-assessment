# Schema definition for the auth response returned by the /auth endpoint.
# This ensures the response contains a token string that can be used for authenticated requests.
AUTH_SCHEMA = {
    "type": "object",
    "properties": {
        "token": {"type": "string"}
    },
    "required": ["token"]
}
