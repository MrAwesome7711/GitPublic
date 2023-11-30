# Title: Orthogonal Basis Calculator
# Description: A process to compute a basis that is orthogonal to a given basis using the Gram-Schmidt process
# Author: Nathan Walker
# Version: 3.2
# Date: 11-28-23

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

# Subscript definitions
def sub(number):
    if number == 0:
        return "\u2070"
    elif number == 1:
        return "\u00B9"
    elif number == 2:
        return "\u00B2"
    elif number == 3:
        return "\u00B3"
    elif number == 4:
        return "\u2074"
    elif number == 5:
        return "\u2075"
    elif number == 6:
        return "\u2076"
    elif number == 7:
        return "\u2077"
    elif number == 8:
        return "\u2078"
    elif number == 9:
        return "\u2079"


# ***METHOD DEFINITIONS***

# Convert Strings to floating point numbers
def str_to_int(stringList):
    floatList = []
    for x in range(len(stringList)):
        floatVector = [eval(i) for i in stringList[x]]
        floatList.append(floatVector)
    return floatList

# Dot product
def dot(vector1, vector2):
    answer = 0
    for x in range(len(vector1)):
        answer = answer + vector1[x] * vector2[x]
    return answer

# Orthogonal Projection of a vector v into a line spanned by a vector s
def proj(v,s):
    scalar = dot(v,s)/dot(s,s)
    vector = [x * scalar for x in s]
    return vector

# Normalize 
def normalize(vector):
    result = []
    total = 0
    for x in vector:
        total = total + x ** 2
    sqrtsum = total ** (1/2)
    for x in vector:
        result.append(x/sqrtsum)
    return result


# ***MAIN METHOD***

# Header
print(RESET + "\n                                        **Orthogonal Basis Calculator** \n\n" + CYAN + "version 3.2\n")

# Input and setup
vector1 = (input(YELLOW + "Enter the first vector in your basis with a space in between each number (for example, '1 2 3 4' without quotes): " + RED)).split()
basis_strings = []
vector2 = vector1
while vector2 != []:
    basis_strings.append(vector2)
    vector2 = (input(YELLOW + "Enter another vector or press enter to continue: " + RED)).split()
dec_place = eval(input(YELLOW + "Enter the number of decimal places to which your answers should be rounded: " + RED))
B = str_to_int(basis_strings)

# Compute orthogonal basis
K = [B[0]]
for x in range(1, len(B)):
    answer = B[x]
    for y in range(x):
        projected_vecor = proj(B[x], K[y-1])
        for z in range(len(answer)):
            answer[z] = answer[z] - projected_vecor[z]
    K.append(answer)

# Round and output orthogonal basis
K_Rounded = []
for x in K:
    templist = []
    for y in x:
        templist.append(round(y, dec_place))
    K_Rounded.append(templist)
print("\n")
print(GREEN + "Orthogonal Basis:" + MAGENTA)
for x in range(len(K_Rounded)):
    print("K"+ sub(x+1) + "=", K_Rounded[x])
print("\n" + RESET)

# Compute orthonormal basis
N = []
for x in K:
    N.append(normalize(x))

# Round and output orthonormal basis
N_Rounded = []
for x in N:
    templist = []
    for y in x:
        templist.append(round(y, dec_place))
    N_Rounded.append(templist)
print(GREEN + "Orthonormal Basis:" + MAGENTA)
for x in range(len(N_Rounded)):
    print("N"+ sub(x+1) + "=", N_Rounded[x])
print("\n" + RESET)

input(BLUE + "Press enter to quit" + RESET)


