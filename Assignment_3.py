# Assignment-3
"""
		Write a Python program to store marks scored in subject “Fundamental of Data
		Structure” by N students in the class. Write functions to compute following:
			a) The average score of class
			b) Highest score and lowest score of class
			c) Count of students who were absent for the test
			d) Display mark with highest frequency
"""


def fillMarks():
	list=[]
	students=int(input("Enter the total no.of students in class: "))
	for i in range(0, students):
		print("Enter marks of student ", (i+1), ": ", end="")
		list.append(int(input()))
	return list

def avgMarks(list):
	absent=0
	sum=0
	for i in list:
		if(i==-1):
			absent+=1
		else:
			sum+=i		
	return sum/(len(list)-absent)
	
	
def absent(list):
	count=0
	for i in list:
		if(i==-1):
			count+=1
		else:
			continue
	return count	
	

def highScr(list):
	max=-1
	for i in list:
		if(i>max and i!=-1):
			max=i
		else:
			continue
	return max
	

def lowScr(list):
	min=101
	for i in list:
		if(i<min and i!=-1):
			min=i
		else:
			continue
	return min
	

def maxFreq(list):
	newList=[]
	eleList=[]
	freqList=[]
	for i in list:
		if(i!=-1):
			newList.append(i)
		else:
			continue
	while(len(newList)>0):
		ele=newList[0]
		eleList.append(ele)
		freq=1
		for i in range(1, len(newList)):
			if(ele==newList[i]):
				freq+=1
			else:
				continue
		freqList.append(freq)
		for i in newList:
			if(ele==i):
				newList.remove(i)
			else:
				continue
	print(freqList)
	print(eleList)
	max=-1
	idx=-1
	for i in range(0, len(freqList)):
		if(max<freqList[i]):
			max=freqList[i]
			idx=i
		else:
			continue
	return eleList[idx]
	
	
# ------------------------------------------------------------------------------->


stdMrks=[]
stdMarks=fillMarks()

print("The list of marks of all students is: ", stdMarks)

print("The average score of class is:", avgMarks(stdMarks))
print("The highest score of class is:", highScr(stdMarks))
print("The lowest score of class is:", lowScr(stdMarks))
print("The total no.of absent students for test are:", absent(stdMarks))
print("The marks with highest frequency is: ", maxFreq(stdMarks))




