import mysql.connector 
 
from tkinter import * 
 
from tkinter import messagebox 
# Connect to MySQL 
db = mysql.connector.connect( 
    host="localhost", 
    user="root", 
    password="Sneha@123", 
    database="contact" 
) 
 
cursor = db.cursor() 
 
# Create user table if not exists 
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS users ( 
        id INT AUTO_INCREMENT PRIMARY KEY, 
        username VARCHAR(255) UNIQUE, 
        password VARCHAR(255) 
    ) 
""") 
db.commit() 
 
# Create phonebook table if not exists 
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS contacts ( 
        id INT AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR(255), 
        phone_number VARCHAR(15), 
        user_id INT, 
        FOREIGN KEY (user_id) REFERENCES users(id) 
    ) 
""") 
db.commit() 
 
def authenticate(): 
    """Authenticate the user.""" 
    entered_username = username_entry.get() 
    entered_password = password_entry.get() 
 
    query = "SELECT * FROM users WHERE username = %s AND password = %s" 
    cursor.execute(query, (entered_username, entered_password)) 
    result = cursor.fetchone() 
 
    if result: 
        login_window.destroy() 
        open_phonebook_gui(result[0])  # Pass user ID to the main GUI 
    else: 
        messagebox.showerror("Login Failed", "Invalid username or password") 
 
def signup(): 
    """Create a new user account.""" 
    new_username = new_username_entry.get() 
    new_password = new_password_entry.get() 
 
    if not new_username or not new_password: 
        messagebox.showerror("Error", "Username and Password are required!") 
        return 
 
    try: 
        query = "INSERT INTO users (username, password) VALUES (%s, %s)" 
        values = (new_username, new_password) 
        cursor.execute(query, values) 
        db.commit() 
        messagebox.showinfo("Success", "Account created successfully!") 
        new_username_entry.delete(0, END) 
        new_password_entry.delete(0, END) 
    except mysql.connector.IntegrityError: 
        messagebox.showerror("Error", "Username already exists. Please choose a different username.") 
 
def open_phonebook_gui(user_id): 
    def add_contact(): 
        name = name_entry.get() 
        phone_number = phone_entry.get() 
 
        if not name or not phone_number: 
            messagebox.showerror("Error", "Name and Phone Number are required!") 
            return 
 
        query = "INSERT INTO contacts (name, phone_number, user_id) VALUES (%s, %s, %s)" 
        values = (name, phone_number, user_id) 
        cursor.execute(query, values) 
        db.commit() 
        messagebox.showinfo("Success", "Contact added successfully!") 
        name_entry.delete(0, END) 
        phone_entry.delete(0, END) 
 
    def search_contact(): 
        name = name_entry.get() 
 
        if not name: 
            messagebox.showerror("Error", "Name is required!") 
            return 
 
        query = "SELECT * FROM contacts WHERE name = %s AND user_id = %s" 
        cursor.execute(query, (name, user_id)) 
        result = cursor.fetchall() 
 
        if result: 
            contact_info = "Contact found:\n" 
            for row in result: 
                contact_info += f"ID: {row[0]}, Name: {row[1]}, Phone Number: {row[2]}\n" 
            messagebox.showinfo("Contact Found", contact_info) 
        else: 
            messagebox.showinfo("Contact Not Found", "Contact not found.") 
 
    def delete_contact(): 
        contact_id = id_entry.get() 
 
        if not contact_id: 
            messagebox.showerror("Error", "Contact ID is required!") 
            return 
 
        query = "DELETE FROM contacts WHERE id = %s AND user_id = %s" 
        cursor.execute(query, (contact_id, user_id)) 
        db.commit() 
        messagebox.showinfo("Success", "Contact deleted successfully!") 
        id_entry.delete(0, END) 
 
     
 
    # GUI Setup 
    root = Tk() 
    root.title("Phonebook Management System") 
 
    Label(root, text="Contact ID:").grid(row=0, column=0, padx=10, pady=5) 
    Label(root, text="Name:").grid(row=1, column=0, padx=10, pady=5) 
    Label(root, text="Phone Number:").grid(row=2, column=0, padx=10, pady=5) 
 
    id_entry = Entry(root, width=30) 
    id_entry.grid(row=0, column=1, padx=10, pady=5) 
    name_entry = Entry(root, width=30) 
    name_entry.grid(row=1, column=1, padx=10, pady=5) 
    phone_entry = Entry(root, width=30) 
    phone_entry.grid(row=2, column=1, padx=10, pady=5) 
 
    Button(root, text="Add Contact", command=add_contact).grid(row=3, column=0, columnspan=2, pady=10) 
    Button(root, text="Search Contact", command=search_contact).grid(row=4, column=0, columnspan=2, pady=10) 
    Button(root, text="Delete Contact", command=delete_contact).grid(row=5, column=0, columnspan=2, pady=10) 
     
    Button(root, text="Exit", command=root.destroy).grid(row=8, column=0, columnspan=2, pady=10) 
 
    root.mainloop() 
 
# GUI Setup for Login 
login_window = Tk() 
login_window.title("Login") 
 
Label(login_window, text="Username:").grid(row=0, column=0, padx=10, pady=5) 
Label(login_window, text="Password:").grid(row=1, column=0, padx=10, pady=5) 
 
username_entry = Entry(login_window, width=30) 
username_entry.grid(row=0, column=1, padx=10, pady=5) 
password_entry = Entry(login_window, width=30, show="*") 
password_entry.grid(row=1, column=1, padx=10, pady=5) 
 
login_button = Button(login_window, text="Login", command=authenticate) 
login_button.grid(row=2, column=0, columnspan=2, pady=10) 
 
# GUI Setup for Signup 
signup_window = Tk() 
signup_window.title("Signup") 
 
Label(signup_window, text="New Username:").grid(row=0, column=0, padx=10, pady=5) 
Label(signup_window, text="New Password:").grid(row=1, column=0, padx=10, pady=5) 
 
new_username_entry = Entry(signup_window, width=30) 
new_username_entry.grid(row=0, column=1, padx=10, pady=5) 
new_password_entry = Entry(signup_window, width=30, show="*") 
new_password_entry.grid(row=1, column=1, padx=10, pady=5) 
 
signup_button = Button(signup_window, text="Signup", command=signup) 
signup_button.grid(row=2, column=0, columnspan=2, pady=10) 
 
login_window.mainloop() 
signup_window.mainloop() 
 
# Close the connection 
cursor.close() 
db.close()
