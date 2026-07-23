from datetime import date
import validators as valid
import config as cfg
import storage as store

def add_contact(contacts: dict, phone: str, details: dict) -> bool:
    """Validates fields, inserts new record into contacts dict, saves to file; returns True on success."""
    if not valid.is_valid_phone(phone) or not valid.is_valid_email(details["email"]):
        return False
    if phone in contacts:
        return False
    contacts[phone] = {
        "first_name": details["first_name"],
        "last_name": details["last_name"],
        "email": details["email"],
        "metadata": {
            "created_at": date.today().isoformat(),
            "updated_at": date.today().isoformat()
        }
    }
    return store.save_contacts(contacts=contacts)


def update_contact(contacts: dict, phone: str, updated_details: dict) -> dict | None:
    """Validates fields, updates existing contact in-place, saves to file; returns updated dict or None on failure."""
    if not valid.is_valid_phone(phone) or not valid.is_valid_email(updated_details["email"]):
        return None
    contacts[phone] = {
        "first_name": updated_details['first_name'],
        "last_name": updated_details['last_name'],
        "email": updated_details['email'],
        "metadata": {
            "created_at": contacts[phone]['metadata']['created_at'],
            "updated_at": date.today().isoformat()
        }
    }
    return contacts if store.save_contacts(contacts=contacts) else None


def delete_contact(contacts: dict, phone: str) -> dict | None:
    """Removes contact keyed by phone; saves to file; returns updated dict or None on failure."""
    if not valid.is_valid_phone(phone) or phone not in contacts:
        return None
    del contacts[phone]
    return contacts if store.save_contacts(contacts=contacts) else None


def get_sorted_contacts(contacts: dict, reverse: bool = False) -> dict:
    """Returns a new dict sorted alphabetically by first_name; supports reverse flag."""
    return dict(sorted(contacts.items(), key=lambda x: x[1]['first_name'], reverse=reverse))


def search_contacts(contacts: dict, query: str) -> dict:
    """Filters dict for partial matches inside names, email, or phone; case-insensitive."""
    q = query.lower()
    return {
        phone: details for phone, details in contacts.items()
        if q in details['first_name'].lower()
        or q in details['last_name'].lower()
        or q in details['email'].lower()
        or q in phone
    }

