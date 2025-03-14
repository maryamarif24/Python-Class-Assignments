import json
import os
import sqlite3

# Database connection
def init_db():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER NOT NULL,
        genre TEXT NOT NULL,
        read_status BOOLEAN NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Load library from database
def load_library():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, author, year, genre, read_status FROM books")
    books = [dict(zip(["title", "author", "year", "genre", "read"], row)) for row in cursor.fetchall()]
    conn.close()
    return books

# Save book to database
def save_book(book):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO books (title, author, year, genre, read_status)
                      VALUES (?, ?, ?, ?, ?)''',
                   (book["title"], book["author"], book["year"], book["genre"], book["read"]))
    conn.commit()
    conn.close()

# Remove book from database
def remove_book_from_db(title):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE LOWER(title) = LOWER(?)", (title,))
    conn.commit()
    conn.close()

# Update book in database
def update_book_in_db(book, old_title):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute('''UPDATE books SET title = ?, author = ?, year = ?, genre = ?, read_status = ?
                      WHERE LOWER(title) = LOWER(?)''',
                   (book["title"], book["author"], book["year"], book["genre"], book["read"], old_title))
    conn.commit()
    conn.close()

# Add a book
def add_book(library):
    try:
        title = input("Enter the book title: ").strip()
        author = input("Enter the author: ").strip()
        year = int(input("Enter the publication year: ").strip())
        genre = input("Enter the genre: ").strip()
        read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

        book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read_status
        }

        library.append(book)
        save_book(book)

    except ValueError:
        print("\033[91mInvalid input for year. Please enter a valid number.\033[0m\n")
    else:
        print("\033[92mBook added successfully!\033[0m\n")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            remove_book_from_db(title)
            print("\033[91mBook removed successfully!\033[0m\n")
            return
    else:
        print("\033[93mBook not found.\033[0m\n")

# Edit a book
def edit_book(library):
    title = input("Enter the title of the book to edit: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            print("Editing book. Press Enter to keep current value.")
            try:
                book["title"] = input(f"Title ({book['title']}): ").strip() or book["title"]
                book["author"] = input(f"Author ({book['author']}): ").strip() or book["author"]
                year_input = input(f"Year ({book['year']}): ").strip()
                book["year"] = int(year_input) if year_input else book["year"]
                book["genre"] = input(f"Genre ({book['genre']}): ").strip() or book["genre"]
                read_status = input("Have you read this book? (yes/no): ").strip().lower()
                book["read"] = book["read"] if read_status == "" else (read_status == "yes")
                update_book_in_db(book, title)
            except ValueError:
                print("\033[91mInvalid input for year. Please enter a valid number.\033[0m\n")
                return
            else:
                print("\033[92mBook updated successfully!\033[0m\n")
                return
    else:
        print("\033[93mBook not found.\033[0m\n")

# Search for a book
def search_book(library):
    keyword = input("Enter keyword to search (title, author, genre): ").strip().lower()
    results = [book for book in library if keyword in book["title"].lower() or keyword in book["author"].lower() or keyword in book["genre"].lower()]

    if results:
        print("Search Results:")
        for i, book in enumerate(results, 1):
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("\033[93mNo books found.\033[0m\n")

# Display all books (with sorting)
def display_books(library):
    if not library:
        print("Your library is empty.\n")
        return

    print("Sort by:\n1. Title\n2. Author\n3. Year\n4. Genre")
    choice = input("Enter your choice: ").strip()

    sort_key = {"1": "title", "2": "author", "3": "year", "4": "genre"}.get(choice, "title")

    if sort_key == "year":
        sorted_library = sorted(library, key=lambda x: x["year"])
    else:
        sorted_library = sorted(library, key=lambda x: x[sort_key].lower())

    print("Your Library:")
    for i, book in enumerate(sorted_library, 1):
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    print()

# Display statistics
def display_statistics(library):
    if not library:
        print("Your library is empty.\n")
        return

    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    unread_books = total_books - read_books

    genres = {}
    for book in library:
        genre = book["genre"]
        genres[genre] = genres.get(genre, 0) + 1

    print("\nLibrary Statistics:")
    print(f"Total books: {total_books}")
    print(f"Books read: {read_books}")
    print(f"Books unread: {unread_books}")
    print("Books by genre:")
    for genre, count in genres.items():
        print(f"- {genre}: {count} books")
    print()


# Main menu
def main():
    init_db()
    library = load_library()

    while True:
        print("Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Edit a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Display statistics")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            edit_book(library)
        elif choice == "4":
            search_book(library)
        elif choice == "5":
            display_books(library)
        elif choice == "6":
            display_statistics(library)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("\033[91mInvalid choice. Please try again.\033[0m\n")

if __name__ == "__main__":
    main()