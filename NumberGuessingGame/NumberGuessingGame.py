import random

number=random.randint(1,100)
attempts=0
guesses=[]

print("--Welcome to GuessIt---")
print("Guess a number between 1 and 100")

while(True):
    guess=int(input("Enter your Guess.."))
    attempts=attempts+1
    guesses.append(guess)
    if guess<number:
        print("You are very close..")
    elif guess>number:
        print("You are very far..")
    else:
        print("Correct! You Guessed it right.")
        print("Number:",number)
        print("Attempts:",attempts)
        print("Your Guesses",guesses)
        break