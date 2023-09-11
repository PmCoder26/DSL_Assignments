# Assignment-1.

"""
    In second year computer engineering class, group A student’s play cricket, group B
    students play badminton and group C students play football.
    Write a Python program using functions to compute following: -
            a) List of students who play both cricket and badminton
            b) List of students who play either cricket or badminton but not both
            c) Number of students who play neither cricket nor badminton
            d) Number of students who play cricket and football but not badminton.
    (Note - While realizing the group, duplicate entries should be avoided. Do not use built-in functions)
"""


def createList(list):
    n = int(input("Enter the no.of players: "))
    for i in range(0, n):
        list.append(input("Name: "))
    return list


def rmDupli(list):
    list1=[]
    for i in range(0, len(list)-1):
        for j in range(i+1, len(list)):
            if(list[i]==list[j]):
                list[j]=-1
    for i in range(0, len(list)):
        if(list[i]!=-1):
            list1.append(list[i]);
    return list1


def isIn(list, ply):
    for i in range(0, len(list)):
        if ply == list[i]:
            return True
    else:
        return False


def isNotIn(list, ply):
    for i in range(0, len(list)):
        if (ply == list[i]):
            return False
    else:
        return True


def union(list4, list5):
    list6 = []
    for i in list4:
        list6.append(i)
    for i in range(0, len(list5)):
        if isNotIn(list6, list5[i]):
            list6.append(list5[i])
    return list6


def intersection(list4, list5):
    list6 = []
    for i in list4:
        if isIn(list5, i):
            list6.append(i)
    return list6


def nCnB(list4, list5, list6):
    list7 = []
    for i in range(0, len(list6)):
        if isNotIn(list4, list6[i]) and isNotIn(list5, list6[i]):
            list7.append(list6[i])
    return list7


def CAndFNotB(list1, list2, list3):
    list4 = intersection(list1, list3)
    list5 = []
    for i in range(0, len(list4)):
        if isNotIn(list2, list4[i]):
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

# removing the duplicates if present in the list.
listA=rmDupli(listA)
listB=rmDupli(listB)
listC=rmDupli(listC)

# printing the lists of players in their respective games.
print("The lists of players are: ")
print("Cricket Players:", listA)
print("Badminton Players:", listB)
print("Football Players:", listC)

print("The students who play either cricket or badminton but not both are:", union(listA, listB))
print("The students who play both cricket and badminton are:", intersection(listA, listB))
print("Students who play neither cricket nor badminton is:", (nCnB(listA, listB, listC)))
print("Number of students who play neither cricket nor badminton is:", len(nCnB(listA, listB, listC)))
print("Number of students who play cricket and football but not badminton is:", len(CAndFNotB(listA, listB, listC)))

