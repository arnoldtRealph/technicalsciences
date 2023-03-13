import streamlit as st
import sqlite3
from sqlite3 import Error

# create connection to SQLite database
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('users.db')
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return conn

# create a users table in SQLite database if it doesn't exist
def create_users_table(conn):
    try:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        """)
        print("Users table created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

# add a new user to the SQLite database
def add_user(conn, username, password):
    try:
        c = conn.cursor()
        c.execute("""
            INSERT INTO users (username, password) VALUES (?, ?)
        """, (username, password))
        conn.commit()
        print("User added successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

# retrieve a user from the SQLite database by username and password
def get_user(conn, username, password):
    try:
        c = conn.cursor()
        c.execute("""
            SELECT * FROM users WHERE username=? AND password=?
        """, (username, password))
        return c.fetchone()
    except Error as e:
        print(f"The error '{e}' occurred")

# create connection to SQLite database
conn = create_connection()
if conn is not None:
    create_users_table(conn)

# create login page
st.title("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user = get_user(conn, username, password)
    if user is not None:
        st.success("Logged in!")
    else:
        st.error("Invalid username or password")

# create register page
st.title("Register")

new_username = st.text_input("New username")
new_password = st.text_input("New password", type="password")

if st.button("Register"):
    add_user(conn, new_username, new_password)
    st.success("User registered successfully")



def show_login_page():
    # Create a connection to the database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Create the users table if it doesn't already exist
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password TEXT)''')

    # Display the login form
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Check if the username and password are valid
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        result = c.execute(query).fetchone()
        if result is not None:
            st.success("Logged in!")
        else:
            st.error("Invalid username or password")

    # Close the database connection
    conn.close()
