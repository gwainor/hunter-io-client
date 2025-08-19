from typing import Type, TypeVar

import httpx
from pydantic import BaseModel as PydanticBaseModel
from pydantic import EmailStr

TModel = TypeVar('TModel', bound='BaseModel')


class BaseModel(PydanticBaseModel):
    @classmethod
    def from_response(cls: Type[TModel], response: httpx.Response) -> TModel:
        json = response.json()
        if response.is_error:
            return cls(**json)
        else:
            return cls(**json["data"])


class ErrorResponseItem(BaseModel):
    id: str
    code: int
    details: str


class ErrorResponse(BaseModel):
    errors: list[ErrorResponseItem]


class HunterIoSource(BaseModel):
    domain: str
    uri: str
    extracted_on: str
    last_seen_on: str
    still_on_page: bool


class EmailVerifierResponse(BaseModel):
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
