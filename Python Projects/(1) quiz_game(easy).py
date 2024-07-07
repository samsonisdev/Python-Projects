print("Welcome to my computer quiz!")

playing = input("Do you want to play?: ")
if playing.lower() != 'yes':
    quit()

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == 'central processing unit':
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What does GPU stand for? ")
if answer.lower() == 'graphics processing unit':
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What does PSU stand for? ")
if answer.lower() == 'power supply unit':
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What does ATM stand for? ")
if answer.lower() == 'automated teller machine':
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What does USA stand for? ")
if answer.lower() == 'united states of america':
    print("Correct!")
    score += 1
else:
    print("Wrong!")

per = score /4*100
print("Your Score is: " + str(per) + "%"+ " \nYou got " + str(score) + " out of 4 questions correct")