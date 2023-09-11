# Assignment-2.
"""
    Write a python program to compute following computation on matrix:
        a) Addition of two matrices.
        b) Subtraction of two matrices.
        c) Multiplication of two matrices.
        d) Transpose of a matrix.
"""


def printMat(mat):
    if mat != None:
        for i in mat:
            print(i)
    else:
        return


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


def addMat(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):  # checking the no.of rows and columns of both matrix
        print("Addition cannot be performed.")
    else:
        print("Addition of two matrices is: ")
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
        print("Subtraction of two matrices is: ")
        mat3 = []
        for i in range(0, len(mat1)):
            subMat2 = []
            for j in range(0, len(mat1[0])):
                subMat2.append(mat1[i][j] - mat2[i][j])
            mat3.append(subMat2)
        return mat3


def multiUtil(mat1, mat2, i, j):
    prd = 0
    for k in range(0, len(mat1)):
        prd += mat1[i][k] * mat2[k][j]
    return prd


def multiMat(mat1, mat2):
    if len(mat1[0]) != len(mat2):
        print("Multiplication cannot be performed.")
    else:
        print("Multiplication of two matrix is: ")
        mat3 = []
        for i in range(0, len(mat1)):
            subMat3 = []
            for j in range(0, len(mat2[0])):
                subMat3.append(multiUtil(mat1, mat2, i, j))
            mat3.append(subMat3)
        return mat3


def transpose(mat):
    if len(mat) != len(mat[0]):
        print("Transpose cannot be calculated.")
    else:
        print("The transpose of the mat is: ")
        for i in range(0, int(len(mat) / 2)):
            for j in range(0, len(mat[0])):
                if i != j:
                    temp = mat[i][j]
                    mat[i][j] = mat[j][i]
                    mat[j][i] = temp
                else:
                    continue
        return mat


# ------------------------------------------------------------------------------->


# Adding two matrix.
mat1 = []
mat2 = []

print("Inputs for matrix 1")
mat1 = createMat(mat1)

print("Inputs for matrix 2")
mat2 = createMat(mat2)

mat3 = addMat(mat1, mat2)       # Addition of two matrices.
mat4 = subMat(mat1, mat2)       # Subtraction of two matrices.
mat5 = multiMat(mat1, mat2)     # Multiplication of two matrices.

printMat(mat3)      # Addition.

printMat(mat4)      # Subtraction.

printMat(mat5)      # Multiplication.

print("The transpose of matrix 1: ")
printMat(transpose(mat1))       # Transpose of matrix 1.
print("The transpose of matrix 2: ")
printMat(transpose(mat2))       # Transpose of matrix 2.
