from random import randint

WELCOME_MSG = """
Welcome to the Math test!
    1) Start the game
    2) Game rules
    3) Exit Game
"""

RESTART_MSG = """
What you want to do now?
    1)Restart
    2)Go back to easy level
    3)Select difrent level
    4)Back to main menu
    5)Else press any key to Exit
"""


def easy_level_addition():
    count = 0
    score = 0
    while count <= 9:
        count += 1
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        easy_addition = num1 + num2
        try:
            answer = input(f"{num1} + {num2} \n")
            ans = int(answer)
        except ValueError:
            print("Please enter a number!\n" f"Answer was {easy_addition}")
            continue
        if ans == easy_addition:
            print("Correct!")
            score += 1
        else:
            print("Inccorect!\n" f"Answer was {easy_addition}")
    else:
        print("You got " + str(score) + f" correct out of {count}!")
        option = input(RESTART_MSG)
        if option == "1":
            easy_level_addition()
        if option == "2":
            easy_level()
        if option == "3":
            game_start()
        if option == "4":
            main()
        else:
            exit()


# Easy level addition,
# After every question prints out is it was answered correct or inccorect
# If it was answered incorectly it will print out the correct answer
# At the end shows how much score you have (how many answered Correct)
# When finnished gives user the option to select what it want to do
# after the test
# If answer is left blank it will ask to enter a number


def easy_level_subtract():
    count = 0
    score = 0
    while count <= 9:
        count += 1
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        if num1 > num2:
            easy_subtract = num1 - num2
            try:
                answer = input(f"{num1} - {num2} \n")
                ans = int(answer)
            except ValueError:
                print("Please enter a number!\n" f"Answer was {easy_subtract}")
                continue
            if ans == easy_subtract:
                print("Correct!")
                score += 1
            else:
                print("Inccorect!\n" f"Answer was {easy_subtract}")
        if num2 > num1:
            easy_subtract = num2 - num1
            try:
                answer = input(f"{num2} - {num1} \n")
                ans = int(answer)
            except ValueError:
                print("Please enter a number!\n" f"Answer was {easy_subtract}")
                continue
            if ans == easy_subtract:
                print("Correct!")
                score += 1
            else:
                print("Inccorect!\n" f"Answer was {easy_subtract}")
    else:
        print("You got " + str(score) + f" correct out of {count} !")
        option = input(RESTART_MSG)
        if option == "1":
            easy_level_subtract()
        if option == "2":
            easy_level()
        if option == "3":
            game_start()
        if option == "4":
            main()
        else:
            exit()


# Easy level subtract
# After every question prints out is it was answered correct or inccorect
# At the end shows how much score you have (how many answered Correct)
# When finnished gives user the option to select what it want to do,
# after the test
# If the user answered inccorect , then the game shows the answer
# If left blank it will ask to enter a number
# Entering a letter it will also ask to enter a number


def easy_level_multiplication():
    count = 0
    score = 0
    while count <= 9:
        count += 1
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        easy_multiplication = num1 * num2
        try:
            answer = input(f"{num1} * {num2} \n")
            ans = int(answer)
        except ValueError:
            print("Please enter a number!\n"
            f"Answer was {easy_multiplication}")
            continue
        if ans == easy_multiplication:
            print("Correct!")
            score += 1
        else:
            print("Inccorect!\n" f"Answer was {easy_multiplication}")
    else:
        print("You got " + str(score) + f" correct out of {count}!")
        option = input(RESTART_MSG)
        if option == "1":
            easy_level_multiplication()
        if option == "2":
            easy_level()
        if option == "3":
            game_start()
        if option == "4":
            main()
        else:
            exit()


# Easy level multiplication
# After every question prints out is it was answered correct or inccorect
# At the end shows how much score you have (how many answered Correct)
# When finnished gives user the option to select what it want to do,
# after the test
# If the user answered inccorect , then the game shows the answer
# If left blank it will ask to enter a number
# Entering a letter it will also ask to enter a number

def division_operation(easy=True):
    """
    Asks users 10 division questions based on difficulty level.

    Args:
        easy (bool, optional): Whether to present easy or medium level
        difficulty questions. Defaults to True.
    """
    if easy:
        num1 = randint(1, 10)
        num2 = randint(1, 10)
    else:
        num1 = randint(11, 100)
        num2 = randint(11, 100)


def easy_level_division():
    count = 0
    score = 0
    while count <= 9:
        
        num1 = randint(1, 10)
        num2 = randint(1, 10)

        easy_division = None
        user_msg = None

        if num1 % num2 == 0:
            easy_division = num1 / num2
            user_msg = f"{num1} / {num2}"
            
        elif num2 % num1 == 0:
            easy_division = num2 / num1
            user_msg = f"{num2} / {num1}"
            
        if not easy_division:
            continue

        count += 1
        try:
            answer = input(user_msg)
            ans = int(answer)
        except ValueError:
            print("Please enter a number!\n" f"Answer was {easy_division}")
            continue
        if ans == easy_division:
            print("Correct!")
            score += 1
        else:
            print("Inccorect!\n" f"Answer was {easy_division}")

    else:
        print("You got " + str(score) + f" correct out of {count}!")
        option = input(RESTART_MSG)
        if option == "1":
            easy_level_division()
        if option == "2":
            easy_level()
        if option == "3":
            game_start()
        if option == "4":
            main()
        else:
            exit()


