#second largest value 
def findLargest(arr):
	secondLargest = arr[0]
	largest = arr[0]
	for i in range(len(arr)):
		if arr[i] > largest:
			largest = arr[i]

	for i in range(len(arr)):
		if arr[i] > secondLargest and arr[i] != largest:
			secondLargest = arr[i]

	return secondLargest
print(findLargest([10, 20, 4, 45, 99]))

#second method
numbers =[10, 20, 30, 40, 50, 60, 70, 80, 1, 15, 45, 60, 50, 30, 40, 20, 40, 60, 30, 78]

def find_second_largest(arr):
    first, second = 0, 0

    for number in arr:
        if number > first:
            second = first
            first = number
        elif number > second and number < first:
            second = number

    return second
print(find_second_largest(arr=numbers))

#third ways
def secondLargest(lst):
    mx = 0
    num = 0
    sec = 0
    for i in lst:
        if i > mx:
            sec = mx
            mx = i
        else:
            if i > num and num <= sec:
                sec = i
            num = i
    return sec
print(secondLargest(lst=numbers))

#forth method
arr=numbers
arr.remove(max(arr))
print(max(arr))

#fifth method
lis = [11,52,63,85,14]
lis.sort()
print(lis[len(lis)-2])





