# -*- coding: utf-8 -*-

"""Tests for {{ cookiecutter.project_slug }}."""

import json


def test_response(client):
    resp = client.handle_request(method="GET", path="/", headers={}, body="")
    assert resp["statusCode"] == 200
    assert json.loads(resp["body"]) == {"hello": "world"}
