import random

def play(): 
    possibilities = ['rock', 'paper', 'scissor']
    user_choice = input("Enter your choice (rock, paper, scissor): ").lower()
    if user_choice not in possibilities:
        print("Invalid choice! Please choose rock, paper, or scissor.")
        return
    computer_choice = random.choice(possibilities)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissor') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissor' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")