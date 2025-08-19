from dataclasses import dataclass
from typing import Any

import httpx

from app.config import settings
from app.models import ErrorResponse


class ApiError(Exception):
    """Base API error raised when API returns an error response."""

    error_data: ErrorResponse | None = None

    def __init__(self, message: str, error_data: ErrorResponse | None = None):
        super().__init__(message)
        self.error_data = error_data


@dataclass(frozen=True, slots=True)
class Client:
    # Timeout in seconds
    timeout: float = 10.0

    def get(self, path: str, query_params: dict[str, Any] | None = None) -> httpx.Response:
        with self._client() as client:
            query_parameters = httpx.QueryParams(**query_params) if query_params else None
            response = client.get(path, params=query_parameters)

        if response.is_error:
            error_response = ErrorResponse.from_response(response)
            raise ApiError(
                "API request failed with status code "
                f"{response.status_code}: {response.text}",
                error_data=error_response
            )

        return response

    def _client(self) -> httpx.Client:
        return httpx.Client(
            base_url=settings.service_url,
            timeout=self.timeout,
            headers={"X-API-KEY": settings.api_key}
        )
