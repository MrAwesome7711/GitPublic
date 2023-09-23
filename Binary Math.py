# Title: Binary Math
# Description: A program with various simple binary operations
# Author: Nathan Walker
# Version: Beta 2.1
# Date: 9-23-23

# ***METHOD DEFINITIONS***


# menu text method
def menu():
    print("       ****   Main Menu   ****\n")
    print("[1] Find one's complement of a binary number")
    print("[2] Find two's complement of a binary number")
    print("[3] Add two numbers using one's complement")
    print("[4] Add two numbers using two's complement")
    print("[5] Developer menu")
    print("[0] Exit program\n")


# Find one's complement of a binary number
def ones():
    # Input
    number = str(input("Enter a binary number: "))

    # Flip each digit
    newNumber = ""
    for x in number:
        if x == "0":
            newNumber = newNumber + "1"
        if x == "1":
            newNumber = newNumber + "0"

    # print
    print("Your new number is: " + newNumber)


# Find two's complement of a binary number
def twos():
    # Input
    number = str(input("Enter a binary number: "))

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
    print("Your new number is: " + newNumber)



# Add two numbers using one's comlement
def oneAdd():
    # Take input
    numOne = str(input("Enter your first number: "))
    numTwo = str(input("Enter your second number: "))

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
        print("Answer: " + subAnswer)
    elif oneAddSub(numOne, numTwo, "buffer")[len(numOne)] == "0":
        print("Answer: " + subAnswer)


# Add two numbers using two's complement
def twoAdd():
    # Input
    numOne = str(input("Enter your first number: "))
    numTwo = str(input("Enter your second number: "))

    # Add
    subAnswer = oneAddSub(numOne, numTwo, "answer")

    # If there is a carry, add to start of answer; else, just print
    if oneAddSub(numOne, numTwo, "buffer")[len(numOne)] == "1":
        subAnswer = "1" + subAnswer
        print("Answer: " + subAnswer)
    elif oneAddSub(numOne, numTwo, "buffer")[len(numOne)] == "0":
        print("Answer: " + subAnswer)
      

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
        print("[1] normalize binary number")
        print("[2] Base binary addition method")
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
#        elif selection == "3":
#            print(newLine)
#        elif selection == "4":
#            print(newLine)
        elif selection == "0":
            break
        else:
            print("invalid input" + newLine)
        




# ****MAIN METHOD****
newLine = "\n \n \n"
print ("[****  WELCOME TO THE BINARY MATH PROGRAM!!!  ****]\n\n")
while (True):
    menu()
    selection = input("Select and option: ")
    print("\n")
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
    
print("Quitting....\n")
print("Thanks for using my program!\n-N")
