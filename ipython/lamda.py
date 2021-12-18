#using the lamda function to create a function

a = lambda x,y : x+y
print(a(5, 6))

x=['ab','cd']
print(list(map(lambda x:x.upper(),x)))
print(list(map(lambda x:x.split(),x)))

#givn a list of numbers and a number, return the count of the numbers greater than the given number
ls = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x: x > 5, ls)))

#find the value of the list
ls = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x: x*x, ls)))











