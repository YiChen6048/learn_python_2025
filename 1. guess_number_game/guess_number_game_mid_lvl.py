# Middle Level Number Guessing Game
# skills practiced: Control Structures, Function Encapsulation, Error Handling, List Operations, User Input & Output, Random Module, Main Entry Check, Algorithmic Thinking (Binary search used in AI guessing mode)

# This code implements a number guessing game with difficulty levels and an AI guessing feature.
# Game 1: The user can choose between easy and hard modes
# Game 2: The AI can guess a number the user is thinking of
# The game set guess attempt limit
# The game tracks the number of attempts and provides feedback on guesses.

import random

def play_game():
    print("Welcome to number guessing game!")
    print("Choose a difficulty level:")
    print("1. Easy (1-100)")
    print("2. Hard (1-1000)")
    difficulty = input("Enter 1 or 2: ")

    if difficulty == "1":
        max_number = 100
        max_attempts = 10
    elif difficulty == "2":
        max_number = 1000
        max_attempts = 15
    else:
        print("Invalid choice. Defaulting to Easy mode.")
        max_number = 100
        max_attempts = 10

    secret_number = random.randint(1, max_number)
    guesses = []

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{max_attempts}: Guess the number (1-{max_number}): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue #玩家输入非数字，比如 "hello"，触发 ValueError，continue 跳过这一轮后面的代码，重新开始新一轮输入


        guesses.append(guess)

        if guess < 1 or guess > max_number:
            print(f"Please enter a number between 1 and {max_number}.")
            continue 

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed it! The number was {secret_number}. You guessed it in {attempt} attempts.")
            break
    else: # 为什么我猜对了，却不会触发 else？答案是：for ... else 中的 else 只在 for 循环完整执行完所有轮次 且没有 break 的时候执行。
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {secret_number}.")

    print("Your guesses were:", guesses)

def ai_guess_game():
    print("Now it's AI's turn to guess your number!")
    print("Think of a number between 1 and 100, and I will try to guess it.")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2  # binary search algorithm can efficiently guess the user's number
        attempts += 1
        print(f"AI guesses: {guess}")
        feedback = input("Is it too low (L), too high (H), or correct (C)? ").strip().upper()

        if feedback == 'C':
            print(f"AI guessed your number {guess} in {attempts} attempts!")
            return
        elif feedback == 'L':
            low = guess + 1
        elif feedback == 'H':
            high = guess - 1
        else:
            print("Invalid input. Please enter L, H, or C.")

    print("AI couldn't guess your number. Please check your inputs.")

def main():
    while True:   # 不断重复显示菜单，除非用户选了退出，才用 break 停止
        print("\nMenu:")
        print("1. Play Number Guessing Game")
        print("2. AI Guess Your Number")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            play_game()
        elif choice == "2":
            ai_guess_game()
        elif choice == "3":
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__": #若是被别的文件导入（如 import guess_game）那么__name__ == "game" ❌不会执行main()；若是直接运行这个文件（如 python guess_game.py）那么__name__ == "__main__"	✅ 会执行main()
    main()

