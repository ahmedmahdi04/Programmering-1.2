import random

computer = random.choice(["rock", "paper", "scissors"])

user = input("rock, paper or scissors? ")

print("The computer chose", computer,"and the user chose", user +".")

# TODO - Implement the if statements that prints who wins

if user == "rock" and computer == "paper":
    print("computer wins")

elif user == "paper" and computer == "scissors":
    print("computer wins")

elif user == "rock" and computer == "scissors":
    print("user wins")

elif user == "paper" and computer == "rock":
    print("user wins")

elif user == "rock" and computer == "rock":
    print("equilibrium ")

elif computer == "scissors" and user == "paper":
    print("computer wins")

elif computer == "scrissors" and user == "rock":
    print("user wins")

elif computer == "paper" and user == "scrissors":
    print("user wins")

elif user == "scrissors" and computer == "scrissors":
    print("equilibrium ") 
    
