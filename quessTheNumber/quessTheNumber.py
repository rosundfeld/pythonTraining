import random

def play():
    attenps = 0
    userInput = int(input("Enter a number between 1 and 100: "))
    if userInput < 1 or userInput > 100:
        print("Invalid input! Please enter a number between 1 and 100.")
        return
    randomNumber = random.randint(1, 100)
    while True:
        attenps += 1
        if userInput < randomNumber:
            print("Too low! Try again.")
            userInput = int(input("Enter a number between 1 and 100: "))
        elif userInput > randomNumber:
            print("Too high! Try again.")
            userInput = int(input("Enter a number between 1 and 100: "))
        else:
            print(f"Congratulations! You've guessed the number {randomNumber} in {attenps} attempts.")
            break