import re
import time
import hashlib

# =========================
# CONSTANTS (IMPROVED)
# =========================
# Using constants improves maintainability and security control
PLAIN_PASSWORD = "Secure@123"

# NEW: Store password as HASH instead of plain text (security best practice)
CORRECT_PASSWORD = hashlib.sha256(PLAIN_PASSWORD.encode()).hexdigest()

MAX_ATTEMPTS = 3  # Limits login attempts
LOCKOUT_DELAY = 2  # NEW: Delay (seconds) after failed attempt to slow brute force

# =========================
# FUNCTION: HASH PASSWORD (NEW)
# =========================
# Converts user input into hashed value for secure comparison
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# =========================
# FUNCTION: PASSWORD STRENGTH CHECK (ENHANCED)
# =========================
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Too short"
    if not re.search("[A-Z]", password):
        return "Weak: Missing uppercase letter"
    if not re.search("[a-z]", password):  # NEW: Check lowercase
        return "Weak: Missing lowercase letter"
    if not re.search("[0-9]", password):
        return "Weak: Missing number"
    if not re.search("[@#$%]", password):
        return "Weak: Missing special character"
    return "Strong password"


# =========================
# FUNCTION: BRUTE FORCE TEST (SECURITY ENHANCED)
# =========================
def brute_force_test():
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        test_password = input("Enter password: ")

        # =========================
        # NEW: Check password strength BEFORE authentication
        # =========================
        strength = check_password_strength(test_password)
        print(f"Password Strength: {strength}")

        if "Weak" in strength:
            print("Weak password not allowed. Try again.\n")
            attempts += 1
            continue

        # =========================
        # NEW: HASH INPUT before comparison (secure authentication)
        # =========================
        hashed_input = hash_password(test_password)

        if hashed_input == CORRECT_PASSWORD:
            print("Access Granted")
            return
        else:
            print("Access Denied\n")
            attempts += 1

            # =========================
            # NEW: Delay to slow brute force attacks
            # =========================
            time.sleep(LOCKOUT_DELAY)

            # =========================
            # NEW: Log failed attempt (security monitoring)
            # =========================
            with open("log.txt", "a") as file:
                file.write("Failed login attempt\n")

    print("Account Locked due to multiple failed attempts")


# =========================
# FUNCTION: DICTIONARY ATTACK TEST (ENHANCED)
# =========================
def dictionary_attack_test():
    common_passwords = ["123456", "password", "admin", "qwerty"]

    if PLAIN_PASSWORD in common_passwords:
        print("Vulnerable to dictionary attack")
    else:
        print("Not vulnerable to common passwords")


# =========================
# FUNCTION: SQL INJECTION TEST (IMPROVED)
# =========================
def sql_injection_test(input_value):
    # NEW: Expanded detection patterns
    dangerous_patterns = ["'", "--", ";", "DROP", "SELECT"]

    for pattern in dangerous_patterns:
        if pattern.lower() in input_value.lower():
            print("Potential SQL Injection detected")
            return

    print("Input is safe")


# =========================
# MAIN MENU (NEW - UI IMPROVEMENT)
# =========================
def main():
    while True:
        print("\n==== PASSWORD SECURITY SYSTEM ====")
        print("1. Check Password Strength")
        print("2. Dictionary Attack Test")
        print("3. SQL Injection Test")
        print("4. Brute Force Login Test")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            pwd = input("Enter password: ")
            print(check_password_strength(pwd))

        elif choice == "2":
            dictionary_attack_test()

        elif choice == "3":
            user_input = input("Enter input to test: ")
            sql_injection_test(user_input)

        elif choice == "4":
            brute_force_test()

        elif choice == "5":
            print("Exiting system...")
            break

        else:
            print("Invalid option. Try again.")


# =========================
# RUN PROGRAM
# =========================
main()