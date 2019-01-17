# -*- coding: utf-8 -*-

"""Tests for {{ cookiecutter.project_slug }}."""


def test_response(client):
    resp = client.handle_request(method="GET", path="/", headers={}, body="")
    __import__("pprint").pprint(resp)
    assert resp["statusCode"] == 403
