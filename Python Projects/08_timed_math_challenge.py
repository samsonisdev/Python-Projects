import random
import time

operators = ["+", "-", "*"]
operand1 = 2
operand2 = 13
total_questions = 10
time_limit = 30
skipped_questions = 0
correct = 0
def generate_problem():
    left = random.randint(operand1, operand2)
    right = random.randint(operand1, operand2)
    operator = random.choice(operators)

    expression = str(left) + " " + operator + " " + str(right)
    answer = eval(expression)

    return expression, answer

input("Press Enter to start! "
      "\nRemember! You have 30 seconds to complete the test.")
print("----------------------")

start_time = time.time()

for i in range(total_questions):
    expression, answer = generate_problem()
    while True:
        problem = input("Problem #" + str(i+1) + ": " + expression + " = ")

        if problem == 's' or problem == 'skip' or problem == 'S':
            skipped_questions += 1
            break

        if problem == str(answer):
            correct += 1
            break


end_time = time.time()

total_time = round(end_time - start_time, 2)
print("Total Questions: ", total_questions,
      "\nCorrect Questions: ", correct, "/", total_questions,
      "\nSkipped Questions: ", skipped_questions,
      "\nTime Limit: ", time_limit, "seconds",
      "\nTime Taken: ", total_time, "seconds")




