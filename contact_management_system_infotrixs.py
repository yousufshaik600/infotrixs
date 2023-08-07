import json

def load_contacts_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts_to_file(contacts, filename):
    with open(filename, 'w') as file:
        json.dump(contacts, file)

def add_contact(contacts, name, phone, email):
    contact = {
        'phone': phone,
        'email': email
    }
    contacts[name] = contact
    print("Contact added successfully!")

def search_contact(contacts, name):
    if name in contacts:
        contact = contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
    else:
        print("Contact not found.")

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def update_contact(contacts, name, phone, email):
    if name in contacts:
        contacts[name]['phone'] = phone
        contacts[name]['email'] = email
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts_from_file('contacts.json')
    
    while True:
        print("\n1. Add contact")
        print("2. Search contact by name")
        print("3. Delete contact")
        print("4. Update contact information")
        print("5. View all contacts")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(contacts, name, phone, email)
            save_contacts_to_file(contacts, 'contacts.json')

        elif choice == '2':
            name = input("Enter name to search: ")
            search_contact(contacts, name)

        elif choice == '3':
            name = input("Enter name to delete: ")
            delete_contact(contacts, name)
            save_contacts_to_file(contacts, 'contacts.json')

        elif choice == '4':
            name = input("Enter name to update: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            update_contact(contacts, name, phone, email)
            save_contacts_to_file(contacts, 'contacts.json')

        elif choice == '5':
            print("\n--- All Contacts ---")
            for name, contact in contacts.items():
                print(f"Name: {name}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
            print("--------------------")

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
