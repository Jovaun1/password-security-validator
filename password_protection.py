import re
import time

# =========================
# CONSTANTS (NEW IMPROVEMENT)
# Using constants improves readability and maintainability
# =========================
CORRECT_PASSWORD = "Secure@123"
MAX_ATTEMPTS = 3  # Limits login attempts to prevent brute force attacks


# Function to check password strength
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Too short"
    if not re.search("[A-Z]", password):
        return "Weak: Missing uppercase letter"
    if not re.search("[0-9]", password):
        return "Weak: Missing number"
    if not re.search("[@#$%]", password):
        return "Weak: Missing special character"
    return "Strong password"


# Function to simulate brute force attack (login system)
def brute_force_test():
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        test_password = input("Enter password: ")

        # =========================
        # NEW IMPROVEMENT:
        # Enforce password strength BEFORE authentication
        # Prevents weak passwords from being used
        # =========================
        strength = check_password_strength(test_password)
        print(f"Password Strength: {strength}")

        if "Weak" in strength:
            print("Weak password not allowed. Try again.\n")
            attempts += 1
            continue  # Skip authentication if password is weak

        # =========================
        # EXISTING LOGIC (ENHANCED BY SECURITY CHECK)
        # =========================
        if test_password == CORRECT_PASSWORD:
            print("Access Granted")
            return
        else:
            print("Access Denied\n")
            attempts += 1

    # =========================
    # NEW IMPROVEMENT:
    # Lock account after max attempts to prevent brute force attacks
    # =========================
    print("Account Locked due to multiple failed attempts")


# Function to test dictionary attack vulnerability
def dictionary_attack_test():
    common_passwords = ["123456", "password", "admin", "qwerty"]

    if CORRECT_PASSWORD in common_passwords:
        print("Vulnerable to dictionary attack")
    else:
        print("Not vulnerable to common passwords")


# Function to test SQL injection input
def sql_injection_test(input_value):
    if "'" in input_value or "--" in input_value:
        print("Potential SQL Injection detected")
    else:
        print("Input is safe")


# =========================
# RUN TESTS
# =========================

print("Password Strength Test:")
print(check_password_strength("weak"))

print("\nDictionary Attack Test:")
dictionary_attack_test()

print("\nSQL Injection Test:")
sql_injection_test("admin' --")

print("\nBrute Force Test:")
brute_force_test()