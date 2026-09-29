# ==========================================
# CODSOFT PYTHON PROGRAMMING INTERNSHIP
# TASK 5 - CONTACT BOOK
# ==========================================

contacts = {}


# ---------- ADD CONTACT ----------
def add_contact():
    print("\n========== ADD CONTACT ==========")

    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    print("\nContact added successfully!")


# ---------- VIEW CONTACTS ----------
def view_contacts():
    print("\n========== CONTACT LIST ==========")

    if len(contacts) == 0:
        print("No contacts available.")
        return

    for name, details in contacts.items():
        print("\nName:", name)
        print("Phone:", details["phone"])
        print("Email:", details["email"])
        print("Address:", details["address"])


# ---------- SEARCH CONTACT ----------
def search_contact():
    print("\n========== SEARCH CONTACT ==========")

    name = input("Enter name to search: ")

    if name in contacts:
        print("\nContact found!")
        print("Name:", name)
        print("Phone:", contacts[name]["phone"])
        print("Email:", contacts[name]["email"])
        print("Address:", contacts[name]["address"])
    else:
        print("\nContact not found.")


# ---------- UPDATE CONTACT ----------
def update_contact():
    print("\n========== UPDATE CONTACT ==========")

    name = input("Enter name to update: ")

    if name in contacts:

        print("\nEnter new contact details:")

        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")

        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }

        print("\nContact updated successfully!")

    else:
        print("\nContact not found.")


# ---------- DELETE CONTACT ----------
def delete_contact():
    print("\n========== DELETE CONTACT ==========")

    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        print("\nContact deleted successfully!")
    else:
        print("\nContact not found.")


# ---------- MAIN MENU ----------
while True:

    print("\n===================================")
    print("           CONTACT BOOK")
    print("===================================")

    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("\nThank you for using the Contact Book!")
        break

    else:
        print("\nInvalid choice. Please try again.")
