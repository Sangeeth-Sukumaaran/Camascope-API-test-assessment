from jsonschema import Draft7Validator, FormatChecker


def validate_schema(response_data, schema):
    """Validate response data against a JSON schema and raise an assertion if it fails."""
    # Use Draft7Validator for JSON Schema validation and enable format checking for date strings.
    validator = Draft7Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(response_data), key=lambda error: error.path)

    if errors:
        error_messages = []
        for error in errors:
            location = ".".join(str(item) for item in error.path) or "root"
            # Build a friendly error message that shows the failing location in the response.
            error_messages.append(f"{location}: {error.message}")
        raise AssertionError("Schema validation failed: " + "; ".join(error_messages))
