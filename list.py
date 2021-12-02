list1 = [x for x in range(40, 200, 5)]
print(list1)
list2 = [51, 52, 53, 54, 55, 52, 57, 52, 59]

#remove the value if present in the list 
list2.remove(52)
print(list2)
#remove the value if it is not present in the list
#list2.remove(70)
#print(list2)
for i in list2:
     if i == 52:
         list2.remove(i)
print(list2)

list2 = [51, 52, 53, 54, 55, 52, 57, 52, 59]
#remove the all occurance of the value if present in the list
def removeoccur(list, n):
    for value in n:
        while value in list:
            list.remove(value)
    return list
print(removeoccur(list2, [52, 57]))



    






