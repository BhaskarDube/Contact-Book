# -*- coding: utf-8 -*-
"""
Created on Sun May 12 17:15:03 2024

@author: bhask
"""

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if self.contacts:
            print("Contact List:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. Name: {contact.name}, Phone: {contact.phone_number}")
        else:
            print("Contact list is empty.")

    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                results.append(contact)
        return results

    def update_contact(self, index, new_contact):
        if index < len(self.contacts):
            self.contacts[index] = new_contact
            print("Contact updated successfully!")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if index < len(self.contacts):
            del self.contacts[index]
            print("Contact deleted successfully!")
        else:
            print("Invalid contact index.")

def main():
    contact_list = ContactList()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_list.add_contact(contact)
        elif choice == '2':
            contact_list.view_contacts()
        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            search_results = contact_list.search_contact(keyword)
            if search_results:
                print("Search Results:")
                for contact in search_results:
                    print(f"Name: {contact.name}, Phone: {contact.phone_number}")
            else:
                print("No matching contacts found.")
        elif choice == '4':
            index = int(input("Enter the index of the contact to update: "))
            if 0 <= index < len(contact_list.contacts):
                name = input("Enter name: ")
                phone_number = input("Enter phone number: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                new_contact = Contact(name, phone_number, email, address)
                contact_list.update_contact(index, new_contact)
            else:
                print("Invalid contact index.")
        elif choice == '5':
            index = int(input("Enter the index of the contact to delete: "))
            contact_list.delete_contact(index)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
