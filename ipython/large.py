#find the second largest value

num = [1,2,3,4,5,6,7,8,9,10]

def secondlargest(numbers):
    numbers.sort()
    return  numbers[-2]
print(secondlargest(numbers=num))

#find the occurance in the gien string

# using dictionary
# def char_count(str):
#    dict = {}
#   for n in str:
#      keys = dict.keys()
#     if n in keys:
#       dict[n] += 1
#    else:
#      dict[n] = 1
#  return dict
# print(char_count("google.com"))

#Initialize array     
arr = [25, 11, 7, 75, 56]    
     
#Initialize max with first element of array.    
max = arr[0]  
     
#Loop through the array    
for i in range(0, len(arr)):    
    #Compare elements of array with max    
   if(arr[i] > max):    
       max = arr[i]
       
           
print("Largest element present in given array: " + str(max))   


#find the occurance in the gien string
def char_count(str):
    dict = {}
    for n in str:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_count("google.com"))

