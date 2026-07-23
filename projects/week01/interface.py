import os
import config as cfg
import storage

def display_menu() -> None:
    """Prints a styled, decorated CLI menu without using parameters."""
    # Clears terminal for a clean workspace
    os.system("cls" if os.name == "nt" else "clear")

    # Fetch total contacts directly from storage to keep signature parameter-free
    current_data = storage.load_contacts(cfg.DATA_FILE_PATH)
    total_contacts = len(current_data)

    # App Branding Header Block
    print(f"{cfg.CLR_HEADER}╔══════════════════════════════════════════════════════╗{cfg.CLR_RESET}")
    print(
        f"{cfg.CLR_HEADER}║   🚀 {cfg.CLR_BOLD}{cfg.APP_NAME:<38}{cfg.CLR_RESET}{cfg.CLR_HEADER} v{cfg.VERSION}   ║{cfg.CLR_RESET}"
    )
    print(f"{cfg.CLR_HEADER}╚══════════════════════════════════════════════════════╝{cfg.CLR_RESET}")

    # Active Database Metrics
    print(f" 📂 Data File: {cfg.CLR_INFO}{cfg.DATA_FILE_PATH}{cfg.CLR_RESET}")
    print(f" 📇 Database State: {cfg.CLR_SUCCESS}{total_contacts} Active Record(s){cfg.CLR_RESET}")
    print(f"─" * 56)

    # Core Operations Options Grid
    print(f" [{cfg.CLR_BOLD}1{cfg.CLR_RESET}] ➕ Create New Contact")
    print(f" [{cfg.CLR_BOLD}2{cfg.CLR_RESET}] 🔍 Search/Filter Directory")
    print(f" [{cfg.CLR_BOLD}3{cfg.CLR_RESET}] ✏️  Modify Field Entry")
    print(f" [{cfg.CLR_BOLD}4{cfg.CLR_RESET}] 🗑️  Delete Existing Entry")
    print(f" [{cfg.CLR_BOLD}5{cfg.CLR_RESET}] 📋 List Alphabetical Index (Sort)")

    # System Utilities Section Divider
    print(f"\n {cfg.CLR_INFO}🛠️  SYSTEM UTILITIES:{cfg.CLR_RESET}")
    print(f" [{cfg.CLR_BOLD}6{cfg.CLR_RESET}] 💾 Force Backup Rotation")
    print(f" [{cfg.CLR_BOLD}0{cfg.CLR_RESET}] ❌ Secure Safe & Exit")
    print(f"─" * 56)

    


def prompt_contact_input(defaults: dict = None) -> dict:
    """Prompts for name, phone, email; shows defaults if updating; returns dict."""
    contact = {}
    contact['first_name'] = input(f"{cfg.CLR_BOLD}Enter first name: {cfg.CLR_RESET}")
    contact['last_name'] = input(f"{cfg.CLR_BOLD}Enter last name: {cfg.CLR_RESET}")
    contact['phone'] = input(f"{cfg.CLR_BOLD}Enter phone: {cfg.CLR_RESET}")
    contact['email'] = input(f"{cfg.CLR_BOLD}Enter email: {cfg.CLR_RESET}")
    
    return contact

def prompt_get_number() -> str:
    """Prompts for phone number; returns the entered string."""
    return input(f"{cfg.CLR_BOLD}Enter phone number: {cfg.CLR_RESET}")

def display_contact(contacts: dict, query: str = None) -> None:
    """Displays contacts in a formatted table; filters by phone query if provided."""
    if query is not None:
        filtered_contacts = {
            phone: details for phone, details in contacts.items() if query in phone
        }
    else:
        filtered_contacts = contacts
    if len(filtered_contacts) == 0:
        print(f"{cfg.CLR_FAIL}No contacts found.{cfg.CLR_RESET}")
        return
    print(f"{cfg.CLR_HEADER}╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{cfg.CLR_RESET}")
    print(f"{cfg.CLR_HEADER}║   First Name                | Last Name                | Phone                | Email                           ║{cfg.CLR_RESET}")
    print(f"{cfg.CLR_HEADER}╠═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣{cfg.CLR_RESET}")
    for phone, details in filtered_contacts.items():
        print(f"{cfg.CLR_INFO}║   {details['first_name']:<26}| {details['last_name']:<25}| {phone:<21}| {details['email']:<32}║{cfg.CLR_RESET}")
    print(f"{cfg.CLR_INFO}╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{cfg.CLR_RESET}")

