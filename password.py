import streamlit as st
import re
st.title("Password Strength Checker")
st.write("Enter a password, and we will tell you how strong it is.")
password = st.text_input("Enter your password")
def password_strength(password):
    if len(password) < 8:
        return "Weak (Password should be at least 8 characters long)"
    elif not re.search("[a-z]", password):
        return "Weak (Password should contain at least one lowercase letter)"
    elif not re.search("[A-Z]", password): 
        return "Weak (Password should contain at least one uppercase letter)"
    elif not re.search("[0-9]", password):  
        return "Weak (Password should contain at least one digit)"
    elif not re.search("[!@#$%^&*(),.?\":{}|<>]", password): 
        return "Weak (Password should contain at least one special character)"
    else:
        return "Strong (Your password is strong!)"
if password:
    strength = password_strength(password)
    st.write(strength)
