import random

play = input("Do you want to play a game? ")
if play.lower() != 'yes':
    print("Okay! Bye!")
    quit()

print("QUIZ GAME")
num = input("How big the number should be?: ")
if num.isdigit():
    num = int(num)
else:
    print("Oops! Restart Game.")
    quit()

guesses = 0

while True:
    guesses += 1
    random_num = random.randrange(1, num)

    make_a_guess = input("Make a guess: ")
    if make_a_guess.isdigit():
        make_a_guess = int(make_a_guess)
    else:
        print("Oops! You must enter a number!")
        continue

    if make_a_guess == random_num:
        print("Computer Guess: ", random_num)
        print("correct")
        break
    else:
        print("Computer Guess: ", random_num)
        print("wrong")

print("You got it in", guesses, "guesses!")

if guesses >= 5:
    print("You're really weak at guessing numbers")
else:
    print("Great job!")

