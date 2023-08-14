class Contact:
    def __init__(self, name, address, phone_number, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nPhone Number: {self.phone_number}\nEmail: {self.email}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                new_name = input("Enter new name (press enter to skip): ")
                new_address = input("Enter new address (press enter to skip): ")
                new_phone_number = input("Enter new phone number (press enter to skip): ")
                new_email = input("Enter new email (press enter to skip): ")

                if new_name:
                    contact.name = new_name
                if new_address:
                    contact.address = new_address
                if new_phone_number:
                    contact.phone_number = new_phone_number
                if new_email:
                    contact.email = new_email

                print("Contact updated successfully.")
                return

        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return

        print("Contact not found.")

    def list_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(contact)
                print("-" * 20)


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. List Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter name: ")
            address = input("Enter address: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact = Contact(name, address, phone_number, email)
            contact_book.add_contact(contact)

        elif choice == "2":
            name = input("Enter name to update: ")
            contact_book.update_contact(name)

        elif choice == "3":
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)

        elif choice == "4":
            contact_book.list_contacts()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
