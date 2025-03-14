# 📚 Personal Library Manager

The **Personal Library Manager** is a command-line application built with **Python** and **SQLite**. It enables users to seamlessly manage their book collections by providing features to add, remove, update, search, and display books. This project demonstrates robust database management skills and efficient Python programming.

---

## 📝 Project Overview

The **Personal Library Manager** is a user-friendly system that helps you track your book collection and reading progress. Whether you are a casual reader or an avid book lover, this tool provides an organized way to keep your personal library in check.

### ✅ Key Features

1. **Add New Books**:  
   - Input and store book details (title, author, publication year, genre, and read status).  
2. **Remove Books**:  
   - Delete a book from your library by providing its title.  
3. **Edit Book Details**:  
   - Update any book’s information without removing it.  
4. **Search for Books**:  
   - Search by title, author, or genre with case-insensitive matching.  
5. **Display All Books**:  
   - View a list of all books, with sorting options:  
      - Title (A-Z)  
      - Author (A-Z)  
      - Year (Ascending)  
      - Genre (A-Z)  
6. **Display Statistics**:  
   - Get insights about your reading habits, including:  
      - Total books in the library.  
      - Number of books read.  
      - Number of unread books.  
7. **Persistent Storage**:  
   - Uses an SQLite database to permanently store book records, ensuring data is saved between sessions.  
8. **Interactive Menu**:  
   - User-friendly menu for navigation and input validation for seamless user experience.  

---

## 📊 Detailed Statistics Feature

The statistics section provides you with a comprehensive view of your reading progress:

- **Total Books**: Displays the total number of books in the library.  
- **Read Books**: Shows how many books you have marked as "read".  
- **Unread Books**: Displays the number of books still pending to be read.  

This feature helps you track and reflect on your reading journey.

---

## 📂 Project Structure

📦 Personal Library Manager ├── 📄 library_manager.py # Main script to manage books └── 📄 README.md # Project documentation


---

## 🛠️ Technologies Used

The project leverages the following technologies:

- **Python**: Core programming language used to implement the system.  
- **SQLite**: Lightweight database solution for storing book information persistently.  
- **CLI (Command-Line Interface)**: Provides an interactive menu-based interface for users.  

---

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have Python installed on your machine. Check using:

```bash
python --version
