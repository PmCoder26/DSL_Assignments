# Assignment-2.
"""
    Write a python program to compute following computation on matrix:
        a) Addition of two matrices.
        b) Subtraction of two matrices.
        c) Multiplication of two matrices.
        d) Transpose of a matrix.
"""


def fact(n):
    if (n == 1):
        return 1
    else:
        return n * fact(n - 1)


def fibo(n):
    a = 0
    b = 1
    sum = 0
    if n == 1:
        print(a)
    elif n == 2:
        print(b)
    else:
        for i in range(0, n, 1):
            print(sum, end=" ")
            sum = a + b
            a = b
            b = sum


def printMat(mat):
    if mat != None:
        for i in mat:
            print(i)
    else:
        return


def addMat(mat1, mat2):
    if len(mat1[0]) != len(mat2)):  # checking the no.of rows and columns of both matrix
        print("Addition cannot be performed.")
    else:
        mat3 = []
        for i in range(0, len(mat1)):
            subMat1 = []
            for j in range(0, len(mat1[0])):
                subMat1.append(mat1[i][j] + mat2[i][j])
            mat3.append(subMat1)
        return mat3


def subMat(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):  # checking the no.of rows and columns of both matrix
        print("Subtraction cannot be performed.")
    else:
        mat3 = []
        for i in range(0, len(mat1)):
            subMat2 = []
            for j in range(0, len(mat1[0])):
                subMat2.append(mat1[i][j] - mat2[i][j])
            mat3.append(subMat2)
        return mat3


def createMat(mat):
    row = int(input("Enter no.of rows: "))
    col = int(input("Enter no.of columns: "))
    for i in range(0, row):
        subMat1 = []
        for j in range(0, col):
            subMat1.append(int(input("Enter number: ")))
        mat.append(subMat1)
        print()
    return mat


def multiUtil(mat1, mat2, i, j):
    prd = 0
    for k in range(0, len(mat1)):
        prd += mat1[i][k] * mat2[k][j]
    return prd


def multiMat(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        print("Multiplication cannot be performed.")
    else:
        mat3 = []
        for i in range(0, len(mat1)):
            subMat3 = []
            for j in range(0, len(mat1[0])):
                subMat3.append(multiUtil(mat1, mat2, i, j))
            mat3.append(subMat3)
        return mat3


def transpose(mat):
    if len(mat) != len(mat[0]):
        print("Transpose cannot be calculated.")
    else:
        for i in range(0, int(len(mat) / 2)):
            for j in range(0, len(mat[0])):
                if (i != j):
                    temp = mat[i][j]
                    mat[i][j] = mat[j][i]
                    mat[j][i] = temp
                else:
                    continue
        return mat


# -------------------------------------------------->


# #	Printing fibonacci series terms till nth term
# n=int(input("Enter the no. of terms of fibonacci series that you want to print: "))
# fibo(n)
# print("Thankyou!!!")

# # Calculating and printing the factorial of n.
# n=int(input("Enter the value of n: "))
# print("The factorial of", n, "is", fact(n))	

# Adding two matrix.
mat1 = []
mat2 = []
print("Inputs for matrix 1")
mat1 = createMat(mat1)
print("Inputs for matrix 2")
mat2 = createMat(mat2)
mat3 = addMat(mat1, mat2)
mat4 = subMat(mat1, mat2)
mat5 = multiMat(mat1, mat2)

print("Addition of two matrices is: ")
printMat(mat3)
print("Subtraction of two matrices is: ")
printMat(mat4)

print("Multiplication of two matrix is: ")
printMat(mat5)

print("The transpose of the mat1 is: ")
printMat(transpose(mat1))