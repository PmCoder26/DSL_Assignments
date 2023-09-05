# Assignment-1.

"""
    In second year computer engineering class, group A student’s play cricket, group B
    students play badminton and group C students play football.
    Write a Python program using functions to compute following: -
            a) List of students who play both cricket and badminton
            b) List of students who play either cricket or badminton but not both
            c) Number of students who play neither cricket nor badminton
            d) Number of students who play cricket and football but not badminton.
"""

def createList(list):
    n=int(input("Enter the no.of players: "))
    for i in range(0, n):
        list.append(input("Name: "))
    return list

def union(list4, list5):
    for i in range(0, len(list5)):
        if list5[i] not in list4:
            list4.append(list5[i])
    return list4


def intersection(list4, list5):
    list6 = []
    for i in range(0, len(list5)):
        if list5[i] in list4:
            list6.append(list5[i])
    return list6


def nCnB(list4, list5, list6):
    list7 = []
    for i in range(0, len(list6)):
        if list6[i] not in list4 and list6[i] not in list5:
            list7.append(list6[i])
    return list7


def CAndFNotB(list1, list2, list3):
    list4 = intersection(list1, list3)
    list5 = []
    for i in range(0, len(list4)):
        if list4[i] not in list2:
            list5.append(list4[i])
    return list5


listA = []  # Cricket players.
listB = []  # Badminton players.
listC = []  # Football players.

# creating the lists of players via user input.
print("Creating list of players playing Cricket-")
listA = createList(listA)
print("Creating list of players playing Badminton-")
listB = createList(listB)
print("Creating list of players playing Football-")
listC = createList(listC)

print("The students who play either cricket or badminton but not both are:", union(listA, listB))
print("The students who play both cricket and badminton are:", intersection(listA, listB))
print("Number of students who play neither cricket nor badminton is:", len(nCnB(listA, listB, listC)))
print(nCnB(listA, listB, listC))
print("Number of students who play cricket and football but not badminton is:", len(CAndFNotB(listA, listB, listC)))
