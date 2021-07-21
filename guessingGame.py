import random

print("Number Guessing Game")

number = random.randint(1, 100)

chances = 0

print("Guess a number between 1 and 100:")

while chances < 5:
    guessNumber = int(input("Type in a number to guess:"))

    if guessNumber == number:
        print("Congratulations, You Won!!!! Whoa, that was some psycic stuff right there. Good job, mate.")
        break

    elif guessNumber < number:
        print("You guess was wayyy lower than the actual number . Guess again")

    else: 
        print("Your guess was wayyy higher than the actual number. Guess again")

    chances += 1

if not chances < 5:
     print("Aye... You lost. I'm not going to be mean and tell you that the number was", number)
     
