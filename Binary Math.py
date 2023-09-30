# Title: Binary Math
# Description: A program with various simple binary operations
# Author: Nathan Walker
# Version: 2.5
# Date: 9-27-23

# Import
import time

# Color definitions
BLACK = "\u001b[30m"
RED = "\u001b[31m"
GREEN = "\u001b[32m"
YELLOW = "\u001b[33m"
BLUE = "\u001b[34m"
MAGENTA = "\u001b[35m"
CYAN = "\u001b[36m"
WHITE = "\u001b[37m"
RESET = "\u001b[0m"

# Static variable definitions
LINE = "**     "


# ***METHOD DEFINITIONS***

# Header text method
def header():
    print(RESET + "\n\n            ****   Binary Math Program   ****\n\n")
    print("                                     (c) Walker Tech inc.")


# Menu text method
def menu():
    print(BLUE + "*********************************************************\n")
    print(WHITE + "                       Main Menu                         \n")
    print(BLUE + "*********************************************************")
    print(BLUE + LINE)
    print(BLUE + LINE + YELLOW + "[1]" + CYAN + " Find one's complement of a number")
    print(BLUE + LINE + YELLOW + "[2]" + CYAN + " Find two's complement of a number")
    print(BLUE + LINE + YELLOW + "[3]" + CYAN + " Add numbers")
    print(BLUE + LINE + YELLOW + "[4]" + CYAN + " Developer menu")
    print(BLUE + LINE + YELLOW + "[0]" + CYAN + " Exit program")
    print(BLUE + LINE)
    print(BLUE + "*********************************************************\n" + RESET)


# Find one's complement of a binary number
def one():
    # Input
    number = str(input(YELLOW + "Enter a binary number: " + RED))

    # Flip each digit
    newNumber = ""
    for x in number:
        if x == "0":
            newNumber = newNumber + "1"
        if x == "1":
            newNumber = newNumber + "0"

    # print
    print(GREEN + "\nYour new number is: " + MAGENTA + newNumber + WHITE)


# Find two's complement of a binary number
def two():
    # Input
    number = str(input(YELLOW + "Enter a binary number: " + RED))

    # Flip each Digit
    newNumber = ""
    for x in number:
        if x == "0":
            newNumber = newNumber + "1"
        if x == "1":
            newNumber = newNumber + "0"
    
    # Add one
    newNumber = (add_two(newNumber, normalize("1", len(newNumber)), 2))

    # Print
    print(GREEN + "\nYour new number is: " + MAGENTA + newNumber + WHITE)


# Addition main method
def add():
    # Variables
    numbers = []
    number = "temp"
    
    # Take input
    complement = input(YELLOW + "One's complement (1), or two's complement (2): " + RED)
    numbers.append(str(input(YELLOW + "Enter a number: " + RED)))
    while number != "":
        number = str(input(YELLOW + "Enter another number or hit enter to continue: " + RED))
        numbers.append(number)
    print(GREEN + "\nAnswer: " + MAGENTA + add_many(numbers, complement) + WHITE)


# IN DEVELOPMENT Multiplication main method
def multiply():
    # Variables
    numbers = []

    # Input
    number1 = str(input(YELLOW + "Enter your first number: " + RED))
    number2 = str(input(YELLOW + "Enter your second number number: " + RED))

    # Main loop
    for x in range(len(number2)):
        # Add a variable that allows going through strings backwards
        y = len(number2) - x - 1

        # Add zeroes to the end
        if number2[y] == 1:
            temp = number1
            for z in range(y):
                temp = temp + "0"
            numbers.append(temp)
    
    # Add numbers and print
    print(GREEN + "\nAnswer: " + MAGENTA + add_many(numbers, "M") + WHITE)
    
   
