import json

# Define the contact book as a dictionary
contact_book = {}

# Function to add a new contact
def add_contact(name, phone):
    contact_book[name] = phone
    print(f"Contact {name} added.")

# Function to view all contacts
def view_contacts():
    if not contact_book:
        print("No contacts found.")
    else:
        for name, phone in contact_book.items():
            print(f"Name: {name}, Phone: {phone}")

# Function to search for a contact
def search_contact(name):
    if name in contact_book:
        print(f"Name: {name}, Phone: {contact_book[name]}")
    else:
        print(f"Contact {name} not found.")

# Function to remove a contact
def remove_contact(name):
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} removed.")
    else:
        print(f"Contact {name} not found.")

# Function to save contacts to a file
def save_contacts(filename):
    with open(filename, 'w') as file:
        json.dump(contact_book, file)
    print("Contacts saved.")

# Function to load contacts from a file
def load_contacts(filename):
    global contact_book
    try:
        with open(filename, 'r') as file:
            contact_book = json.load(file)
        print("Contacts loaded.")
    except FileNotFoundError:
        print("No saved contacts found.")

# Main function to display the menu and handle user input
def main():
    while True:
        print("\nContact Book Application")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Remove a contact")
        print("5. Save contacts to a file")
        print("6. Load contacts from a file")
        print("7. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            add_contact(name, phone)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            name = input("Enter contact name to search: ")
            search_contact(name)
        elif choice == '4':
            name = input("Enter contact name to remove: ")
            remove_contact(name)
        elif choice == '5':
            filename = input("Enter filename to save contacts: ")
            save_contacts(filename)
        elif choice == '6':
            filename = input("Enter filename to load contacts: ")
            load_contacts(filename)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
