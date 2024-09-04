import random

options = ["Rock,", "Paper", "Scissors"]

user_choice = input("Choose Rock, Paper or Scissors:  ")

computer_choice = random.choice(options)

print("You Chose:", user_choice)
print("Computer choice:", computer_choice)


if user_choice == computer_choice:
    print("It's a tie")

elif user_choice == "Rock" and computer_choice == "Scissors":
    print("Rock Smashes Scissors! You Win!")

elif user_choice == "Paper" and computer_choice == "Rock":
    print("Paper Covers Rock! You Win!")

elif user_choice == "Scissors" and computer_choice == "Paper":
    print("Scissors Cuts Paper! You Win!")

else:
    print("You Lose")

