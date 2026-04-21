import re
import time
import hashlib
import os
from datetime import datetime

# =========================
# CONSTANTS (IMPROVED)
# =========================
PLAIN_PASSWORD = "Secure@123"
CORRECT_PASSWORD = hashlib.sha256(PLAIN_PASSWORD.encode()).hexdigest()

MAX_ATTEMPTS = 3
LOCKOUT_DELAY = 2

# NEW: File storage for users + logs
USER_FILE = "users.txt"
LOG_FILE = "log.txt"


# =========================
# FUNCTION: HASH PASSWORD
# =========================
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# =========================
# FUNCTION: PASSWORD STRENGTH SCORE (NEW)
# =========================
# Gives numeric score instead of just Weak/Strong
def password_strength_score(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[a-z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[@#$%]", password):
        score += 1

    return score


# =========================
# FUNCTION: PASSWORD STRENGTH CHECK (UPDATED)
# =========================
def check_password_strength(password):
    score = password_strength_score(password)
    return f"Score: {score}/5"


# =========================
# FUNCTION: LOGGING SYSTEM (NEW)
# =========================
def log_event(message):
    with open(LOG_FILE, "a") as file:
        file.write(f"{datetime.now()} - {message}\n")


# =========================
# FUNCTION: REGISTER USER (NEW)
# =========================
def register_user():
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    score = password_strength_score(password)
    print(f"Password Strength Score: {score}/5")

    # Enforce stronger password policy
    if score < 4:
        print("Password too weak. Registration failed.\n")
        return

    hashed = hash_password(password)

    with open(USER_FILE, "a") as file:
        file.write(f"{username},{hashed}\n")

    print("User registered successfully!\n")
    log_event(f"User registered: {username}")


# =========================
# FUNCTION: LOGIN SYSTEM (NEW)
# =========================
def login():
    if not os.path.exists(USER_FILE):
        print("No users found. Please register first.\n")
        return

    username = input("Enter username: ")
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        password = input("Enter password: ")

        print(check_password_strength(password))

        hashed_input = hash_password(password)

        with open(USER_FILE, "r") as file:
            users = file.readlines()

        for user in users:
            stored_username, stored_password = user.strip().split(",")

            if username == stored_username:
                if hashed_input == stored_password:
                    print("Login successful!\n")
                    log_event(f"Successful login: {username}")
                    return
                else:
                    print("Incorrect password\n")
                    log_event(f"Failed login: {username}")
                    break

        attempts += 1
        time.sleep(LOCKOUT_DELAY)

    print("Account Locked due to multiple failed attempts\n")
    log_event(f"Account locked: {username}")


# =========================
# FUNCTION: DICTIONARY ATTACK TEST
# =========================
def dictionary_attack_test():
    common_passwords = ["123456", "password", "admin", "qwerty"]

    if PLAIN_PASSWORD in common_passwords:
        print("Vulnerable to dictionary attack")
    else:
        print("Not vulnerable to common passwords")


# =========================
# FUNCTION: SQL INJECTION TEST
# =========================
def sql_injection_test(input_value):
    dangerous_patterns = ["'", "--", ";", "DROP", "SELECT"]

    for pattern in dangerous_patterns:
        if pattern.lower() in input_value.lower():
            print("Potential SQL Injection detected")
            log_event("SQL Injection attempt detected")
            return

    print("Input is safe")


# =========================
# MAIN MENU (UPDATED)
# =========================
def main():
    while True:
        print("\n==== PASSWORD SECURITY SYSTEM ====")
        print("1. Register User")
        print("2. Login")
        print("3. Check Password Strength")
        print("4. Dictionary Attack Test")
        print("5. SQL Injection Test")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            register_user()

        elif choice == "2":
            login()

        elif choice == "3":
            pwd = input("Enter password: ")
            print(check_password_strength(pwd))

        elif choice == "4":
            dictionary_attack_test()

        elif choice == "5":
            user_input = input("Enter input to test: ")
            sql_injection_test(user_input)

        elif choice == "6":
            print("Exiting system...")
            break

        else:
            print("Invalid option. Try again.")


# =========================
# RUN PROGRAM
# =========================
main()