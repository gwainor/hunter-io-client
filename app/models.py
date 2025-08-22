"""Models."""
from typing import Type, TypeVar

import httpx
from pydantic import BaseModel as PydanticBaseModel
from pydantic import EmailStr

TModel = TypeVar('TModel', bound='BaseModel')


class BaseModel(PydanticBaseModel):
    """Base Model for all."""

    @classmethod
    def from_response(cls: Type[TModel], response: httpx.Response) -> TModel:
        """From response, create model instance."""
        json = response.json()
        if response.is_error:
            return cls(**json)

        return cls(**json['data'])


class ErrorResponseItem(BaseModel):
    """Error response item.

    The structure is taken from hunter.io error responses.
    """

    id: str
    code: int
    details: str


class ErrorResponse(BaseModel):
    """Error response model."""

    errors: list[ErrorResponseItem]


class HunterIoSource(BaseModel):
    """Hunter IO Source model.

    This source is being repeated in the responses
    """

    domain: str
    uri: str
    extracted_on: str
    last_seen_on: str
    still_on_page: bool


class EmailVerifierResponse(BaseModel):
    """Email Verifier response model."""

    status: str
    score: int
    email: EmailStr
    regexp: bool
    gibberish: bool
    disposable: bool
    webmail: bool
    mx_records: bool
    smtp_server: bool
    smtp_check: bool
    accept_all: bool
    block: bool
    sources: list[HunterIoSource]


class EmailFinderResponse(BaseModel):
    """Email Finder response model."""

    first_name: str
    last_name: str
    email: EmailStr
    score: int
    domain: str
    accept_all: bool
    position: str | None
    twitter: str | None
    linkedin_url: str | None
    phone_number: str | None
    company: str | None
    sources: list[HunterIoSource]
