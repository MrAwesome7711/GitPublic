# Title: Orthogonal Basis
# Description: A process to compute a basis that is orthogonal to a given basis
# Author: Nathan Walker
# Version: 1.1
# Date: 11-21-23
# ***METHOD DEFINITIONS***

# subscripts
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

# Convert Strings to Floating point numbers
def str_to_int(stringList):
    floatList = []
    for x in range(len(stringList)):
        floatVector = [eval(i) for i in stringList[x]]
        floatList.append(floatVector)
    return floatList

# Dot Product
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


# ***MAIN METHOD***
# Input and setup
vector1 = (input("Enter your first vector in your basis with the form with spaces between the numbers (for example, '1 2 3 4' without quotes): ")).split()
basis_strings = []
vector2 = vector1
while vector2 != []:
    basis_strings.append(vector2)
    vector2 = (input("Enter another vector or just press enter to continue: ")).split()
B = str_to_int(basis_strings)
#B_Rounded = []
#for x in B:
#    for y in x:
#        B_Rounded.append(round(y, 3))

# Find elements of K
K = [B[0]]
for x in range(1, len(B)):
    answer = B[x]
    for y in range(x):
        projected_vecor = proj(B[x], K[y-1])
        for z in range(len(answer)):
            answer[z] = answer[z] - projected_vecor[z]
    K.append(answer)

# Round and output
K_Rounded = []
for x in K:
    templist = []
    for y in x:
        templist.append(round(y, 3))
    K_Rounded.append(templist)
print("\n")
print("Orthogonal Basis:")
for x in range(len(K_Rounded)):
    print("K"+ sub(x+1) + "=", K_Rounded[x])
print("\n")

