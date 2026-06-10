import requests


class APIClient:
    """Simple HTTP client wrapper for the API under test."""

    def __init__(self, base_url, session=None):
        self.base_url = base_url
        # Reuse a requests.Session for connection pooling and shared headers.
        self.session = session or requests.Session()

    def get(self, endpoint, **kwargs):
        # Use the underlying session to perform GET requests against the base URL.
        return self.session.get(f"{self.base_url}{endpoint}", **kwargs)

    def post(self, endpoint, payload=None, **kwargs):
        # Send JSON as the request body for POST operations.
        return self.session.post(f"{self.base_url}{endpoint}", json=payload, **kwargs)

    def put(self, endpoint, payload=None, **kwargs):
        # Send JSON as the request body for PUT operations.
        return self.session.put(f"{self.base_url}{endpoint}", json=payload, **kwargs)

    def patch(self, endpoint, payload=None, **kwargs):
        # Send JSON as the request body for PATCH operations.
        return self.session.patch(f"{self.base_url}{endpoint}", json=payload, **kwargs)

    def delete(self, endpoint, **kwargs):
        # Delete a resource at the given endpoint.
        return self.session.delete(f"{self.base_url}{endpoint}", **kwargs)
