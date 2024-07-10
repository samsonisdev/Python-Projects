# This is an Adventure Game. This program works on nested if/else conditions and leads the user to different adventures 

play = input("Do you want to play a game? ")
if play.lower() != 'yes':
    quit()

name = input("Please enter your name: ")
adventures = []

print("Welcome to the adventure Game", name, "!")

print("You're on a dirt road, there are two ways to go either left or right. Which way do you wanna go? ")
trouble1 = input("Left or Right? ").lower()
if trouble1 == 'right':
    print("You came across a dense jungle. There's a huge cave hole in front of you and a staircase. Do you want to go in the cave or climb the staircase? ")
    cave_stair = input("Cave or Stair? ").lower()
    if cave_stair == 'cave':
        adventures.append(cave_stair)
        print("You're in the cave now. It's all dark in here. You see a burning fire from one side and a ray of light from the other side. Do you want to go near the burning fire or ray of light? ")
    elif cave_stair == 'stair':
        adventures.append(cave_stair)
        print("You're at the top of the hill. You can see a whole village. You're free now!")
    else:
        print("Enter a valid option. You lose!")
elif trouble1 == 'left':
    print("You came across a river. You're thirsty and wanna drink water. There's crystal clear magical river water and a water bottle. Do you wanna drink the river water or have the water bottle? ")
    river_bottle = input("River or Bottle? ").lower()
    if river_bottle == 'river':
        adventures.append(river_bottle)
        print("You drank the magical water. You're able to fly now!")
    elif river_bottle == 'bottle':
        adventures.append(river_bottle)
        print("You drank the forbidden water. You're grabbed by some strangers!")
else:
    print("Enter a valid option. You lose!")

print("Thanks for playing!")
no_of_adv = input("Do you wanna know what adventures you did?").lower()
if no_of_adv != 'yes':
    quit()

for i in adventures:
    print("Adventures you did: ", end="")
    print(i, end="")
