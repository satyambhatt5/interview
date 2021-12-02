numbers = [2, 3, 4, 7, 9, 11, 12, 14, 15]
##find the even and odd in the list
even_list = list(filter(lambda x: (x % 2 == 0), numbers))
print(even_list)

odd_list = list(filter(lambda x: (x % 2 != 0), numbers))
print(odd_list)



# numbers of occurance of each character in a list 
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
# print(char_count("google.com")
str ="qhhqfwhqfbhfyffhbhfb"
def char_count(str): 
    dict = {} 
    for n in str: 
        keys = dict.keys() 
        if n in keys: 
            dict[n] += 1
        else: 
            dict[n] = 1
    return dict
print(char_count(str))

#swap the list value 
def swapList(sl):
    n = len(sl)
    # Swapping 
    sl[0],sl[n - 1]=sl[n - 1],sl[0]
    return sl
print(swapList([1,2,3,4,5]))

#second method swap the value 
def swap(l):
  #now swap the value 
  l[0],l[-1]=l[-1]**2,l[0]**2
  #sum of last three value 
  return l #sum(l[3:])l
print(swap(l=numbers))

#please do suffling 
from random import shuffle
x = ['hackr.io', 'Is', 'The', 'Best', 'For', 'Learning', 'Python']
shuffle(x) 
print(x)
















