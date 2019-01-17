# -*- coding: utf-8 -*-

"""Test configuration for {{ cookiecutter.project_name }}."""

import pytest

from chalice.config import Config
from chalice.local import LocalGateway

from app import app


@pytest.fixture(scope="module")
def client():
    return LocalGateway(app, Config())
