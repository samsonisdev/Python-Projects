import turtle
import time
import random

WIDTH = 500
HEIGHT = 500

COLORS = ['red', 'blue', 'black', 'orange', 'pink', 'cyan', 'green', 'yellow', 'purple', 'brown']

# 1st Function:
def get_number_of_turtles():
    while True:
        no_of_turtles = input("How many turtles do you want to race (2 - 10): ")
        if no_of_turtles.isdigit():
            no_of_turtles = int(no_of_turtles)
        else:
            print("That was not a number!")
            continue

        if 2 <= no_of_turtles <= 10:
            print(f"{no_of_turtles} turtles to race!")
            break
        else:
            print("You can only race 2-10 turtles")
    return no_of_turtles

# 4th Function:
def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            move = random.randrange(1, 20)
            racer.forward(move)

            x, y = racer.pos()
            if y >= HEIGHT:
                return colors[turtles.index(racer)]

# 3rd Function:
def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

# 2nd Function:
def turtle_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")


turtles_to_race = get_number_of_turtles()
turtle_screen()
random.shuffle(COLORS)
racer = COLORS[:turtles_to_race]
winner = race(racer)
print("The winner is", winner)
time.sleep(5)

