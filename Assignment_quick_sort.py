"""
    Write Python program to store first year percentage of students in array.
    Write function for sorting array of floating point numbers in ascending
    order using quick sort and display top five scores.

"""


# -------------------------------------------------------------------------------->
# Functions.

# function to create list.
def createList(list):
    # input the size of list.
    n = int(input("Enter the total no.of students in the class: "))
    for i in range(0, n):
        print("Enter the percentage of student ", (i + 1), ": ", end="")
        list.append(int(input()))
    return list


# function for the quick sort.
def quickSort(list, start, end):
    if (start >= end):
        return
    else:
        pvtIdx = partition(list, start, end)
        quickSort(list, start, pvtIdx - 1)
        quickSort(list, pvtIdx + 1, end)


# function for the partition of array.
def partition(list, start, end):
    # specially for the case if no element smaller than pivot exists.
    # Hence, the pivot will be placed at the first position.
    startIdx = start - 1
    for i in range(start, end):
        # if the ith element is smaller than the pivot then update its position.
        if (list[i] < list[end]):
            startIdx += 1
            # swapping that ith element with the smaller element than pivot.
            temp = list[i]
            list[i] = list[startIdx]
            list[startIdx] = temp
        else:
            continue
    # now repositioning the pivot element to its appropriate position.
    startIdx += 1
    temp = list[startIdx]
    list[startIdx] = list[end]
    list[end] = temp
    # returning the startIdx as the pivot index.
    return startIdx


# function to find the top five scores.
def topFive(list):
    if (len(list) == 0):
        return list
    else:
        # if the list contains 5 or less than 5 scores, hence they are only.
        # the top five.
        if (len(list) <= 5):
            newList = []
            # storing the elements in reverse/descending order.
            for i in range(0, len(list)):
                newList.append(list[len(list) - 1 - i])
            return newList
        else:
            newList = []
            for i in range(0, 5):
                newList.append(list[len(list) - 1 - i])
            return newList


# -------------------------------------------------------------------------------->

ans = 1
while (ans == 1):
    # creating the list.
    list = []
    list = createList(list)
    print("The score list is:", list)

    # sorting the list using the quick sort.
    print("The list before sorting is:", list)
    quickSort(list, 0, len(list) - 1)
    print("The list after sorting is:", list)

    # finding the top five scores.
    topFiveList = topFive(list)
    print("The top five scores are:", topFiveList)

    print("Do you want to continue the program?(Yes - 1, No - 2)")
    ans = int(input("Your response(1 or 2): "))
