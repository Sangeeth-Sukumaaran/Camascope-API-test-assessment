# Test Cases

| Title | Expected Result | Actual Result |
|---|---|---|
| Generate token with valid credentials | Token is returned successfully | |
| Generate token with invalid credentials | Token is not returned and authentication should fail | |
| Create booking with valid data | Booking is created and booking ID is returned | |
| Get booking by valid ID | Booking details are returned | |
| Update booking with valid token | Booking is updated successfully | |
| Partially update booking with valid token | Selected fields are updated successfully | |
| Delete booking with valid token | Booking is deleted successfully | |
| Get booking using invalid ID | Error response is returned | |
| Update booking without token | Access is denied | |
| Create booking with missing required field | API rejects or handles invalid request safely | |
| Create booking with invalid date format | API rejects or handles invalid request safely | |
| Create booking with checkout before checkin | API rejects invalid booking date logic | |
| Create booking with negative price | API rejects negative total price | |
| Create booking with invalid boolean type | API rejects non-boolean depositpaid value | |
| Create booking with malformed field types | API returns 400 Bad Request, not 500 Internal Server Error | |
| Create booking with text/plain Content-Type | API rejects unsupported content type | |
| Create booking with XSS payload | API rejects or sanitises unsafe script input | |
| Create booking with long firstname | API rejects or safely handles excessive length | |
| Update non-existing booking | API returns 404 Not Found | |
| Delete non-existing booking | API returns 404 Not Found | |