# Add two binary numbers
def add_two(numOne, numTwo, complement):
    # Variables
    buffer = "0"
    answer = ""
    
    # Normalize lengths (if not the same)
    if (len(numOne) < len(numTwo)):
        numOne = normalize(numOne, len(numTwo))
    if (len(numTwo) < len(numOne)):
        numTwo = normalize(numTwo, len(numOne))

    # Main loop
    for x in range(len(numOne)):
        # Add a variable that allows going through strings backwards
        y = len(numOne) - x - 1

        # Take sum of digits in two numbers and buffer
        total = int(numOne[y]) + int(numTwo[y]) + int(buffer[x])
        # If 0, zero in answer and no carry
        if total == 0:
            answer = "0" + answer
            buffer = buffer + "0"
        # If 1, one in answer and no carry
        elif total == 1:
            answer = "1" + answer
            buffer = buffer + "0"
        # If 2, zero in answer and carry one
        elif total == 2:
            answer = "0" + answer
            buffer = buffer + "1"
        # If 3, one in answer and carry one
        elif total == 3:
            answer = "1" + answer
            buffer = buffer + "1"
    
    # Carry handling for each complement
    if buffer[len(numOne)] == "1" and complement == "1":
        return add_two(answer, normalize("1", len(answer)), 1)
    elif buffer[len(numOne)] == "1" and complement == "M":
        return "1" + answer
    else:
        return answer


# Add a list of numbers
def add_many(numbers, complement):
    total = add_two(numbers[0], numbers[1], complement)
    i = 2
    while i<len(numbers):
        total = add_two(total, numbers[i], complement)
        i = i+1
    return total

  
# Additional sub-method to normalize a number to a given length by adding zeros
def normalize(number, length):
    while len(number) < length:
        number = "0" + number
    return number


# Color Menu        
def color_menu():
    print("Color Menu")
    print("[1] Black")
    print("[2] Red")
    print("[3] Green")
    print("[4] Blue")
    print("[5] Magenta")
    print("[6] Cyan")
    print("[7] White")
    selection = input(YELLOW + "Select a menu option: " + RED)
    print(WHITE + "\n\n")
    if selection == "1":
        print(BLACK)
        exit()
    elif selection == "2":
        print(RED)
        exit()
    elif selection == "3":
        print(GREEN)
        exit()
    elif selection == "4":
        print(BLUE)
        exit()
    elif selection == "5":
        print(MAGENTA)
        exit()
    elif selection == "6":
        print(CYAN)
        exit()
    elif selection == "7":
        print(WHITE)
        exit()  


# Dev menu
def dev_menu():
    newLine = "\n \n \n"
    while (True):
        print("      ****  Developer Menu   ****")
        print("Please note that these features are temporary and/or developmental, so don't expect them to work!")
        print("Also sorry no color but this is dev menu so deal with it")
        print("[1] Normalize binary number")
        print("[2] Color Menu")
        print("[3] Multiply two numbers")
        print("[0] Return to previous menu\n")
        selection = input("Select and option: ")
        print("\n")
        if selection == "1":
            number = str(input("Enter a number: "))
            length = int(input("Enter a length: "))
            print(normalize(number, length))
            print(newLine)
        elif selection == "2":
            color_menu()
        elif selection == "3":
            multiply()
            print(newLine)
        elif selection == "0":
            break
        else:
            print("invalid input" + newLine)



# MAIN METHOD
newLine = "\n \n \n"
header()
while (True):
    menu()
    selection = input(YELLOW + "Select a menu option: " + RED)
    print(RESET + "\n")
    if selection == "1":
        one()
        print(newLine)
    elif selection == "2":
        two()
        print(newLine)
    elif selection == "3":
        add()
        print(newLine)
    elif selection == "4":
        dev_menu()
        print(newLine)
    elif selection == "0":
        break
    else:
        print("invalid input" + newLine)
    
print(GREEN + "\n\nQuitting....\n")
print(GREEN + "Thanks for using my program!\n\n" + BLUE + "-N" + RESET)
time.sleep(1)