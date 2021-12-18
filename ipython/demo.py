
#find the largest number in a list

ls=[1,23,4,5,6,7,8,9,10]

def larget_value(ls):
    max=ls[0]
    for i in ls:
        if i>max:
            max=i
    return max
print(larget_value(ls))


# *? find the smallest number in a list
def smallest_value(ls):
    min=ls[0]
    for i in ls:
        if i<min:
            min=i
    return min
print(smallest_value(ls))

#check if a number is in a list
def check_number(ls,num):
    for i in ls:
        if i==num:
            return True
    return False
print(check_number(ls,5))

#second mehtod 
#find the list of numbers that are divisible by 5
def divisible_by_5(ls):
    ls2=[]
    for i in ls:
        if i%5==0:
            ls2.append(i)
    return ls2
print(divisible_by_5(ls))








