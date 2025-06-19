import json
import os

# Define the class
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def display(self):
        print(f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}")

contacts = []

# Load contacts from file at the beginning
def load_contacts():
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r") as f:
            data = json.load(f)
            for item in data:
                contact = Contact(item["name"], item["phone"], item["email"])
                contacts.append(contact)

# Save to file
def save_contacts():
    with open("contacts.json", "w") as f:
        data = [{"name": c.name, "phone": c.phone, "email": c.email} for c in contacts]
        json.dump(data, f, indent=4)

# Add contact
def add_contact():
    print("\nAdd New Contact")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter your email: ")
    contact = Contact(name, phone, email)
    contacts.append(contact)
    save_contacts()
    print("Contact added successfully!")

# View all contacts
def view_contacts():
    if not contacts:
        print("No contacts to show.")
    else:
        print("\nContact List:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. ", end="")
            contact.display()

# Search contact
def search_contact():
    name_to_find = input("Enter name to search: ")
    found = False
    for contact in contacts:
        if contact.name.lower() == name_to_find.lower():
            contact.display()
            found = True
            break
    if not found:
        print("Contact not found.")

# Delete contact
def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ")
    found = False
    for contact in contacts:
        if contact.name.lower() == name_to_delete.lower():
            contacts.remove(contact)
            save_contacts()
            print(f"Contact '{contact.name}' deleted successfully.")
            found = True
            break
    if not found:
        print("Contact not found.")

# Update contact
def update_contact():
    name_to_update = input("Enter the name of the contact to update: ")
    found = False
    for contact in contacts:
        if contact.name.lower() == name_to_update.lower():
            print("What would you like to update?")
            print("1. Name")
            print("2. Phone")
            print("3. Email")
            option = input("Choose an option (1-3): ")
            if option == "1":
                contact.name = input("Enter new name: ")
            elif option == "2":
                contact.phone = input("Enter new phone number: ")
            elif option == "3":
                contact.email = input("Enter new email: ")
            else:
                print("Invalid option.")
                return
            save_contacts()
            print("Contact updated successfully.")
            found = True
            break
    if not found:
        print("Contact not found.")

# Load existing contacts on start
load_contacts()

# Main menu loop
while True:
    print("\n=== Contact Book ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        update_contact()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
