# Assignment_2.
"""
            Write a python program to compute following computation on matrix:
            a) Addition of two matrices
            b) Subtraction of two matrices
            c) Multiplication of two matrices
            d) Transpose of a matrix
"""


# Defining the functions.

def createMat(mat):
    mat1 = [[], [], []]
    for i in range(0, len(mat)):
        for j in range(0, len(mat)):
            mat1[i].append(int(input("Enter number: ")))
    return mat1


def addMat(mat1, mat2):
    mat3 = [[], [], []]
    for i in range(0, len(mat1)):
        for j in range(0, len(mat2)):
            mat3[i].append(mat1[i][j] + mat2[i][j])
    return mat3


def subMat(mat1, mat2):
    mat3 = [[], [], []]
    for i in range(0, len(mat1)):
        for j in range(0, len(mat2)):
            mat3[i].append(mat1[i][j] - mat2[i][j])
    return mat3


def multiUtil(mat1, mat2, x, y):
    product=0;
    for i in range(0, len(mat1)):
        product+=mat1[x][i]*mat2[i][y]
    return product


def multiMat(mat1, mat2):
    mat3=[[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
    for x in range(0, len(mat1)):
        for y in range(0, len(mat1)):
            mat3[x][y]=multiUtil(mat1, mat2, x, y)
    return mat3

def transpose(mat):
    for i in range(0, int(len(mat) / 2)):
        for j in range(0, len(mat)):
            if i != j:  # swapping the elements
                temp = mat1[i][j]
                mat[i][j] = mat[j][i]
                mat[j][i] = temp
    return mat


# ----------------------------------------------------------------------------->

# Main Logic.

mat1 = [[], [], []]
mat2 = [[], [], []]

mat1 = createMat(mat1)  # Creating matrix.
mat2 = createMat(mat2)  # Creating matrix.

print("Matrix 1:")  # Printing mat1
for i in mat1:
    print(i)

print("Matrix 2:")  # Printing mat2
for i in mat2:
    print(i)

mat3 = addMat(mat1, mat2)  # Adding two matrix.
mat4 = subMat(mat1, mat2)  # Subtracting two matrix.
mat5= multiMat(mat1, mat2)  # Multiplying two matrix.

mat6 = transpose(mat1)  # Calculating transpose of matrix
mat7 = transpose(mat2)  # Calculating transpose of matrix

print("Matrix after addition is: ")
for i in mat3:
    print(i)

print("Matrix after subtraction is: ")
for i in mat4:
    print(i)

print("Matrix after multiplication is: ")
for i in mat5:
    print(i)

print("Transpose of matrix 1 is: ")
for i in mat6:
    print(i)

print("Transpose of matrix 2 is: ")
for i in mat7:
    print(i)
