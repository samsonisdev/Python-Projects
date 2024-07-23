import random
import string

def password_generator(min_length, numbers=True, special_char=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_char:
        characters += special

    password = ""
    has_numbers = False
    has_special = False
    meets_criteria = False

    while not meets_criteria or len(password) < min_length:
        char = random.choice(characters)
        password += char

        if char in digits:
            has_numbers = True
        elif char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_numbers
        if special_char:
            meets_criteria = has_special and meets_criteria

    return password

min = int(input("What should be the minimum length of password? "))
number = input("Should it include numbers (y/n)? ") == "y"
special = input("Should it include special characters (y/n)? ") == "y"

pwd = password_generator(min, number, special)
print("The generated password is: ", pwd)