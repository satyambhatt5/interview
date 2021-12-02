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

