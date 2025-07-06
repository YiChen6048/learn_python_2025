# Middle Level Rock-Paper-Scissors Game
# Skills practiced: Control Structures, Function Encapsulation, User Input & Output, Random Module, File I/O, Main Entry Check, Game Logic, Scoreboard Management

# This file is the main entry point for the Rock-Paper-Scissors game.
# It allows users to play in solo or multiplayer mode and updates the scoreboard.
# It imports the play_game function from the game module.   

from game import play_game
import os

SCOREBOARD_PATH = os.path.join("2. rock_paper_scissors", "scoreboard.txt")

def update_scoreboard(username, player_points):
    try:
        with open(SCOREBOARD_PATH, "a") as f:
            f.write(f"{username}: {player_points}\n") # write the username and points to the scoreboard file
    except Exception as e:
        print(f"Error updating scoreboard: {e}") # if there is an error, print it

def main():
    print("Welcome to the game!")
    username = input("Enter your username: ")
    
    points, records = play_game(username) # Play the game and get points
    
    print("\nGame record is: ")
    for r in records:
        print(f"round = {r['round']}: player = {r['player']} computer = {r['computer']} result = {r['result']}")

    print(f"\nTotal points: {points}")

    update_scoreboard(username, points)
    print("\nScoreboard updated.")

def multiplayer():
    num_players = int(input("Please enter the number of players: "))
    for i in range(num_players):
        print(f"\nPlayer {i+1}: ")
        username = input("Please enter your username: ")
        player_points, round_results = play_game(username)
       
        print("\nGame record is:")
        for r in round_results:
            print(f"Round {r['round']}: player = {r['player']}, computer = {r['computer']}, result = {r['result']}")

        win_count = sum(1 for r in round_results if r['result'] == 'win')
        lose_count = sum(1 for r in round_results if r['result'] == 'lose')

        if win_count > lose_count:
            print(f"\nResult: {username} won the game!")
        elif lose_count > win_count:
            print(f"\nResult: {username} lost the game.")
        else:
            print(f"\nResult: {username} tied the game.")

        print(f"Total points: {player_points}")
        update_scoreboard(username, player_points)
        print("Scoreboard updated.")

if __name__ == "__main__":
    mode = input("Choose mode: 1 - solo, 2 - multiplayer: ")
    if mode == "1":
        main()
    else:
        multiplayer()

