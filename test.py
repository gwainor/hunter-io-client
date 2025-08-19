from app.client import ApiError, Client
from app.endpoints import find_email, verify_email


def main():
    # Example usage. Fill in with appropriate information
    person = {
        "domain": "example.com",
        "first_name": "John",
        "last_name": "Doe"
    }

    client = Client()
    try:
        found_email = find_email(client, **person)
        verified_email = verify_email(client, found_email.email)
    except ApiError as error:
        if hasattr(error, 'error_data') and error.error_data:
            for err in error.error_data.errors:
                print(f"Error details: {err.details}")
                print(f"Error code: {err.code}")
                print(f"Error ID: {err.id}")
        else:
            print(f"API error occurred: {error}")
    else:
        print("Found email", found_email)
        print("Verified email", verified_email)


if __name__ == "__main__":
    main()
