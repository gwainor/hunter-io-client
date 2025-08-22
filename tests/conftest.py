"""Configuration and setup for the tests."""
from http import HTTPStatus
from typing import Generator

import httpx
import pytest

from app.client import Client
from app.config import settings


@pytest.fixture(scope='module')
def client() -> Generator[Client, None, None]:
    """Client fixture."""
    instance = Client(test_mode=True)
    yield instance


@pytest.fixture()
def fail_client() -> Generator[Client, None, None]:
    """Fail client.

    This client always fails with unauthorized error.
    """
    instance = Client(test_mode=True)
    error_json = {'errors': [{'id': 'unauthorized', 'code': HTTPStatus.UNAUTHORIZED, 'details': 'Unauthorized'}]}
    instance._client = httpx.Client(  # noqa: WPS437 The instance MUST be changed for tests
        base_url=settings.service_url,
        timeout=instance.timeout,
        transport=httpx.MockTransport(
            lambda request: httpx.Response(
                HTTPStatus.UNAUTHORIZED, json=error_json,
            ),
        ),
    )

    yield instance


@pytest.fixture()
def person_data() -> dict[str, str]:
    """Person data for the tests.

    Hunter.io provides a test API key that can be used for testing purposes.
    It always returns same dummy data when called with the test api key.
    """
    return {
        'domain': 'piedpiper.com',
        'first_name': 'Richard',
        'last_name': 'Hendricks',
        'email': 'richard@piedpiper.com',
    }
