from random import randint

print("Welcome to the Math test!")

# Easy level addition
def easy_level_addition():
    count = 0
    score = 0
    while (count < 10):
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
        print('You got ' + str(score) + ' correct out of 10!')
        option = int(input('What you want to do now? \n1)restart \n2)go back to easy level \n3)select difrent level \n4)back to main menu \n'))
        if option == 1:
            easy_level_addition()
        if option == 2:
            easy_level()
        if option == 3:
            game_start()
        if option == 4:
            main()

# Easy level subtract
def easy_level_subtract():
    count = 0
    score = 0
    while (count < 10):
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
        option = int(input('What you want to do now? \n1)restart \n2)go back to easy level \n3)select difrent level \n4)back to main menu \n'))
        if option == 1:
            easy_level_subtract()
        if option == 2:
            easy_level()
        if option == 3:
            game_start()
        if option == 4:
            main()

# Easy level multiplication
def easy_level_multiplication():
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    easy_multiplication = num1 * num2
    answer = input(f'{num1} * {num2} \n')
    ans = int(answer)
    print('Correct' if ans == easy_multiplication else "Wrong")

# Creating easy level division test
def easy_level_division():
    while True:
        num1 = randint(1, 10)
        num2 = randint(1, 10)

        if num1%num2 == 0:
            easy_subtract = num1 / num2
            answer = input(f'{num1} / {num2} \n')
            ans = int(answer)
            print('Correct' if ans == easy_subtract else 'Wrong')
        elif num2%num1 == 0:
            easy_subtract = num2 / num1
            answer = input(f'{num2} / {num1} \n')
            ans = int(answer)
            print('Correct' if ans == easy_subtract else 'Wrong')
        if not answer:
            break


# Creating what user want to do in a easy level
def easy_level():
    easy_level_select = input("What would you like to do in this level? \nDivision \nMultiplication \nSubtract \nAddition \n")
    while easy_level_select not in ("division", "multiplication", "subtract", "addition"):
        break
    if easy_level_select.lower() == "division":
        print("You have selected easy level division")
        easy_level_division()
    if easy_level_select.lower() == "multiplication":
        easy_level_multiplication()
    if easy_level_select.lower() == "subtract":
        easy_level_subtract()
    if easy_level_select.lower() == "addition":
        easy_level_addition()

# Checking what user has typed if it typed 1 or 2
def game_start():
        
        print("1) Level 1 (1 - 10)")
        print("2) Level 2 (10 - 100)")
        level = int(input("What level of Math quiz do you want to play? "))
        if level == 1:
            print("starting easy level")
            easy_level()




# Asking user what they want to do read the rules or start the game
def main():
    print("1) Start the game")
    print("2) Game rules")
    game_beginning = input("Please select if you want to start the game or read the rules of the game. ")

    while game_beginning not in ("1", "2"):
        print("Select one of the two options:")
    if game_beginning == "1":
        game_start()
    elif game_beginning == "2":
        game_rules()

main()

