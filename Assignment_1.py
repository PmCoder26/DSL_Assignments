# Assignment - 1.
'''
        Question: In second year computer engineering class, group A student’s play cricket, group B students play badminton and group C students play football.
        Write a Python program using functions to compute following: -
            a)List of students who play both cricket and badminton
            b)List of students who play either cricket or badminton but not both
            c)Number of students who play neither cricket nor badminton
            d)Number of students who play cricket and football but not badminton.
'''


def union(list4, list5):  # Calculating the union of two lists.
    for i in range(0, len(list5)):
        if list5[i] not in list4:
            list4.append(list5[i])
    return list4


def intersection(list4, list5):  # Calculating the intersection of two lists.
    list6 = []
    for i in range(0, len(list5)):
        if list5[i] in list4:
            list6.append(list5[i])
    return list6


def nCnB(list4, list5, list6):  # Finding the players who neither play cricket nor badminton.
    list7 = []
    for i in range(0, len(list6)):
        if list6[i] not in list4 and list6[i] not in list5:
            list7.append(list6[i])
    return list7


def CAndFNotB(list1, list2, list3):  # Finding the players who play cricket adn football but not badminton.
    list4 = intersection(list1, list3)
    list5 = []
    for i in range(0, len(list4)):
        if list4[i] not in list2:
            list5.append(list4[i])
    return list5


# ---------------------------------------------------------------------------------------------------------------------------->

listA = ["P1", "P2", "P3", "P4", "P9", "P5"]  # Cricket players.
listB = ["P1", "P2", "P6", "P7", "P8", "P4"]  # Badminton players.
listC = ["P8", "P10", "P11", "P4", "P5"]  # Football players.

print("The students who play both cricket and badminton are:", intersection(listA, listB))
print("The students who play either cricket or badminton but not both are:", union(listA, listB))
print("The students who play neither cricket not badminton are:", nCnB(listA, listB, listC))
print("Number of students who play neither cricket nor badminton is:", len(nCnB(listA, listB, listC)))
print("The students who play cricket and football but not badminton is:", CAndFNotB(listA, listB, listC))
print("Number of students who play cricket and football but not badminton is:", len(CAndFNotB(listA, listB, listC)))
