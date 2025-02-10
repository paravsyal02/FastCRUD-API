import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",  # Default XAMPP username
        password="",  # Leave blank if you didn’t set a password
        database="crud_app"  # Name of the database you created
    )
    print("Database connection successful!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
