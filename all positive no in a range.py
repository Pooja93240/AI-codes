#Python Program to print all positive number in range
def readlist():
    s=int(input("Enter the size of the list"))
    list=[]
    for i in range(1,s+1):
        n=float(input("enter"+str(i)+"element"))
        list.append(n)
    return(list)

def findpositive(list1,list2):
    for num in list1:
        if num>0:
            print (num)

    for num in list2:
        if num>0:
            print(num)
#Main Module
print("list 1")
l1=readlist()
print("list 2")
l2=readlist()

#Function call
findpositive(l1,l2)
