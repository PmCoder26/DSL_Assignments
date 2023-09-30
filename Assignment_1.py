# Assignment-3.

"""
        In Second year Computer Engineering class of M students, set A of students play cricket and set B of students play
        badminton.
        Write python program to find and display-
            A. Set of students who play either cricket or badminton or both
            B. Set of students who play both cricket and badminton
            C. Set of students who play only cricket
            D. Set of students who play only badminton
            E. Number of students who play neither cricket nor badminton
"""


# -------------------------------------------------------------------------------------------------------------------------------------->

# -------------------------------------------------------------------------------------------------------------------------------------->
def createList(list):
    n = int(input("Enter the no.of students: "))
    for i in range(0, n):
        list.append(input("Name: "))
    return list


def rmDupli(list):
    list1 = []
    for i in range(0, len(list) - 1):
        for j in range(i + 1, len(list)):
            if (list[i] == list[j]):
                list[j] = -1
    for i in range(0, len(list)):
        if (list[i] != -1):
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


def onlyCkt(listA, listB):
    oC = []
    common = intersection(listA, listB)
    for i in listA:
        if isNotIn(common, i):
            oC.append(i)
        else:
            continue
    return oC


def onlyBdm(listA, listB):
    oB = []
    common = intersection(listA, listB)
    for i in listB:
        if isNotIn(common, i):
            oB.append(i)
        else:
            continue
    return oB


def nCnB(stList, listA, listB):
    ans = []
    allPlys = union(listA, listB)
    for i in stList:
        if isNotIn(allPlys, i):
            ans.append(i)
        else:
            continue
    return ans


# ------------------------------------------------------------------------------------------------------------------------------------>

# ------------------------------------------------------------------------------------------------------------------------------------>
stList = []  # Total no.of students.
listA = []  # Cricket players.
listB = []  # Badminton players.

# creating the lists of players and total students via user input.

print("Creating the list of total no.of students-")
stList = createList(stList)
print("Creating list of players playing Cricket-")
listA = createList(listA)
print("Creating list of players playing Badminton-")
listB = createList(listB)

# removing the duplicates if present in the list.
listA = rmDupli(listA)
listB = rmDupli(listB)

# printing the lists of players in their respective games.
print("The list of all students are: ", stList)
print("The lists of players are: ")
print("Cricket Players:", listA)
print("Badminton Players:", listB)

print("The students who play either cricket or badminton or both are:", union(listA, listB))
print("The students who play both cricket and badminton are:", intersection(listA, listB))
print("The students who play only cricket are: ", onlyCkt(listA, listB))
print("The students who play only cricket are: ", onlyBdm(listA, listB))
print("The students who play neither cricket nor badminton are: ", nCnB(stList, listA, listB))
# ------------------------------------------------------------------------------------------------------------------------------------>
