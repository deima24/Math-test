from random import randint

print("Welcome to the Math test!")

# Asking user what they want to do read the rules or start the game
print("1) Start the game")
print("2) Game rules")
game_beginning = input("Please select if you want to start the game or read the rules of the game. ")
num1 = randint(1, 10)
num2 = randint(1, 10)

# Easy level multiplication
def easy_level_multiplication():
    easy_multiplication = num1 * num2
    answer = input(f'{num1} * {num2} \n')
    ans = int(answer)
    print('Correct' if ans == easy_multiplication else "Wrong")

# Creating easy level division test
def easy_level_division():
    num1%num2 == 0
    easy_division = num1 / num2 
    answer = input(f'{num1} / {num2} \n')
    ans = int(answer)
    print('Correct' if ans == easy_division else 'Wrong')


# Creating what user want to do in a easy level
def easy_level():
    easy_level_select = input("What would you like to do in this level? \nDivision \nMultiplication \nSubtract \nAddition \n")
    while easy_level_select not in ("division", "multiplication", "subtract", "addition"):
        break
    if easy_level_select == "division":
        print("You have selected easy level division")
        easy_level_division()
    if easy_level_select == "multiplication":
        easy_level_multiplication()
    if easy_level_select == "subtract":
        easy_level_subtract()
    if easy_level_select == "addition":
        easy_level_addition()

# Checking what user has typed if it typed 1 or 2
def game_start():
        
        print("1) Level 1 (0 - 10)")
        print("2) Level 2 (10 - 100)")
        level = int(input("What level of Math quiz do you want to play? "))
        if level == 1:
            print("starting easy level")
            easy_level()

while game_beginning not in ("1", "2"):
    print("Select one of the two options:")
if game_beginning == "1":
    game_start()
elif game_beginning == "2":
    game_rules()


