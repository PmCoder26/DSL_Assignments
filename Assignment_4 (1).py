"""
        Write a Python program to store first year percentage of students in array. Write
            function for sorting array of floating point numbers in ascending order using
            a) Selection Sort.
            b) Bubble sort and display top five scores.
"""
# ------------------------------------------------------------------------------------------------------------>

# Functions.


# Function to sort list using bubble sort in ascending order.
def bubbleSort(list):
    # Iteratig over the list.
    for i in range(0, len(list)-1):
        # Iterating over the list to compare numbers.
        for j in range(0, len(list)-1-i):
            # Comparing the jth element with j+1 th element. 
            if(list[j]>list[j+1]):      # swapping the elements.
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return list


# Function to sort list using selection sort in ascending order.
def selectionSort(list):
    # Iteratig over the list.
    for i in range(0, len(list)-1):
        # Initializing the idx to ith index to that it would neglect the sorted part.
        idx=i       
        # Traversing from the (i+1)th element.
        for j in range(i+1, len(list)):
            # updating the value of idx if smaller element exists than him.
            if(list[idx]>list[j]):
                idx=j
            else:
                continue
        # swapping the ith element and the smallest element for the respective part of list.
        temp=list[i]
        list[i]=list[idx]
        list[idx]=temp
    return list


# Function to create list of marks.
def createList(n):
    list=[]
    # loop to store the n no.of marks in list.
    for i in range(n):
        # addin marks to list.
        list.append(int(input("Enter marks: ")))
    return list


def get_best_5(list):
    # if the length of list is less than or equal to 5 that means print the whole list.
    if(len(list)<=5):
        # list to store all the marks in descending order.
        b_5=[]
        # iterating from the last element to 0th element.
        for i in range(len(list)-1, -1, -1):
            # adding element to top 5 list.
            b_5.append(list[i])
        # printing the list as top five scores.
        print("The top", len(list), "scores are:", b_5)
    else: 
        # list to store all the marks in descending order.
        b_5=[]
        # variable to fetch elements from last index.
        i=len(list)-1
        # variable to track the count of top 5 scores.
        cnt=0
        # adding the top five scores unless their count is less that 5.
        while(cnt<5):
            # adding the top 5 list.
            b_5.append(list[i])
            # increment in the count.
            cnt+=1
            # decrement in the index.
            i-=1
        # printing the top 5 list.
        print("Top 5 scores are:", b_5)
        
# ------------------------------------------------->


list=[]     # Declaring empty list.
# Taking the user input for total no.of students in class.
n=int(input("Enter no.of students: "))      # 
# Creating the list of marks by calling function.
list=createList(n)
print("List of marks:", list)   # Displaying list of marks.

# Sorting the list using bubble sort and displaying sorted list.
print("Sorted marklist using bubble sort is:", bubbleSort(list))
# Sorting the list using selection sort.
list=selectionSort(list)
# Displaying the sorted list.
print("Sorted marklist using selection sort is:", list)
# calling the function to find the top 5 scores. 
get_best_5(list)
