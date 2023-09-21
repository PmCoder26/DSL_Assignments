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

# Functions

# creating the lists of players.
def createList(list):
    n = int(input("Enter the no.of players: "))
    for i in range(0, n):
        list.append(input("Name: "))
    return list


# removing the duplicates from the list.
def rmDupli(list):
    list1=[]
    # loop for taking single player to compare with others.
    for i in range(0, len(list)-1):
        # comparing the single player with others in every main iteration.
        for j in range(i+1, len(list)):
            # if the specific player is the list for more than one times.
            if(list[i]==list[j]):
                # initilizing the specific value to that index so that duplicates's position can be identified.
                list[j]=-1
    # loop for finalizing the lists of non-repeating players.
    for i in range(0, len(list)):
        # for not -1, as it does not indicates the duplicate's postion, adding to final list.
        if(list[i]!=-1):
            list1.append(list[i]);
    return list1


# checking whether player present in the list.
def isIn(list, ply):
    # loop for iterating the player to whole list.
    for i in range(0, len(list)):
        # if player is in list then returning true and exit from loop.
        if ply == list[i]:
            return True
    else:
        return False


# checking whether player is not present in the list.
def isNotIn(list, ply):
    # loop for iterating single player to whole list.
    for i in range(0, len(list)):
        # if player is present in list retrun false.
        if (ply == list[i]):
            return False
    else:
        return True


# calculating union within two lists.
def union(list4, list5):
    list6 = []
    # loop for adding the players present in list4.
    for i in list4:
        list6.append(i)
    # now, loop for adding the players in list5.
    for i in range(0, len(list5)):
        # if players of list5 not present in list6, add them.
        if isNotIn(list6, list5[i]):
            list6.append(list5[i])
    return list6


# calculating intersection of two lists.
def intersection(list4, list5):
    list6 = []
    # loop for players in list4.
    for i in list4:
        # if player of list4 present in list5, adding him in final list.
        if isIn(list5, i):
            list6.append(i)
    return list6


# finding the players neither play cricket nor basketball.
def nCnB(list4, list5, list6):
    list7 = []
    # loop for iterating each player of list6.
    for i in range(0, len(list6)):
        # if the player of list6 is not present in list4 and list5, then adding to final list.
        if isNotIn(list4, list6[i]) and isNotIn(list5, list6[i]):
            list7.append(list6[i])
    return list7


# finding the players play football and cricket but not badminton.
def CAndFNotB(list1, list2, list3):
    # calculating the intersection of list1 and list3 and storing in list4.
    list4 = intersection(list1, list3)
    list5 = []
    # loop for iterating over each player of list4.
    for i in range(0, len(list4)):
        # if every player of list4 is not  present in list2 then adding it to final list.
        if isNotIn(list2, list4[i]):
            list5.append(list4[i])
    return list5

# ----------------------------------------------------------------------------------------------------------------------------->

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

# performing the operations on the given tasks.
print("The students who play either cricket or badminton but not both are:", union(listA, listB))
print("The students who play both cricket and badminton are:", intersection(listA, listB))
print("Students who play neither cricket nor badminton is:", (nCnB(listA, listB, listC)))
print("Number of students who play neither cricket nor badminton is:", len(nCnB(listA, listB, listC)))
print("Number of students who play cricket and football but not badminton is:", len(CAndFNotB(listA, listB, listC)))

