# phonebook-management-system
The code contains implementation of a basic phonebook management system using Python and MySQL.

**OVERVIEW**
A phonebook management system is a software application designed to help users organize and manage their contacts. It typically allows users to store contact information such as names, phone numbers, addresses, and email addresses in a digital format. The system provides functionalities such as adding new contacts, searching for existing contacts, updating contact details, and deleting contacts. 

Project: Phonebook Application
This project implements a phonebook application with user authentication.

**Database Design**

The application uses MySQL to store user credentials and contact information. Two tables are created:
users: Stores user credentials (username, password)
contacts: Stores contact information (linked to a user ID from the users table)

**User Authentication**

Users can log in with username and password.
New users can sign up by providing a unique username and password.

**Phonebook Functionality**

The application provides a graphical user interface (GUI) built with tkinter.
Login and signup functionalities are implemented with separate windows.
After successful login, users can access the main phonebook GUI.
The GUI allows users to:
  Add new contacts
  Search for existing contacts
  Delete contacts
Note: All CRUD (Create, Read, Update, Delete) operations on contacts interact with the contacts table in the database.

**Program Termination**

Upon program completion, the database connection and cursor are closed to release resources.

