# This is a Roll a Dice Game. This program asks the user to enter number of players. The program works for the number of players the user enters
# giving each person a turn. This program adds the points of the dice the user rolls and tells who's the winner among the given number of players.  

import random

play = input("Would you like to play Roll a Dice? ").lower()
if play != 'yes':
    quit()

score = 0
max_score = 20
no_of_rolls = 0

while True:
    players = input("Enter number of players (Max 4 & Min 2 players): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Enter players from 2 - 4")

player_score = [0 for _ in range(players)]
print("Players Scores: ", player_score)

while max(player_score) < max_score:
    for idx in range(players):
        print("\nPlayer", idx + 1, "turn has started\n")
        print("Your total score is", player_score[idx])
        score = 0

        while True:
            dice = random.randint(1, 6)
            role = input("Press R to roll and Q to quit: ").lower()
            if role == 'r':
                print("Dice rolled: ", dice)
                no_of_rolls += 1
                score += dice
                print("Your score is: ", score)
            if role == 'q' or role == 'quit':
                quit()
            if dice == 1:
                score = 0
                print("Uhhoo! You're back at 0. Make 20 points to win.")
            elif score >= 20:
                print("\033[33mYou won! Your total score is", score, "\033[0m")
                print("You rolled the dice", no_of_rolls, "times.")
                player_score[idx] += score
                break
    break

max_score = max(player_score)
winner = player_score.index(max_score)
print("The winner is Player", winner + 1, "with a score of", max_score)
