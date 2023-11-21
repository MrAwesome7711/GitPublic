# Title: Orthogonal Basis
# Description:
# Author: Nathan Walker
# Version: 1.0
# Date: 11-21-23
# ***METHOD DEFINITIONS***

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
    for y in x:
        K_Rounded.append(round(y, 3))
print("\n")
print(K_Rounded)
print("\n")

