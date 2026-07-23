import re
import config as cfg


def is_valid_phone(phone: str) -> bool:
    """Validates phone against configured regex; returns boolean."""
    return bool(re.match(cfg.PHONE_REGEX, phone))

def is_valid_email(email: str) -> bool:
    """Validates email structure; returns boolean."""
    return bool(re.match(cfg.EMAIL_REGEX, email))
