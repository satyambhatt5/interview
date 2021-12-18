#find the occourance in the list of the given number
ls=[10,30,40,50,50,40,30,10]
def count_occurrence(list, n):
    #counter variable
    count=0
    for i in list:
        if(i==n):
          #update counter variable
            count=count+1
    return count
print(count_occurrence(ls,50))

#occurrences in list
#count()
#second method
#input list
li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)
print("Original list: ",li)

n=int(input("Enter element to be checked list: "))

#using count()
print(n," has occurred ",li.count(n),"times")





