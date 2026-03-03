library = {}

while True:
    print("\n===== Library Menu =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View Available Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # ---- Add Book ----
    if choice == "1":
        book_id = input("Enter Book ID: ")
        book_name = input("Enter Book Name: ")
        library[book_id] = {"name": book_name, "status": "Available"}
        print("Book added successfully!")

    # ---- Issue Book ----
    elif choice == "2":
        book_id = input("Enter Book ID to Issue: ")
        if book_id in library and library[book_id]["status"] == "Available":
            library[book_id]["status"] = "Issued"
            print("Book issued successfully!")
        else:
            print("Book not available or invalid ID!")

    # ---- Return Book ----
    elif choice == "3":
        book_id = input("Enter Book ID to Return: ")
        if book_id in library and library[book_id]["status"] == "Issued":
            library[book_id]["status"] = "Available"
            print("Book returned successfully!")
        else:
            print("Invalid return attempt!")

    # ---- View Available Books ----
    elif choice == "4":
        print("\nAvailable Books:")
        found = False
        for book_id in library:
            if library[book_id]["status"] == "Available":
                print(book_id, ":", library[book_id]["name"])
                found = True
        if not found:
            print("No books available")

    # ---- Exit ----
    elif choice == "5":
        print("Exiting Library System...")
        break

    else:
        print("Invalid choice! Try again.")
