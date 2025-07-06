import random

choices = ["rock", "paper", "scissors"]

def get_player_choice():
    choice = input("Your choice (rock/paper/scissors): ").lower()
    while choice not in choices:
        print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
        choice = input("Your choice: ").lower()
    return choice

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_round():
    player_choice = get_player_choice()
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(player_choice, computer_choice)
    print(result)

def main():
    print("Welcome to the Paper Rock Scissors Game!")
    play_game = True
    while play_game:
        play_round()
        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again == "no":
                print("Thanks for playing!")
                play_game = False  # 退出外层循环
                break
            elif play_again == "yes":
                break  # 回到外层继续玩
            else:
                print("Invalid input! Please type 'yes' or 'no'.")

if __name__ == "__main__":
    main()