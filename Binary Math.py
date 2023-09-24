# Title: Binary Math
# Description: A program with various simple binary operations
# Author: Nathan Walker
# Version: Beta 3.1
# Date: 9-24-23



# Color Definitions
BLACK = "\u001b[30m"
RED = "\u001b[31m"
GREEN = "\u001b[32m"
YELLOW = "\u001b[33m"
BLUE = "\u001b[34m"
MAGENTA = "\u001b[35m"
CYAN = "\u001b[36m"
WHITE = "\u001b[37m"
RESET = "\u001b[0m"

# ***METHOD DEFINITIONS***

# Header text method
def header():
    print("\n\n       ****   Binary Math Program (Beta 3.1)   ****\n\n")
    print("                                     (c) Walker Tech inc.")

# menu text method
def menu():
    print(BLUE + "*********************************************************\n")
    print(WHITE + "                       Main Menu                         \n")
    print(BLUE + "*********************************************************")
    print(BLUE + "**")
    print(BLUE + "**     " + YELLOW + "[1]" + CYAN + " Find one's complement of a binary number")
    print(BLUE + "**     " + YELLOW + "[2]" + CYAN + " Find two's complement of a binary number")
    print(BLUE + "**     " + YELLOW + "[3]" + CYAN + " Add two numbers using one's complement")
    print(BLUE + "**     " + YELLOW + "[4]" + CYAN + " Add two numbers using two's complement")
    print(BLUE + "**     " + YELLOW + "[5]" + CYAN + " Developer menu")
    print(BLUE + "**     " + YELLOW + "[0]" + CYAN + " Exit program")
    print(BLUE + "**")
    print(BLUE + "*********************************************************\n" + RESET)


# Find one's complement of a binary number
def ones():
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
def twos():
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
    one = normalize("1", len(newNumber))
    newNumber = oneAddSub(newNumber, one, "answer")

    # Print
    print(GREEN + "\nYour new number is: " + MAGENTA + newNumber + WHITE)



# Add two numbers using one's comlement
def oneAdd():
    # Take input
    numOne = str(input(YELLOW + "Enter your first number: " + RED))
    numTwo = str(input(YELLOW + "Enter your second number: " + RED))

    # Normalize lengths (if not the same)
    if (len(numOne) < len(numTwo)):
        numOne = normalize(numOne, len(numTwo))
    if (len(numTwo) < len(numOne)):
        numTwo = normalize(numTwo, len(numOne))

    # Add
    subAnswer = oneAddSub(numOne, numTwo, "answer")

    # If there is a carry, add one and print; else, just print
    if oneAddSub(numOne, numTwo, "buffer")[len(numOne)] == "1":
        one = normalize("1", len(subAnswer))
        subAnswer = oneAddSub(subAnswer, one, "answer")
        print(GREEN + "\nAnswer: " + MAGENTA + subAnswer + WHITE)
    elif oneAddSub(numOne, numTwo, "buffer")[len(numOne)] == "0":
        print(GREEN + "\nAnswer: " + MAGENTA + subAnswer + WHITE)


# Add two numbers using two's complement
def twoAdd():
    # Input
    numOne = str(input(YELLOW + "Enter your first number: " + RED))
    numTwo = str(input(YELLOW + "Enter your second number: " + RED))

    # Add
    subAnswer = oneAddSub(numOne, numTwo, "answer")

    # If there is a carry, add to start of answer; else, just print
    if oneAddSub(numOne, numTwo, "buffer")[len(numOne)] == "1":
        subAnswer = "1" + subAnswer
        print(GREEN + "\nAnswer: " + MAGENTA + subAnswer + WHITE)
    elif oneAddSub(numOne, numTwo, "buffer")[len(numOne)] == "0":
        print(GREEN + "\nAnswer: " + MAGENTA + subAnswer + WHITE)
      

# Additional sub-method for actually adding numbers
def oneAddSub(numOne, numTwo, returnValue):
    # Variables
    buffer = "0"
    answer = ""

    # Main loop
    for x in range(len(numOne)):
        # Add a variable that allows going through strings backwards
        y = len(numOne) - x - 1

        # Take sum of digits in two numbers and buffer
        sum = int(numOne[y]) + int(numTwo[y]) + int(buffer[x])
        # if 0, zero in answer and no carry
        if sum == 0:
            answer = "0" + answer
            buffer = buffer + "0"
        # if 1, one in answer and no carry
        elif sum == 1:
            answer = "1" + answer
            buffer = buffer + "0"
        # if 2, zero in answer and carry one
        elif sum == 2:
            answer = "0" + answer
            buffer = buffer + "1"
        # if 3, one in answer and carry one
        elif sum == 3:
            answer = "1" + answer
            buffer = buffer + "1"
    
    # Method argument for returning either answer or buffer
    if returnValue == "answer":
        return answer
    elif returnValue == "buffer":
        return buffer
    

# Additional sub-method to normalize a number to a given length by adding zeros
def normalize(number, length):
    while len(number) < length:
        number = "0" + number
    return number
        

#Dev menu
def devMenu():
    newLine = "\n \n \n"
    while (True):
        print("      ****  Developer Menu   ****")
        print("Please note that these features are temporary and/or developmental, so don't expect them to work!")
        print("Also sorry no color but this is dev menu so deal with it")
        print("[1] normalize binary number")
        print("[2] Base binary addition method")
        print("[3] Color Menu")
        print("[0] Return to previous menu\n")
        selection = input("Select and option: ")
        print("\n")
        if selection == "1":
            number = str(input("Enter a number: "))
            length = int(input("Enter a length: "))
            print(normalize(number, length))
            print(newLine)
        elif selection == "2":
            number1 = str(input("Enter a number: "))
            number2 = str(input("Enter another number: "))
            argument1 = str(input("Do you want answer or buffer?: "))
            print("Answer: " + oneAddSub(number1, number2, argument1))
            print(newLine)
        elif selection == "3":
            colorMenu()
#        elif selection == "4":
#            print(newLine)
        elif selection == "0":
            break
        else:
            print("invalid input" + newLine)

# Color Menu        
def colorMenu():
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







# ****MAIN METHOD****
newLine = "\n \n \n"
header()
while (True):
    menu()
    selection = input(YELLOW + "Select a menu option: " + RED)
    print(RESET + "\n")
    if selection == "1":
        ones()
        print(newLine)
    elif selection == "2":
        twos()
        print(newLine)
    elif selection == "3":
        oneAdd()
        print(newLine)
    elif selection == "4":
        twoAdd()
        print(newLine)
    elif selection == "5":
        devMenu()
        print(newLine)
    elif selection == "0":
        break
    else:
        print("invalid input" + newLine)
    
print(GREEN + "\n\nQuitting....\n")
print(GREEN + "Thanks for using my program!\n\n" + BLUE + "-N" + RESET)