# Creating easy level division test
# After every question prints out is it was answered correct or inccorect
# At the end shows how much score you have (how many answered Correct)
# When finnished gives user the option to select what it want to do,
# after the test
# If the user answered inccorect , then the game shows the answer
# If left blank it will ask to enter a number
# Entering a letter it will also ask to enter a number


def medium_level_addition():
    count = 0
    score = 0
    while count <= 9:
        count += 1
        num1 = randint(11, 100)
        num2 = randint(11, 100)
        medium_addition = num1 + num2
        try:
            answer = input(f"{num1} + {num2} \n")
            ans = int(answer)
        except ValueError:
            print("Please enter a number!")
            continue
        if ans == medium_addition:
            print("Correct!")
            score += 1
        else:
            print("Inccorect!\n" f"Answer was {medium_addition}")
    else:
        print("You got " + str(score) + f" correct out of {count}!")
        option = input(
            """What you want to do now?
        1)Restart
        2)Go back to medium level
        3)Select difrent level
        4)Back to main menu
        5)Else press any key to Exit \n"""
        )
        if option == "1":
            medium_level_addition()
        if option == "2":
            medium_level()
        if option == "3":
            game_start()
        if option == "4":
            main()
        else:
            exit()


# Starting medium level addition
# After every question prints out is it was answered correct or inccorect
# At the end shows how much score you have (how many answered Correct)
# When finnished gives user the option to select what it want to do,
# after the test
# If the user answered inccorect , then the game shows the answer
# If left blank it will ask to enter a number
# Entering a letter it will also ask to enter a number


def medium_level_subtract():
    count = 0
    score = 0
    while count <= 9:
        count += 1
        num1 = randint(11, 100)
        num2 = randint(11, 100)
        if num1 > num2:
            medium_subtract = num1 - num2
            try:
                answer = input(f"{num1} - {num2} \n")
                ans = int(answer)
            except ValueError:
                print("Please enter a number!")
                continue
            if ans == medium_subtract:
                print("Correct!")
                score += 1
            else:
                print("Inccorect!\n" f"Answer was {medium_subtract}")
        if num2 > num1:
            medium_subtract = num2 - num1
            try:
                answer = input(f"{num2} - {num1} \n")
                ans = int(answer)
            except ValueError:
                print("Please enter a number!")
                continue
            if ans == medium_subtract:
                print("Correct!")
                score += 1
            else:
                print("Inccorect!\n" f"Answer was {medium_subtract}")
    else:
        print("You got " + str(score) + f" correct out of {count} !")
        option = input(
            """What you want to do now?
        1)Restart
        2)Go back to medium level
        3)Select difrent level
        4)Back to main menu
        5)Else press any key to Exit \n"""
        )
        if option == "1":
            medium_level_subtract()
        if option == "2":
            medium_level()
        if option == "3":
            game_start()
        if option == "4":
            main()
        else:
            exit()


# Starting medium level subtraction
# After every question prints out is it was answered correct or inccorect
# At the end shows how much score you have (how many answered Correct)
# When finnished gives user the option to select what it want to do,
# after the test
# If the user answered inccorect , then the game shows the answer
# If left blank it will ask to enter a number
# Entering a letter it will also ask to enter a number


def medium_level_multiplication():
    count = 0
    score = 0
    while count <= 9:
        count += 1
        num1 = randint(11, 100)
        num2 = randint(11, 100)
        medium_multiplication = num1 * num2
        try:
            answer = input(f"{num1} * {num2} \n")
            ans = int(answer)
        except ValueError:
            print("Please enter a number")
            continue
        if ans == medium_multiplication:
            print("Correct!")
            score += 1
        else:
            print("Inccorect!\n" f"Answer was {medium_multiplication}")
    else:
        print("You got " + str(score) + f" correct out of {count}!")
        option = input(
            """What you want to do now?
        1)Restart
        2)Go back to medium level
        3)Select difrent level
        4)Back to main menu
        5)Else press any key to Exit \n"""
        )
        if option == "1":
            medium_level_multiplication()
        if option == "2":
            medium_level()
        if option == "3":
            game_start()
        if option == "4":
            main()
        else:
            exit()


# Starting medium level multiplication
# After every question prints out is it was answered correct or inccorect
# At the end shows how much score you have (how many answered Correct)
# When finnished gives user the option to select what it want to do,
# after the test
# If the user answered inccorect , then the game shows the answer
# If left blank it will ask to enter a number
# Entering a letter it will also ask to enter a number


