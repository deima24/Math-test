print("Welcome to the Math test!")

# Asking user what they want to do read the rules or start the game
print("1) Start the game")
print("2) Game rules")
game_beginning = input("Please select if you want to start the game or read the rules of the game. ")

# Checking what user has typed if it typed 1 or 2
def game_start():
        print("What level of Math quiz do you want to play? ")
        print("1) Level 1 (0 - 100)")
        print("2) Level 2 (100 - 1000)")

while game_beginning not in ("1", "2"):
    print("Select one of the two options:")
if game_beginning == "1":
    game_start()
elif game_beginning == "2":
    game_rules()