#Let's start by creating variables
print("Welcome to the Account-Registration Simulator!")
print("")
print("Please register below")
print("")

#No worries bro, classes are just the things working in the background, It won't get displayed in the console.
def create_an_account():
    name = input("Create an username: ")
    password = input("Create an password: ")

    #Never seen? That's basically the part in which you save the inputted values into the funktion "user" you just created. It's called a dictionary
    user1 = {
        'name' : name,
        'password' : password
    }
    return user1

user = create_an_account()

print(f"Account Created!: Information: Username: {user['name']}, Password: {user['password']}")


input("Press any key to end the program...")
