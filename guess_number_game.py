# practice flow control(conditional statements, loops), random module.
import random

secret_number = random.randint(1, 100)
guess = None
attempts = 0

print("Welcome to the Number Guessing Game!")

while guess != secret_number:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed it! The number was {secret_number}. You guessed it in {attempts} attempts.")
