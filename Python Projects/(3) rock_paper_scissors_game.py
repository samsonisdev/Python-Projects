import random

user_wins = 0
computer_wins = 0
tie = 0

game_list = ['rock', 'paper', 'scissors']

while True:

    comp_choice = random.choice(game_list)
    print("--------------------------------")
    choice = input("Rock, Paper, or Scissors or Q(quit)?: ").lower()
    if choice == 'q':
        print("     Your Score: ", user_wins)
        print("     Computer score: ", computer_wins)
        print("     Ties: ", tie)

        if user_wins == 0 and computer_wins == 0:
            print("     Play game to build score!")

        elif user_wins == 0:
            print("     You Lost!")

        elif computer_wins == 0:
            print("     Computer Lost!")

        quit()

    elif choice == 'rock':
        if comp_choice == 'rock':
            tie += 1
            print("Computer: ", comp_choice)
            print("You: ", choice)
            print("It's a tie!")
        elif comp_choice == 'scissors':
            user_wins += 1
            print("Computer: ", comp_choice)
            print("You: ", choice)
            print("You won!")
        elif comp_choice == 'paper':
            computer_wins += 1
            print("Computer: ", comp_choice)
            print("You: ", choice)
            print("Computer won!!")

    elif choice == 'paper':
        if comp_choice == 'paper':
            tie += 1
            print("Computer: ", comp_choice)
            print("You: ", choice)
            print("It's a tie!")
        elif comp_choice == 'scissors':
            computer_wins += 1
            print("Computer: ", comp_choice)
            print("You: ", choice)
            print("Computer won!")
        elif comp_choice == 'rock':
            user_wins += 1
            print("Computer: ", comp_choice)
            print("You: ", choice)
            print("You won!!")

    elif choice == 'scissors':
        if comp_choice == 'scissors':
            tie += 1
            print("Computer: ", comp_choice)
            print("You: ", choice)
            print("It's a tie!")
        elif comp_choice == 'rock':
            computer_wins += 1
            print("Computer: ", comp_choice)
            print("You: ", choice)
            print("Computer won!")
        elif comp_choice == 'paper':
            user_wins += 1
            print("Computer: ", comp_choice)
            print("You: ", choice)
            print("You won!!")
    else:
        print("Please enter Rock, Paper or Scissors. Or Q to quit game!")



