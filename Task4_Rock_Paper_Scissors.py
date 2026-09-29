# ==========================================
# CODSOFT PYTHON PROGRAMMING INTERNSHIP
# TASK 4 - ROCK PAPER SCISSORS
# ==========================================

import random

print("===================================")
print("      ROCK PAPER SCISSORS")
print("===================================")

user_score = 0
computer_score = 0

while True:

    print("\n1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "4":
        print("\nGame Over!")
        print("Your Score:", user_score)
        print("Computer Score:", computer_score)
        break

    if choice == "1":
        user = "Rock"
    elif choice == "2":
        user = "Paper"
    elif choice == "3":
        user = "Scissors"
    else:
        print("\nInvalid choice!")
        continue

    computer = random.choice(["Rock", "Paper", "Scissors"])

    print("\nYour choice:", user)
    print("Computer choice:", computer)

    if user == computer:
        print("Result: Tie!")

    elif user == "Rock" and computer == "Scissors":
        print("Result: You Win!")
        user_score += 1

    elif user == "Paper" and computer == "Rock":
        print("Result: You Win!")
        user_score += 1

    elif user == "Scissors" and computer == "Paper":
        print("Result: You Win!")
        user_score += 1

    else:
        print("Result: Computer Wins!")
        computer_score += 1

    print("Your Score:", user_score)
    print("Computer Score:", computer_score)
