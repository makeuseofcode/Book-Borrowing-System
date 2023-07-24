import tkinter as tk
from tkinter import messagebox

class BookBorrowingSystem:
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Book Borrowing System")
        self.master.geometry("750x600")
        self.master.config(bg='#708090')
        self.books = []
        self.lend_list = []
        self.record = {}
        self.setup_gui()
        self.librarians = []

    def setup_gui(self):
        self.login_label = tk.Label(self.master, text="Book Borrowing System", font=("Helvetica", 24), bg='#708090', fg='white')
        self.login_label.pack(pady=(30, 10))
        self.username_label = tk.Label(self.master, text="Username", font=("Helvetica", 16), bg='#708090', fg='white')
        self.username_label.pack()
        self.username_entry = tk.Entry(self.master, font=("Helvetica", 16))
        self.username_entry.pack()
        self.password_label = tk.Label(self.master, text="Password", font=("Helvetica", 16), bg='#708090', fg='white')
        self.password_label.pack()
        self.password_entry = tk.Entry(self.master, font=("Helvetica", 16), show="*")
        self.password_entry.pack()
        self.login_button = tk.Button(self.master, text="Login", command=self.login, font=("Helvetica", 14))
        self.login_button.pack(pady=10)
        self.register_button = tk.Button(self.master, text="Register", command=self.register, font=("Helvetica", 14))
        self.register_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        for librarian in self.librarians:
            if username == librarian[0] and password == librarian[1]:
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
                self.login_label.destroy()
                self.username_label.destroy()
                self.username_entry.destroy()
                self.password_label.destroy()
                self.password_entry.destroy()
                self.login_button.destroy()
                self.register_button.destroy()
                self.book_management_screen()
                return
        messagebox.showerror("Error", "Invalid username or password. Please register if not done already.")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.librarians.append([username, password])
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def book_management_screen(self):
        self.add_book_label = tk.Label(self.master, text="Add Book", font=("Helvetica", 18), bg='#708090', fg='white')
        self.add_book_label.pack(pady=(20, 5))
        self.add_book_entry = tk.Entry(self.master, font=("Helvetica", 14))
        self.add_book_entry.pack()
        self.add_book_button = tk.Button(self.master, text="Add Book", command=self.add_book, font=("Helvetica", 14))
        self.add_book_button.pack(pady=5)
        self.return_book_label = tk.Label(self.master, text="Return Book", font=("Helvetica", 18), bg='#708090', fg='white')
        self.return_book_label.pack(pady=5)
        self.return_book_entry = tk.Entry(self.master, font=("Helvetica", 14))
        self.return_book_entry.pack()
        self.return_book_button = tk.Button(self.master, text="Return Book", command=self.return_book, font=("Helvetica", 14))
        self.return_book_button.pack(pady=5)
        self.remove_book_label = tk.Label(self.master, text="Remove Book", font=("Helvetica", 18), bg='#708090', fg='white')
        self.remove_book_label.pack(pady=5)
        self.remove_book_entry = tk.Entry(self.master, font=("Helvetica", 14))
        self.remove_book_entry.pack()
        self.remove_book_button = tk.Button(self.master, text="Remove Book", command=self.remove_book, font=("Helvetica", 14))
        self.remove_book_button.pack(pady=5)
        self.issue_book_label = tk.Label(self.master, text="Issue Book", font=("Helvetica", 18), bg='#708090', fg='white')
        self.issue_book_label.pack(pady=5)
        self.issue_book_entry = tk.Entry(self.master, font=("Helvetica", 14))
        self.issue_book_entry.pack()
        self.issue_book_button = tk.Button(self.master, text="Issue Book", command=self.issue_book, font=("Helvetica", 14))
        self.issue_book_button.pack(pady=5)
        self.view_books_button = tk.Button(self.master, text="View Books", command=self.view_books, font=("Helvetica", 14))
        self.view_books_button.pack(pady=10)

    def add_book(self):
        book = self.add_book_entry.get()
        self.books.append(book)
        self.record[book] = "added"
        messagebox.showinfo("Success", "Book added successfully")
        self.add_book_entry.delete(0, tk.END)

    def remove_book(self):
        book = self.remove_book_entry.get()
        if book in self.books:
            self.books.remove(book)
            if book in self.record:
                del self.record[book]
            messagebox.showinfo("Success", "Book removed successfully")
        else:
            messagebox.showerror("Error", "Book not found")
        self.remove_book_entry.delete(0, tk.END)

    def issue_book(self):
        book = self.issue_book_entry.get()
        if book in self.books:
            self.lend_list.append(book)
            self.books.remove(book)
            self.record[book] = "issued"
            messagebox.showinfo("Success", "Book issued successfully")
        else:
            messagebox.showerror("Error", "Book not found")
        self.issue_book_entry.delete(0, tk.END)

    def return_book(self):
        book = self.return_book_entry.get()
        if book in self.lend_list:
            self.lend_list.remove(book)
            self.books.append(book)
            self.record[book] = "returned"
            messagebox.showinfo("Success", "Book returned successfully")
        elif book in self.books and self.record.get(book) == "added":
            messagebox.showerror("Error", "Book can't be returned. It hasn't been issued.")
        else:
            messagebox.showerror("Error", "Book not found or not issued")
        self.return_book_entry.delete(0, tk.END)

    def view_books(self):
        message = ""
        for book, status in self.record.items():
            message += f"{book}: {status}\n"
        if not message:
            message = "No book records available."
        messagebox.showinfo("Books", message)

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    book_borrowing_system = BookBorrowingSystem()
    book_borrowing_system.run()
