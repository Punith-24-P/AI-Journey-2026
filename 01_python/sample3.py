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

    import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("\nGuess a number between 1 and 100!")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            return attempts


def main():
    best_score = None

    while True:
        print("\n===== Number Guessing Game =====")
        print("1. Play Game")
        print("2. View Best Score")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            score = play_game()
            if best_score is None or score < best_score:
                best_score = score
                print("🎉 New Best Score!")
        elif choice == '2':
            if best_score:
                print(f"Best Score: {best_score} attempts")
            else:
                print("No games played yet.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()

    import os

FILE_NAME = "tasks.txt"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return [line.strip() for line in file.readlines()]


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Removed: {removed}")
    except (IndexError, ValueError):
        print("Invalid input!")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== To-Do List =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    main()

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid amount!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def display_balance(self):
        print(f"{self.name}'s Balance: {self.balance}")


def main():
    name = input("Enter account holder name: ")
    account = BankAccount(name)

    while True:
        print("\n===== Banking System =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.display_balance()
        elif choice == '4':
            print("Thank you for using banking system!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()

def run_quiz():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
            "answer": "B"
        },
        {
            "question": "Which language is used for web apps?",
            "options": ["A. Python", "B. Java", "C. JavaScript", "D. All"],
            "answer": "D"
        },
        {
            "question": "Who developed Python?",
            "options": ["A. Elon Musk", "B. Guido van Rossum", "C. Bill Gates", "D. Mark Zuckerberg"],
            "answer": "B"
        }
    ]

    score = 0

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is {q['answer']}")

    print(f"\nYour final score: {score}/{len(questions)}")


def main():
    while True:
        print("\n===== Quiz App =====")
        print("1. Start Quiz")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            run_quiz()
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main() 