# Assignment-3
"""
		Write a Python program to store marks scored in subject “Fundamental of Data
		Structure” by N students in the class. Write functions to compute following:
                a) The average score of class.
                b) Highest score and lowest score of class.
                c) Count of students who were absent for the test.
                d) Display mark with the highest frequency.
"""

# ----------------------------------------------------------------------------------------->


# function to create/fill mark list of all students.
def fillMarks():
    # creating mark list.
    list = []
    # taking input for no.of students in class.
    students = int(input("Enter the total no.of students in class: "))
    # iterating for each student to fill list.
    for i in range(0, students):
        # taking user input to get marks of each student and appending to mark list.
        print("Enter marks of student ", (i + 1), ": ", end="")
        list.append(int(input()))
    return list


# function to calculate the average score of class.
def avgMarks(list):
    # creating variable to store no.of absent student.
    absent = 0
    # creating the variable to store the total sum of marks of all non-absent students.
    sum = 0
    # iterating over whole mark list to calculate sum.
    for i in list:
        # if marks[i] is -1 that means student was absent. Hence, increment in absent.
        if (i == -1):
            absent += 1
        else:
            # if student was not absent then considering its marks in sum.
            sum += i
    # calculating the actual average and return the result.
    return sum / (len(list) - absent)


# function to calculate the total no.of students absent for exam.
def absent(list):
    # declaring and initializing the count of absent students to 0.
    count = 0
    # iterating over whole mark list to calculate count.
    for i in list:
        # if list[i] is -1 that means student was absent. Hence, increment in count.
        if (i == -1):
            count += 1
        else:
            continue
    return count


# function to calculate the highest score of class.
def highScr(list):
    # initializing the max to calculate high score to -1 that is relevant minimum value.
    max = -1
    # iterating over whole list to find actual max.
    for i in list:
        # the previous max i.e. previous max score is less that the next score then updating
        # its value to current maximum score. Also checking whether student was absent or not.
        if (i > max and i != -1):
            max = i
        else:
            continue
    return max


# function to calculate the lowest score of class.
def lowScr(list):
    # initializing the min to 101 i.e. suitable value to compare with the marks of each student.
    min = 101
    # iterating over whole mark list to calculate actual min.
    for i in list:
        # the previous mix i.e. previous min score is greater that the next score then updating
        # its value to current minimum score. Also checking whether student was absent or not.
        if (i < min and i != -1):
            min = i
        else:
            continue
    return min


# function to calculate the maximum frequency of same marks scored.
def maxFreq(list):
    # creating new empty list to store marks without the marks of absent students.
    newList = []
    # creating the temporary list for some operations.
    eleList = []
    # creating the list to store the frequency of all different valued scores.
    freqList = []
    # iterating over list to fill the newList without the marks of absent students.
    for i in list:
        # if marks is -1 that means student was absent.
        if (i != -1):
            newList.append(i)
        else:
            continue
    # iterating the prcess below inside while loop unless the newList is empty.
    while (len(newList) > 0):
        # storing the first element of newList.
        ele = newList[0]
        # appending the first element to eleList.
        eleList.append(ele)
        # initializing the frequency to 1 as the element is counted before.
        freq = 1
        # iterating the whole newList from the second element as it was counted previously.
        for i in range(1, len(newList)):
            # if the ele is equal to ith element then increment in freq.
            if (ele == newList[i]):
                freq += 1
            else:
                continue
        # adding the final frequency (freq) of the element to the freqList.
        freqList.append(freq)
        # now iterating the newList to remove all the copies of the element from the newList,
        # so that next time other element will be the first and above operations will be performed for it.
        for i in newList:
            # if ele is equal to newList[i] then remove newList[i].
            if (ele == i):
                newList.remove(i)
            else:
                continue
    print("The list of unique marks is:", eleList)
    print("The list of respective frequencies is:", freqList)
    max = -1
    idx = -1        # variable to store the index of the maximum frequency.
    # iterating over the whole freqList.
    for i in range(0, len(freqList)):
        # if the current max is less than the freqList[i], then updating the current max and updating the idx.
        if (max < freqList[i]):
            max = freqList[i]
            idx = i
        else:
            continue
    # returning the element with the highest frequency.
    return eleList[idx]


# ------------------------------------------------------------------------------->


# creating list of student marks.
stdMrks = []
# adding/filling the marks of all students by calling fillMarks().
stdMarks = fillMarks()

# printing the list of marks of all students.
print("The list of marks of all students is: ", stdMarks)

# calculating and printing the average score of the class.
print("The average score of class is:", avgMarks(stdMarks))
# calculating and printing the highest score of the class.
print("The highest score of class is:", highScr(stdMarks))
# calculating and printing the lowest score of the class.
print("The lowest score of class is:", lowScr(stdMarks))
# calculating and printing the no.of absent students.
print("The total no.of absent students for test are:", absent(stdMarks))
# calculating and printing the maximum frequency of same marks scored by students.
print("The marks with highest frequency is: ", maxFreq(stdMarks))

# ------------------------------------------------------------------------------->
