master_pass = input("What's the master password? ")

def create():
    account_name = input("Account Name: ")
    new_pass = input("Create New Password: ")

    with open('passwords.txt', 'a') as file:
        file.write(account_name + "|" + new_pass + "\n")

def view():
    with open('passwords.txt', 'r') as file:
        for line in file.readlines(): # used to read the lines of the existing file
            data = line.rstrip() # strip the extra line that comes bcz of \n
            user, passw = data.split("|") # splits the data wherever | comes into items of list
            print("Username:", user, ", Password:", passw)

while True:
    print("Would you like to create a new password or view existing ones? ")
    password = input("Create or View or Quit(q)? ").lower()
    if password == 'q' or password == 'quit':
        break

    if password == 'create':
        create()
    elif password == 'view':
        view()
    else:
        print("Invalid Option!")
        continue