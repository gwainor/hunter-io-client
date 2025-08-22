"""Endpoints."""
from pydantic import EmailStr

from app.client import Client
from app.models import EmailFinderResponse, EmailVerifierResponse


def verify_email(client: Client, email: EmailStr) -> EmailVerifierResponse:
    """Verify an email address."""
    response = client.get('/email-verifier', {'email': email})

    return EmailVerifierResponse.from_response(response)


def find_email(client: Client, domain: str, first_name: str, last_name: str) -> EmailFinderResponse:
    """Find an email address by domain, first name, and last name."""
    response = client.get('/email-finder', {
        'domain': domain,
        'first_name': first_name,
        'last_name': last_name,
    })

    return EmailFinderResponse.from_response(response)
