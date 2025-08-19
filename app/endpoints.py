from pydantic import EmailStr

from app.client import Client
from app.models import EmailFinderResponse, EmailVerifierResponse


def verify_email(client: Client, email: EmailStr) -> EmailVerifierResponse:
    response = client.get("/email-verifier", {"email": email})
    email_data = EmailVerifierResponse.from_response(response)
    return email_data


def find_email(client: Client, domain: str, first_name: str, last_name: str) -> EmailFinderResponse:
    response = client.get("/email-finder", {
        "domain": domain,
        "first_name": first_name,
        "last_name": last_name
    })
    email_data = EmailFinderResponse.from_response(response)
    return email_data
