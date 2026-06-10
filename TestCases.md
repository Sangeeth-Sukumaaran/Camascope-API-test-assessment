# Test Case List
ID	Test Case	Type
TC-01	Generate auth token with valid credentials	Positive	
TC-02	Generate auth token with invalid credentials	Negative
TC-03	Create booking with valid data	
TC-04	Get booking by ID	Positive
TC-05	Get all booking IDs	Positive	
TC-06	Update booking	Positive	
TC-07	Partial update booking	Positive	
TC-08	Delete booking	Positive	
TC-09	Update booking without token	Negative	
TC-10	Delete booking without token	Negative	
TC-11	Invalid booking ID	Negative	
TC-12	Negative price	Boundary	
TC-13	Checkout before checkin	Business Rule	
TC-14	Invalid boolean type	Contract	
TC-15	XSS payload	Security	
TC-16	Invalid Content-Type	Negative	
TC-17	Token expiry	Security
TC-18	Rate limiting	Performance/Security	

---

## Automated Scenarios

The following scenarios were selected for automation:

ID	Test Case
TC-01	Generate auth token with valid credentials
TC-02	Generate auth token with invalid credentials
TC-03	Create booking with valid data
TC-04	Get booking by ID
TC-06	Update booking
TC-07	Partial update booking
TC-08	Delete booking
TC-09	Update booking without token
TC-11	Invalid booking ID
TC-12	Negative price
TC-13	Checkout before checkin
TC-14	Invalid boolean type
TC-15	XSS payload
TC-16	Invalid Content-Type

# Notes from Exploratory Testing

The following findings were identified during exploratory testing.

EF-01  DELETE returns 201 instead of 200/204
EF-02  Invalid login returns 200 instead of 401
EF-03  Missing resource returns 405 instead of 404
EF-04  Checkout date before checkin is accepted
EF-05  Negative total price is accepted
EF-06  Invalid input can return 500 instead of 400
EF-07  XSS-style input is accepted/stored
EF-08  Content-Type validation appears weak
EF-09  Token expiry behaviour is unclear
EF-10  No obvious rate limiting
EF-11  Boolean field type validation appears weak
EF-12  No clear length limits for name fields


## Assumptions

The following assumptions were made while designing the tests:

1. The public API is available and stable enough during test execution.
2. Test data created during automation can be deleted after the test.
3. The authentication token remains valid for the duration of the test run.
4. Performance and load testing are out of scope.
5. Full security testing is out of scope, but basic security-aware checks are included.
6. The API documentation does not define firstname and lastname length limits. For demonstration purposes, a minimum length of 1 and maximum length of 100 were treated as reasonable assumptions.
7. Some exploratory tests are marked as expected failures because they document current API behaviour rather than blocking the whole test run.
