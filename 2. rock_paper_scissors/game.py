# 为什么这个函数是 def play_round(player_choice):，而不是 def play_round(computer_choice):？
# 因为这个函数的目的是处理玩家的选择，而不是计算机的选择。“玩家的选择是输入进来的参数”
# 想做 竞技/排位系统	胜 = +1，负 = -1 ✅ 谁先赢3局游戏就结束，然后再依照分数进行排名
# 想做 轻松休闲娱乐	胜 = +1，负 = 0 ✅ 只需知道谁胜谁负，不需知道排名
# ⬇️ 一直问直到玩家输入正确

import random

choices = ["rock", "paper", "scissors"]

def play_game(username, max_round = 5, win_threshold = 3):
    player_points = 0
    win_count = 0
    lose_count = 0
    round_results = []

    for i in range(1, max_round + 1):
        print(f"\nRound {i}:")
        
        while True:
            player_choice = input(f"{username}, enter your choice (rock, paper, scissors): ").lower()
            if player_choice in choices:
                break
            print("Invalid choice. Please choose rock, paper, or scissors.")

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
            results = "tie"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            player_points += 1
            win_count += 1
            results = "win"
        else:
            print("You lose this round.")
            lose_count += 1
            player_points -= 1
            results = "lose"

        print(f"Current results: {results}")
        print(f"Your points: {player_points}")

        round_results.append({
            "round": i,
            "player": player_choice,
            "computer": computer_choice,
            "result": results
        })

        if win_count >= win_threshold:
            print(f"🎉 Congratulations {username}, you won the game!")
            break
        elif lose_count >= win_threshold:
            print(f"😢 Sorry {username}, you lost the game.")
            break

    return player_points, round_results



        









