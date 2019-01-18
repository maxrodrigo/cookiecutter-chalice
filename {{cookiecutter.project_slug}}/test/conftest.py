# -*- coding: utf-8 -*-

"""Test configuration for {{ cookiecutter.project_name }}."""

import pytest

from chalice.config import Config
from chalice.local import LocalGateway

from app import app


class TestClient(object):
    """Simulates requests to the local gateway

    Keyword Arguments:
        headers (dict): Default headers to set on every request (default: ``None``).
    """

    def __init__(self, headers=None):
        self._default_headers = headers

    def request(self, method="GET", path="/", headers=None, body=None):
        """Simulates a request to the app local gateway.

        Performs a request against the application.

        :path: (str) The URL path to request (default: '/').
        :method: (str) An HTTP method to use in the request (default: GET).
        :headers: (dict) Additional headers to include in the request (default: ``None``).
        :body: (str) A string to send as the body of the request (default: ``None``).
        :returns: (dict) The result of the request.

        """
        if not path.startswith("/"):
            raise ValueError("path must start with '/'")

        valid_methods = ["GET", "HEAD", "POST", "PUT", "DELETE"]
        if method not in valid_methods:
            raise ValueError(f"method must be one of: {valid_methods}")

        body = body or ""
        headers = headers or {}

        gateway = LocalGateway(app, Config())
        response = gateway.handle_request(method, path, headers, body)
        return response

    def get(self, path="/", **kwargs):
        """Simulates a GET request to the local gateway"""
        return self.request("GET", path, **kwargs)

    def head(self, path="/", **kwargs):
        """Simulates a HEAD request to the local gateway"""
        return self.request("HEAD", path, **kwargs)

    def post(self, path="/", **kwargs):
        """Simulates a POST request to the local gateway"""
        return self.request("POST", path, **kwargs)

    def put(self, path="/", **kwargs):
        """Simulates a PUT request to the local gateway"""
        return self.request("PUT", path, **kwargs)

    def delete(self, path="/", **kwargs):
        """Simulates a DELETE request to the local gateway"""
        return self.request("DELETE", path, **kwargs)


@pytest.fixture(scope="module")
def client():
    return TestClient()
