# Assignment-2.
"""
    Write a python program to compute following computation on matrix:
        a) Addition of two matrices.
        b) Subtraction of two matrices.
        c) Multiplication of two matrices.
        d) Transpose of a matrix.
"""

# ------------------------------------------------------------------------------->

# Functions.

# function to print matrix.
def printMat(mat):
    # if matrix is not empty then printing the elements.
    if mat != None:
        # printing every element of mat.
        for i in mat:
            print(i)
    else:
        return


# function to create matrix.
def createMat(mat):
    # taking using input for no.of rows and columns.
    row = int(input("Enter no.of rows: "))
    col = int(input("Enter no.of columns: "))
    # iterating all the rows of matrix.
    for i in range(0, row):
        # creating sub-matrix to store elements for ith row of mat.
        subMat1 = []
        for j in range(0, col):
            # appending the elements for ith row.
            subMat1.append(int(input("Enter number: ")))
        # adding the sub-matrix as an element in mat(as a row of elements).
        mat.append(subMat1)
        print()
    return mat


# function to add two matrices.
def addMat(mat1, mat2):
    # checking the no.of rows and columns of both matrix
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        print("Addition cannot be performed.1")
    else:
        print("Addition of two matrices is: ")
        mat3 = []
        # iterating all the rows of the matrices.
        for i in range(0, len(mat1)):
            # creating the matrix to store the result of addition of two numbers for ith row.
            subMat1 = []
            # iterating all the columns of the matrices for ith row.
            for j in range(0, len(mat1[0])):
                # adding the numbers of two matrices of ith row and jth column and appending in subMat1.
                subMat1.append(mat1[i][j] + mat2[i][j])
            # appending the complete row of addition to mat3 as an element.
            mat3.append(subMat1)
        return mat3


# function to subtract two matrices.
def subMat(mat1, mat2):
    # checking the no.of rows and columns of both matrix
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        print("Subtraction cannot be performed.")
    else:
        print("Subtraction of two matrices is: ")
        mat3 = []
        # iterating all the rows of the matrices.
        for i in range(0, len(mat1)):
            # creating the matrix to store the result of subtraction of two numbers for ith row.
            subMat2 = []
            # iterating all the columns of the matrices for ith row.
            for j in range(0, len(mat1[0])):
                # subtracting the numbers of two matrices of ith row and jth column and appending in subMat2.
                subMat2.append(mat1[i][j] - mat2[i][j])
            # appending the complete row of subtraction to mat3 as an element.
            mat3.append(subMat2)
        return mat3


# function to perform operations on row of first matrix and column of second matrix..
def multiUtil(mat1, mat2, i, j):
    # creating the variable to store the result of the multiplication process.
    prd = 0
    # iterating all the columns of ith row of mat1 and all the rows of jth column of mat2.
    for k in range(0, len(mat1)):
        # multiplying the number of ith row and kth column of mat1 with kth row and jth
        # column of mat2 and finally adding their product to prd.
        prd += mat1[i][k] * mat2[k][j]
    return prd


# function to multiply two matrices.
def multiMat(mat1, mat2):
    if len(mat1[0]) != len(mat2):
        print("Multiplication cannot be performed.")
    else:
        print("Multiplication of two matrix is: ")
        mat3 = []
        # iterating all the rows of the matrices.
        for i in range(0, len(mat1)):
            # creating the matrix to store the result of multiplication of two numbers for ith row.
            subMat3 = []
            for j in range(0, len(mat2[0])):
                # multiplying the numbers of two matrices of ith row and jth column and appending in subMat3.
                # calling the multiUtil function to multiply.
                subMat3.append(multiUtil(mat1, mat2, i, j))
            # appending the complete row of multiplication to mat3 as an element.
            mat3.append(subMat3)
        return mat3


# function to find transpose of a matrix.
def transpose(mat):
    # if the no.of rows and no.of columns are not equal, hence we cant find transpose.
    if len(mat) != len(mat[0]):
        print("Transpose cannot be calculated.")
    else:
        print("The transpose of the mat is: ")
        # iterating the half the no.of rows of matrix so that twice swapping of numbers
        # can be prevented.
        for i in range(0, int(len(mat))):
            # iterating the columns of ith row.
            for j in range(0, len(mat[0])):
                # it prevents the diagonal elements for swapping as it results in no change.
                if i != j and i<j:
                    # performing the swapping operation.
                    temp = mat[i][j]
                    mat[i][j] = mat[j][i]
                    mat[j][i] = temp
                else:
                    continue
        return mat


# ------------------------------------------------------------------------------->


# Declaring and initializing two empty matrices.
mat1 = []
mat2 = []

print("Inputs for matrix 1")
mat1 = createMat(mat1)      # calling function to create matrix.

print("Inputs for matrix 2")
mat2 = createMat(mat2)      # calling function to create matrix.

mat3 = addMat(mat1, mat2)       # Addition of two matrices.
mat4 = subMat(mat1, mat2)       # Subtraction of two matrices.
mat5 = multiMat(mat1, mat2)     # Multiplication of two matrices.

printMat(mat3)      # Printing the result of addition of two matrices.

printMat(mat4)      # Printing the result of subtraction of two matrices.

printMat(mat5)      # Printing the result of multiplication of two matrices.

print("The transpose of matrix 1: ")
printMat(transpose(mat1))       # Transpose of matrix 1.
print("The transpose of matrix 2: ")
printMat(transpose(mat2))       # Transpose of matrix 2.

# ------------------------------------------------------------------------------->
