contacts = []

def display_menu():
    print("Contact Management System")
    print("1. Add a new contact")
    print("2. View contacts")
    print("3. Search for a contact")
    print("4. Edit a contact")
    print("5. Delete a contact")
    print("6. Exit")

def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact():
    search_term = input("Enter the name or phone number to search: ")
    matching_contacts = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]
    if not matching_contacts:
        print("No matching contacts found.")
    else:
        print("Matching contacts:")
        for contact in matching_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def edit_contact():
    search_term = input("Enter the name or phone number of the contact to edit: ")
    matching_contacts = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]
    if not matching_contacts:
        print("No matching contacts found.")
    else:
        if len(matching_contacts) > 1:
            print("Multiple matching contacts found. Please be more specific.")
        else:
            contact = matching_contacts[0]
            print(f"Current details: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            name = input("Enter the new name (or leave blank to keep current): ") or contact['name']
            phone = input("Enter the new phone number (or leave blank to keep current): ") or contact['phone']
            email = input("Enter the new email address (or leave blank to keep current): ") or contact['email']
            contact['name'] = name
            contact['phone'] = phone
            contact['email'] = email
            print("Contact updated successfully!")

def delete_contact():
    search_term = input("Enter the name or phone number of the contact to delete: ")
    matching_contacts = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]
    if not matching_contacts:
        print("No matching contacts found.")
    else:
        if len(matching_contacts) > 1:
            print("Multiple matching contacts found. Please be more specific.")
        else:
            contact = matching_contacts[0]
            contacts.remove(contact)
            print("Contact deleted successfully!")

while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        edit_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
