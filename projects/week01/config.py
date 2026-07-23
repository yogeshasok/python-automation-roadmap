import os

# --- FILE PATHS ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE_PATH = os.path.join(BASE_DIR,"data", "contacts.json")
BACKUP_FILE_PATH = os.path.join(BASE_DIR,"data", "contacts_backup.json")

# --- APP SETTINGS ---
APP_NAME = "NEXUS CONTACT ARCHIVE"
VERSION = "2.1.0"

# --- INTERFACE COLORS (ANSI Escape Codes) ---
# Use these constants in print statements to style your text
CLR_HEADER = "\033[95m"  # Purple
CLR_INFO = "\033[94m"  # Blue
CLR_SUCCESS = "\033[92m"  # Green
CLR_WARN = "\033[93m"  # Yellow
CLR_FAIL = "\033[91m"  # Red
CLR_RESET = "\033[0m"  # Reset formatting
CLR_BOLD = "\033[1m"  # Bold

# --- DATA VALIDATION RULES ---
MAX_NAME_LENGTH = 50
# Matches ONLY: +919876543210
PHONE_REGEX = r"^\+91[6-9]\d{9}$"  # Matches Indian mobile numbers only (+91XXXXXXXXXX)
EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

