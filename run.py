print("Welcome to the Math test!")

# Asking user what they want to do read the rules or start the game
print("1) Start the game")
print("2) Game rules")
game_beginning = int(input("Please select if you want to start the game or read the rules of the game. "))

# Checking what user has typed if it typed 1 or 2
if game_beginning != 1 and game_beginning != 2:
    print("Invalid choose. Please try again")
