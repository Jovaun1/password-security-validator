import re
import time

# Sample stored password
correct_password = "Secure@123"

# Function to check password strength
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Too short"
    if not re.search("[A-Z]", password):
        return "Weak: Missing uppercase"
    if not re.search("[0-9]", password):
        return "Weak: Missing number"
    if not re.search("[@#$%]", password):
        return "Weak: Missing special character"
    return "Strong password"

# Function to simulate brute force attack
def brute_force_test():
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        test_password = input("Enter password: ")

        # NEW: Check password strength FIRST
        strength = check_password_strength(test_password)
        print(f"Password Strength: {strength}")

        if "Weak" in strength:
            print("Weak password not allowed. Try again.")
            attempts += 1
            continue

        #  THEN check if correct password
        if test_password == correct_password:
            print("Access Granted")
            return
        else:
            print("Access Denied")
            attempts += 1

    print("Account Locked due to multiple failed attempts")

# Function to test dictionary attack
def dictionary_attack_test():
    common_passwords = ["123456", "password", "admin", "qwerty"]

    for pwd in common_passwords:
        if pwd == correct_password:
            print("Vulnerable to dictionary attack")
            return

    print("Not vulnerable to common passwords")

# Function to test SQL injection
def sql_injection_test(input_value):
    if "'" in input_value or "--" in input_value:
        print("Potential SQL Injection detected")
    else:
        print("Input is safe")

# Run tests
print("Password Strength Test:")
print(check_password_strength("weak"))

print("\nDictionary Attack Test:")
dictionary_attack_test()

print("\nSQL Injection Test:")
sql_injection_test("admin' --")

print("\nBrute Force Test:")
brute_force_test()