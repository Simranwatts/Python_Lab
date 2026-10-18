
contacts = {}

while True:
    print("\n1.Add  2.View  3.Search  4.Update  5.Delete  6.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        name = input("Name: ")
        contacts[name] = input("Phone: ")
        print("Contact saved.")

    elif ch == "2":
        for n, p in contacts.items():
            print(n, ":", p)
        if not contacts:
            print("No contacts.")

    elif ch == "3":
        name = input("Search name: ")
        print(contacts.get(name, "Contact not found."))

    elif ch == "4":
        name = input("Update name: ")
        if name in contacts:
            contacts[name] = input("New phone: ")
            print("Contact updated.")
        else:
            print("Contact not found.")

    elif ch == "5":
        name = input("Delete name: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif ch == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
