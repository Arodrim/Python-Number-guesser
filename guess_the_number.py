import random

random_number = random.randint(1, 10)

while True:
    guess = input("Guess the number (between 1 and 10): ")
    int_guess = int(guess)

    if int_guess == random_number:
        print("You guessed it!")
        break
    else:
        print("Try again!")
