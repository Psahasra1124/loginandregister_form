import streamlit as st
import sqlite3
conn=sqlite3.connect("users.db",check_same_thread=False)
cursor=conn.cursor()
#Creating users table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    email TEXT UNIQUE,
    phone TEXT,
    username TEXT UNIQUE,
    password TEXT
               )
               """)
conn.commit()
def register_user(first_name,last_name,email,phone,username,password):
    try:
        cursor.execute("""
        INSERT INTO users (first_name, last_name, email, phone, username, password)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (first_name, last_name, email, phone, username, password))
        conn.commit()
        return True
    except:
        return False
def login_user(username,password):
    cursor.execute("""
    SELECT * FROM users WHERE username=? AND password=?
    """, (username, password))
    user = cursor.fetchone()
    return user is not None
st.title("User Registration and Login System")
menu = ["Register", "Login"]
choice = st.sidebar.selectbox("Menu", menu)
if choice == "Register":
    st.subheader("Create New Account")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        if register_user(first_name, last_name, email, phone, username, password):
            st.success("You have successfully registered!")
        else:
            st.error("Username or Email already exists.")
elif choice == "Login":
    st.subheader("Login to Your Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login_user(username, password):
            st.success("Login successful!")
        else:
            st.error("Invalid username or password.")   
            
