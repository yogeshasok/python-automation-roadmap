import interface
import engine
import validators as validate
import storage as st
import config as cfg

def main() -> None:
    """Initializes app; loads data; evaluates menu choices; calls logic blocks."""
    contacts_data = st.load_contacts(cfg.DATA_FILE_PATH)
    while True:
        interface.display_menu()
        user_input = input(f"{cfg.CLR_BOLD}Enter your choice: {cfg.CLR_RESET}") 
        match user_input:
            case "1":
                contact = interface.prompt_contact_input()
                if contact['phone'] in contacts_data:
                    print(f"{cfg.CLR_WARN}Contact with phone {contact['phone']} already exists.{cfg.CLR_RESET}")
                elif engine.add_contact(contacts_data, contact['phone'], contact):
                    print(f"{cfg.CLR_SUCCESS}Contact added successfully!{cfg.CLR_RESET}")
                else:
                    print(f"{cfg.CLR_FAIL}Failed to add. Check phone format (+91XXXXXXXXXX) and email.{cfg.CLR_RESET}")
            case "2":
                query = input(f"{cfg.CLR_SUCCESS}Enter query to search: {cfg.CLR_RESET}")
                filtered_contact = engine.search_contacts(contacts_data, query)
                print(f"{cfg.CLR_SUCCESS}Search completed!{cfg.CLR_RESET}")
                interface.display_contact(filtered_contact)
            case "3":
                phone_update = interface.prompt_get_number()
                if validate.is_valid_phone(phone_update) and phone_update in contacts_data:
                    interface.display_contact(contacts_data, phone_update)
                    print(f"{cfg.CLR_SUCCESS} Enter contact details to update:{cfg.CLR_RESET}")
                    contact = interface.prompt_contact_input()
                    if engine.update_contact(contacts_data, phone_update, contact):
                        print(f"{cfg.CLR_SUCCESS}Contact updated successfully!{cfg.CLR_RESET}")
                        interface.display_contact(contacts_data)
                    else:
                        print(f"{cfg.CLR_FAIL}Failed to update contact.{cfg.CLR_RESET}")
                else:
                    print(f"{cfg.CLR_FAIL}Phone not found or invalid format.{cfg.CLR_RESET}")
            case "4":
                print(f"{cfg.CLR_BOLD} Deleting Contact {cfg.CLR_RESET}")
                phone_to_delete = interface.prompt_get_number()
                interface.display_contact(contacts_data, phone_to_delete)
                confirmation = input(f"{cfg.CLR_WARN} Are you sure to delete y/n? {cfg.CLR_RESET}")
                if confirmation.lower() in ["y", "yes"]:
                    if contacts_data := engine.delete_contact(contacts_data, phone_to_delete):
                        print(f"{cfg.CLR_SUCCESS}Contact deleted successfully!{cfg.CLR_RESET}")
                        interface.display_contact(contacts_data)
                    else:
                        print(f"{cfg.CLR_FAIL}Failed to delete. Phone not found or invalid.{cfg.CLR_RESET}")
                else:
                    print(f"{cfg.CLR_INFO}Deletion cancelled.{cfg.CLR_RESET}")
            case "5":
                sorted_contacts = engine.get_sorted_contacts(contacts_data)
                interface.display_contact(sorted_contacts)
            case "6":
                confirmation = input(f"{cfg.CLR_WARN}Are you sure you want to rotate backup? (y/n): {cfg.CLR_RESET}")
                if confirmation.lower() in ["y", "yes"]:
                    if st.rotate_backup():
                        print(f"{cfg.CLR_SUCCESS}Backup created successfully!{cfg.CLR_RESET}")
                    else:
                        print(f"{cfg.CLR_FAIL}Backup failed.{cfg.CLR_RESET}")
                else:
                    print(f"{cfg.CLR_INFO}Backup cancelled.{cfg.CLR_RESET}")
            case "0":
                break
            case _:
                print(f"{cfg.CLR_FAIL}Invalid choice. Please try again.{cfg.CLR_RESET}")
        wait = input("Press Enter to continue...")
        print("\033[2J\033[H") # Clear screen

if __name__ == "__main__":
    main()
