import json

FILENAME = "books.json"
books = []

#Function to add books
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    try:
        year = int(input("Enter year of publication: "))
        books.append({
            "title": title,
            "author": author,
            "year": year
        })
        print("Book added successfully!!!")
    except ValueError:
        print("❌ Invalid year. Please enter a number.")
# Function to view all books
def view_books():
    if not books:
        print("No books added yet. ")
    else:
        print("\n Your Book Collection:")
        for i, book in enumerate(books, 1):
            print(f"{i}. {book['title']} by {book['author']} ({book['year']})")
def search_book():
    search_title = input("Enter the title to search for: ").lower
    found = False
    for book in books:
        if book["title"].lower() == search_title:
            print(f"found: {book['title']} by {book['author']} ({book['year']})")
            found = True
            break
        if not found:
            print("Book not found.")

#Main menu loop
while True:
    print("\n=== My Book Tracker ===")
    print("1. Add a Book")
    print("2. View All Books")
    print("3. Search by Title")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice =="3":
        search_book()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2,3, or 4.")