def medium_level_division():
    count = 0
    score = 0
    while count <= 9:
        count += 1
        num1 = randint(11, 100)
        num2 = randint(11, 100)

        if num1 % num2 == 0:
            medium_division = num1 / num2
            try:
                answer = input(f"{num1} / {num2} \n")
                ans = int(answer)
            except ValueError:
                print("Please enter a number!")
                continue
            if ans == medium_division:
                print("Correct!")
                score += 1
            else:
                print("Inccorect!\n" f"Answer was {medium_division}")
        if num2 % num1 == 0:
            medium_division = num2 / num1
            try:
                answer = input(f"{num2} / {num1} \n")
                ans = int(answer)
            except ValueError:
                print("Please enter a number!")
                continue
            if ans == medium_division:
                print("Correct!")
                score += 1
            else:
                print("Inccorect!\n" f"Answer was {medium_division}")
    else:
        print("You got " + str(score) + f" correct out of {count}!")
        option = input(
            """What you want to do now?
        1)Restart
        2)Go back to medium level
        3)Select difrent level
        4)Back to main menu
        5)Else press any key to Exit \n"""
        )
        if option == "1":
            medium_level_division()
        if option == "2":
            medium_level()
        if option == "3":
            game_start()
        if option == "4":
            main()
        else:
            exit()


# Starting medium level division
# After every question prints out is it was answered correct or inccorect
# At the end shows how much score you have (how many answered Correct)
# When finnished gives user the option to select what it want to do
# after the test
# If the user answered inccorect , then the game shows the answer
# If left blank it will ask to enter a number
# Entering a letter it will also ask to enter a number


def medium_level():
    medium_level_select = input(
        """What would you like to do in this level?
    Division
    Multiplication
    Subtract
    Addition
    Back \n"""
    ).lower()
    while medium_level_select not in (
        """division,
     multiplication,
     subtract,
     addition,
     back"""
    ):
        print("Wrong word. Try Again")
        medium_level()
    if medium_level_select.lower() == "division":
        print("You have selected medium level division")
        medium_level_division()
    elif medium_level_select.lower() == "multiplication":
        print("You have selected medium level multiplication")
        medium_level_multiplication()
    elif medium_level_select.lower() == "subtract":
        print("You have selected medium level subtract")
        medium_level_subtract()
    elif medium_level_select.lower() == "addition":
        print("You have selected medium level addition")
        medium_level_addition()
    elif medium_level_select.lower() == "back":
        game_start()


# Asking user what the user wants to do in a medium level
# User can select one of the 4 choses
# If left blank it will say wrong word
# Entering a number it will also ask to enter a word from the options
# You can enter in lower case, upper case or mixed
# the game will read it as lower case


def easy_level():
    easy_level_select = input(
        """What would you like to do in this level?
    Division
    Multiplication
    Subtract
    Addition
    Back\n"""
    ).lower()
    while easy_level_select not in (
        "division",
        "multiplication",
        "subtract",
        "addition",
        "back",
    ):
        print("Wrong word. Try Again")
        easy_level()
    if easy_level_select.lower() == "division":
        print("You have selected easy level division")
        easy_level_division()
    elif easy_level_select.lower() == "multiplication":
        print("You have selected easy level multiplication")
        easy_level_multiplication()
    elif easy_level_select.lower() == "subtract":
        print("You have selected easy level subtrat")
        easy_level_subtract()
    elif easy_level_select.lower() == "addition":
        print("You have selected easy level addition")
        easy_level_addition()
    elif easy_level_select.lower() == "back":
        game_start()


# Creating what user want to do in a easy level
# User can select what it wants to do in this level
# Entering a number it will also ask to enter a word from the options
# You can enter in lower case, upper case or mixed
# the game will read it as lower case


def game_start():
    while True:
        print("1) Level 1 (1 - 10)")
        print("2) Level 2 (11 - 100)")
        print("3) Go Back")
        level = input("What level of Math quiz do you want to play? ")
        if level == "1":
            print("starting Easy level")
            easy_level()
        elif level == "2":
            print("Starting Medium level")
            medium_level()
        elif level == "3":
            main()
        else:
            print("Wrong input. Please try again")
            game_start()


# Checking what user has typed if it typed 1, 2 or 3
# If user typed none of the option get an message wrong input
# If the user entered a letter or a number higher then 3
# it will come as wrong input and game will ask to enter it again
# If left blank you get the same wrong input


def game_rules():
    print("\nThis game lets you test you'r math knowledge")
    print(
        """\nYou can select 1 of 2 difficulties
    First one is numbers between 1 and 10.
    Second one is numbers between 11 and 100.
    By selecting difficulty then you can select what you want to do.
    You have 4 option
    Addition
    Subtraction
    Multiplication
    Division\n"""
    )
    


# Game rules
# Explanes the rules of the game and what user can do


def main():
    """
    Game rules
    Explains the rules of the game and what user can do.
    """
    while True:
        print(WELCOME_MSG)
        game_beginning = input(
            "Please select if you want to start "
            "the game or read the rules of the game. "
        )

        if game_beginning == "1":
            game_start()
        elif game_beginning == "2":
            game_rules()
        elif game_beginning == "3":
            exit()
        else:
            print("Wrong input. Please try again.")


# Asking user what they want to do read the rules or start the game
# If wrong input entered it will say wrong input and will ask again

if __name__ == "__main__":
    main()
