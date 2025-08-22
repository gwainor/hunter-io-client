"""Client module.

A thin wrapper around the HTTPX client for making API requests.
"""
from dataclasses import dataclass
from typing import Any

import httpx

from app.config import settings
from app.models import ErrorResponse


class ApiError(Exception):
    """Base API error raised when API returns an error response."""

    error_data: ErrorResponse | None = None

    def __init__(self, message: str, error_data: ErrorResponse | None = None):
        """Initialize ApiError with a message and optional error data."""
        super().__init__(message)
        self.error_data = error_data


@dataclass(slots=True)
class Client:
    """Client for making API requests."""

    # Timeout in seconds
    timeout: float = 10.0
    test_mode: bool = False
    _client: httpx.Client | None = None

    def get(self, path: str, query_params: dict[str, Any] | None = None) -> httpx.Response:
        """Make a GET request to the API."""
        query_parameters = httpx.QueryParams(**query_params) if query_params else None
        response = self.request.get(path, params=query_parameters)

        if response.is_error:
            error_response = ErrorResponse.from_response(response)
            error_message = 'API reqiest failed with status code {code}: {details}'.format(
                code=response.status_code,
                details=response.text if response.text else 'No details provided',
            )

            raise ApiError(
                error_message,
                error_data=error_response,
            )

        return response

    @property
    def request(self) -> httpx.Client:
        """Get the HTTPX client for making API requests.

        Lazily create the HTTPX client instance.
        """
        if self._client is None:
            api_key = 'test-api-key' if self.test_mode else settings.api_key

            self._client = httpx.Client(
                base_url=settings.service_url,
                timeout=self.timeout,
                headers={'X-API-KEY': api_key},
            )

        return self._client
