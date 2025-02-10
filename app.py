import streamlit as st
import mysql.connector as msc

# Connect to the database
def create_connection():
    return msc.connect(
        host="localhost",
        user="root",
        password="",
        database="crud_app"
    )

# Create a streamlit app
st.title("Simple Crud Application")

# Function to fetch all users
def get_users():
    db = create_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    db.close()
    return users

# Function to add a new user
def add_user(name, email, age):
    db = create_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)",(name, email, age)) 
    db.commit()
    db.close()

# Function to edit a new user
def update_user(user_id, name, email, age):
    db = create_connection()
    cursor = db.cursor()
    cursor.execute("UPDATE users SET name = %s, email = %s, age = %s WHERE id = %s", (name, email, age, user_id),)
    db.commit()
    db.close()

# Function to delete the user
def delete_user(user_id):
    db = create_connection()
    cursor = db.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    db.commit()
    db.close()


# Streamlit UI

# Sidebar Menu for User Actions
menu = st.sidebar.selectbox("Menu", ["View Users", "Add User", "Edit User", "Delete User"])

# Handling "View Users" Option
if menu == "View Users":
    st.subheader("Users List")
    users = get_users()
    if users:
        for user in users:
            st.write(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}, Age: {user['age']}")
    else:
        st.write("No users found.")

# Handling "Add User" Option
elif menu == "Add User":
    st.subheader("Add New User")
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age",min_value=1, step=1)
    if st.button("Add User"):
        add_user(name, email, age)
        st.success("User added successfully")

# Handling "Edit User" Option
elif menu == "Edit User":
    st.subheader("Edit User")
    user_id = st.number_input("Enter User ID", min_value=1, step=1)
    name = st.text_input("New Name")
    email = st.text_input("New Email")
    age = st.number_input("New Age",min_value=1, step=1)
    if st.button("Update User"):
        update_user(user_id, name, email, age)
        st.success("User updated successfully")

# Handling "Delete User" Option
elif menu == "Delete User":
    st.subheader("Delete User")
    user_id = st.number_input("Enter User ID to Delete", min_value=1, step=1)
    if st.button("Delete User"):
        delete_user(user_id)
        st.success("User deleted successfully")
