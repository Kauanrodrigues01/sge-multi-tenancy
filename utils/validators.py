from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def verify_email(email):
    """Verify if the email is valid."""
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False
