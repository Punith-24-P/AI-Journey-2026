import random
import string

def generate_password(length=10, use_digits=True, use_symbols=True):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def check_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength == 3 or strength == 4:
        return "Moderate"
    else:
        return "Strong"


def main():
    while True:
        print("\n===== Password Tool =====")
        print("1. Generate Password")
        print("2. Check Password Strength")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            length = int(input("Enter password length: "))
            use_digits = input("Include digits? (y/n): ").lower() == 'y'
            use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

            password = generate_password(length, use_digits, use_symbols)
            print(f"Generated Password: {password}")

        elif choice == '2':
            password = input("Enter password to check: ")
            result = check_strength(password)
            print(f"Password Strength: {result}")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()