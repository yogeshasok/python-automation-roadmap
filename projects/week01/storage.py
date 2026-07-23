import config as cfg
import json

def load_contacts(filepath: str) -> dict:
    """Reads JSON file; handles FileNotFoundError/JSONDecodeError; returns dict."""
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}



def save_contacts(contacts: dict) -> bool:
    """Writes contacts dict to DATA_FILE_PATH as JSON; returns True on success."""
    try:
        with open(cfg.DATA_FILE_PATH, "w") as file:
            json.dump(contacts, file, indent=4)
        return True
    except Exception:
        return False

def rotate_backup() -> bool:
    """Backs up current contacts.json to BACKUP_FILE_PATH; returns True on success."""
    json_str = json.dumps(load_contacts(cfg.DATA_FILE_PATH), indent=4)
    try:
        with open(cfg.BACKUP_FILE_PATH, "w") as file:
            file.write(json_str)
        return True
    except Exception:
        return False