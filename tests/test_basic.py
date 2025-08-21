from http import HTTPStatus

import pytest

from app.client import ApiError, Client
from app.endpoints import find_email, verify_email


def test_find_email_endpoint_success(client: Client, person_data: dict[str, str]) -> None:
    """Text for find_email endpoint success test.
    NOTE: Makes actual API call to find email using test api key.
    Returned data is dummy data
    """
    person = find_email(client, person_data["domain"], person_data["first_name"], person_data["last_name"])

    assert person is not None
    assert person.first_name == person_data["first_name"]
    assert person.last_name == person_data["last_name"]
    assert person.email == person_data["email"]


def test_find_email_endpoint_failure(fail_client: Client, person_data: dict[str, str]) -> None:
    with pytest.raises(ApiError) as exc_info:
        find_email(fail_client, person_data["domain"], person_data["first_name"], person_data["last_name"])
        error_data = exc_info.value.error_data
        assert error_data is not None
        assert error_data.errors[0].code == HTTPStatus.UNAUTHORIZED


def test_verify_email_endpoint_success(client: Client, person_data: dict[str, str]) -> None:
    """Text for verify_email endpoint success test.
    NOTE: Makes actual API call to verify email using test api key.
    Returned data is dummy data
    """
    person = verify_email(client, person_data["email"])
    assert person is not None
    assert person.email == person_data["email"]


def test_verify_email_endpoint_failure(fail_client: Client, person_data: dict[str, str]) -> None:
    with pytest.raises(ApiError) as exc_info:
        verify_email(fail_client, person_data["email"])
        error_data = exc_info.value.error_data
        assert error_data is not None
        assert error_data.errors[0].code == HTTPStatus.UNAUTHORIZED
