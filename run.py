from random import randint

print("Welcome to the Math test!")

# Easy level addition, 
# After every question prints out is it was answered correct or inccorect
# At the end shows how musc score you have (how many answered Correct)
# When finnished gives user the option to select what it want to to
# after the test
def easy_level_addition():
    count = 0
    score = 0
    while (count <= 9):
        count += 1
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        easy_addition = num1 + num2
        answer = input(f'{num1} + {num2} \n')
        ans = int(answer)
        if ans == easy_addition:
            print('Correct')
            score += 1
        else:
            print('Inccorect')
    else:
        print('You got ' + str(score) + f' correct out of {count}!')
        option = input('What you want to do now? \n1)restart \n2)go back to easy level \n3)select difrent level \n4)back to main menu \n')
        if option == "1":
            easy_level_addition()
        if option == "2":
            easy_level()
        if option == "3":
            game_start()
        if option == "4":
            main()

# Easy level subtract
# After every question prints out is it was answered correct or inccorect
# At the end shows how musc score you have (how many answered Correct)
# When finnished gives user the option to select what it want to to
# after the test
def easy_level_subtract():
    count = 0
    score = 0
    while (count <= 9):
        count += 1
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        if (num1 > num2):
            easy_subtract = num1 - num2
            answer = input(f'{num1} - {num2} \n')
            ans = int(answer)
            if ans == easy_subtract:
                print('Correct')
                score += 1
            else:
                print('Inccorect')
        elif (num2 > num1):
            easy_subtract = num2 - num1
            answer = input(f'{num2} - {num1} \n')
            ans = int(answer)
            if ans == easy_subtract:
                print('Correct')
                score +=1
            else:
                print('Inccorect')
    else:
        print('You got ' + str(score) + f' correct out of {count} !')
        option = input('What you want to do now? \n1)restart \n2)go back to easy level \n3)select difrent level \n4)back to main menu \n')
        if option == "1":
            easy_level_subtract()
        if option == '2':
            easy_level()
        if option == '3':
            game_start()
        if option == '4':
            main()

# Easy level multiplication
# After every question prints out is it was answered correct or inccorect
# At the end shows how musc score you have (how many answered Correct)
# When finnished gives user the option to select what it want to to
# after the test
def easy_level_multiplication():
    count = 0
    score = 0
    while (count <= 9):
        count += 1
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        easy_multiplication = num1 * num2
        answer = input(f'{num1} * {num2} \n')
        ans = int(answer)
        if ans == easy_multiplication:
            print('Correct')
            score += 1
        else:
            print('Inccorect')
    else:
        print('You got ' + str(score) + f' correct out of {count}!')
        option = input('What you want to do now? \n1)restart \n2)go back to easy level \n3)select difrent level \n4)back to main menu \n')
        if option == '1':
            easy_level_multiplication()
        if option == '2':
            easy_level()
        if option == '3':
            game_start()
        if option == '4':
            main()

# Creating easy level division test
# After every question prints out is it was answered correct or inccorect
# At the end shows how musc score you have (how many answered Correct)
# When finnished gives user the option to select what it want to to
# after the test
def easy_level_division():
    count = 0
    score = 0
    while (count <= 9):
        count += 1
        num1 = randint(1, 10)
        num2 = randint(1, 10)

        if num1%num2 == 0:
            easy_division = num1 / num2
            answer = input(f'{num1} / {num2} \n')
            ans = int(answer)
            if ans == easy_division:
                print('Correct')
                score += 1
            else:
                print('Inccorect')
        if num2%num1 == 0:
            easy_division = num2 / num1
            answer = input(f'{num2} / {num1} \n')
            ans = int(answer)
            if ans == easy_division:
                print('Correct')
                score += 1
            else:
                print('Inccorect')
    else:
        print('You got ' + str(score) + f' correct out of {count}!')
        option = input('What you want to do now? \n1)restart \n2)go back to easy level \n3)select difrent level \n4)back to main menu \n')
        if option == '1':
            easy_level_division()
        if option == '2':
            easy_level()
        if option == '3':
            game_start()
        if option == '4':
            main()

# Starting medium level addition
# After every question prints out is it was answered correct or inccorect
# At the end shows how musc score you have (how many answered Correct)
# When finnished gives user the option to select what it want to to
# after the test
def medium_level_addition():
    count = 0
    score = 0
    while (count <= 9):
        count += 1
        num1 = randint(11, 100)
        num2 = randint(11, 100)
        medium_addition = num1 + num2
        answer = input(f'{num1} + {num2} \n')
        ans = int(answer)
        if ans == medium_addition:
            print('Correct')
            score += 1
        else:
            print('Inccorect')
    else:
        print('You got ' + str(score) + f' correct out of {count}!')
        option = input('What you want to do now? \n1)restart \n2)go back to easy level \n3)select difrent level \n4)back to main menu \n')
        if option == '1':
            medium_level_addition()
        if option == '2':
            medium_level()
        if option == '3':
            game_start()
        if option == '4':
            main()

# Starting medium level subtraction
# After every question prints out is it was answered correct or inccorect
# At the end shows how musc score you have (how many answered Correct)
# When finnished gives user the option to select what it want to to
# after the test
def medium_level_subtract():
    count = 0
    score = 0
    while (count <= 9):
        count += 1
        num1 = randint(11, 100)
        num2 = randint(11, 100)
        if (num1 > num2):
            medium_subtract = num1 - num2
            answer = input(f'{num1} - {num2} \n')
            ans = int(answer)
            if ans == medium_subtract:
                print('Correct')
                score += 1
            else:
                print('Inccorect')
        elif (num2 > num1):
            medium_subtract = num2 - num1
            answer = input(f'{num2} - {num1} \n')
            ans = int(answer)
            if ans == medium_subtract:
                print('Correct')
                score +=1
            else:
                print('Inccorect')
    else:
        print('You got ' + str(score) + f' correct out of {count} !')
        option = input('What you want to do now? \n1)restart \n2)go back to easy level \n3)select difrent level \n4)back to main menu \n')
        if option == '1':
            medium_level_subtract()
        if option == '2':
            medium_level()
        if option == '3':
            game_start()
        if option == '4':
            main()

# Starting medium level multiplication
# After every question prints out is it was answered correct or inccorect
# At the end shows how musc score you have (how many answered Correct)
# When finnished gives user the option to select what it want to to
# after the test
def medium_level_multiplication():
    count = 0
    score = 0
    while (count <= 9):
        count += 1
        num1 = randint(11, 100)
        num2 = randint(11, 100)
        medium_multiplication = num1 * num2
        answer = input(f'{num1} * {num2} \n')
        ans = int(answer)
        if ans == medium_multiplication:
            print('Correct')
            score += 1
        else:
            print('Inccorect')
    else:
        print('You got ' + str(score) + f' correct out of {count}!')
        option = input('What you want to do now? \n1)restart \n2)go back to easy level \n3)select difrent level \n4)back to main menu \n')
        if option == '1':
            medium_level_multiplication()
        if option == '2':
            medium_level()
        if option == '3':
            game_start()
        if option == '4':
            main()

# Starting medium level division
# After every question prints out is it was answered correct or inccorect
# At the end shows how musc score you have (how many answered Correct)
# When finnished gives user the option to select what it want to to
# after the test
def medium_level_division():
    count = 0
    score = 0
    while (count <= 9):
        count += 1
        num1 = randint(11, 100)
        num2 = randint(11, 100)

        if num1%num2 == 0:
            medium_division = num1 / num2
            answer = input(f'{num1} / {num2} \n')
            ans = int(answer)
            if ans == medium_division:
                print('Correct')
                score += 1
            else:
                print('Inccorect')
        if num2%num1 == 0:
            medium_division = num2 / num1
            answer = input(f'{num2} / {num1} \n')
            ans = int(answer)
            if ans == medium_division:
                print('Correct')
                score += 1
            else:
                print('Inccorect')
    else:
        print('You got ' + str(score) + f' correct out of {count}!')
        option = input('What you want to do now? \n1)restart \n2)go back to easy level \n3)select difrent level \n4)back to main menu \n')
        if option == '1':
            medium_level_division()
        if option == '2':
            medium_level()
        if option == '3':
            game_start()
        if option == '4':
            main()

# Asking user what the user wants to do in a medium level
# User can select one of the 4 choses 
def medium_level():
    medium_level_select = input("What would you like to do in this level? \nDivision \nMultiplication \nSubtract \nAddition \n")
    while medium_level_select not in ("division", "multiplication", "subtract", "addition"):
        break
    if medium_level_select.lower() == "division":
        print("You have selected medium level division")
        medium_level_division()
    if medium_level_select.lower() == "multiplication":
        print("You have selected medium level multiplication")
        medium_level_multiplication()
    if medium_level_select.lower() == "subtract":
        print("You have selected medium level subtract")
        medium_level_subtract()
    if medium_level_select.lower() == "addition":
        print("You have selected medium level addition")
        medium_level_addition()

# Creating what user want to do in a easy level
# User can select what it wants to do in this level
def easy_level():
    easy_level_select = input("What would you like to do in this level? \nDivision \nMultiplication \nSubtract \nAddition \n")
    while easy_level_select not in ("division", "multiplication", "subtract", "addition"):
        break
    if easy_level_select.lower() == "division":
        print("You have selected easy level division")
        easy_level_division()
    if easy_level_select.lower() == "multiplication":
        print("You have selected easy level multiplication")
        easy_level_multiplication()
    if easy_level_select.lower() == "subtract":
        print("You have selected easy level subtrat")
        easy_level_subtract()
    if easy_level_select.lower() == "addition":
        print("You have selected easy level addition")
        easy_level_addition()

# Checking what user has typed if it typed 1 or 2
# If user typed none of the option get an error message
def game_start():
        
        print("1) Level 1 (1 - 10)")
        print("2) Level 2 (11 - 100)")
        level = input("What level of Math quiz do you want to play? ")
        if level == "1":
            print("starting Easy level")
            easy_level()
        elif level == "2":
            print("Starting Medium level")
            medium_level()
        else:
            print("Wrong input. Please try again")
            game_start()



# Game rules
def game_rules():
    print("\nThis game lets you test you'r math knowledge")
    print("\nYou can select 1 of 2 difficulties" 
    "\nFirst one is numbers between 1 and 10."
    "\nSecond one is numbers between 11 and 100."
    "\nBy selecting difficulty then you can select what you want to do."
    "\nYou have 4 option"
    "\nAddition"
    "\nSubtraction"
    "\nMultiplication"
    "\nDivision\n")
    game_rules_input = input("Please select what you want to do know."
    "\n1) Go back."
    "\n2) Game Start"
    "\n3) Exit Game \n")
    if game_rules_input == "1":
        main()
    elif game_rules_input == "2":
        game_start()
    elif game_rules_input == "3":
        exit()
    else:
        print("Wrong input. Please try again.")
        game_rules()
    

# Asking user what they want to do read the rules or start the game
def main():
    print("1) Start the game")
    print("2) Game rules")
    print("3) Exit Game")
    game_beginning = input("Please select if you want to start the game or read the rules of the game. ")

    if game_beginning == "1":
        game_start()
    elif game_beginning == "2":
        game_rules()
    elif game_beginning == "3":
        exit()
    else:
        print("Wrong input. Please try again.")
        main()

main()

