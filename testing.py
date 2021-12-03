
#https://stackoverflow.com/questions/1155617/count-the-number-of-occurrences-of-a-character-in-a-string
list2 = [10, 20, 30, 40, 50, 60, 70, 80,1,15,45,60,50,30,40,20,40,60,30,78]
print(list2)

counts_dict = {}
for c in list(list2):
  if c not in counts_dict:
    counts_dict[c] = 0
  counts_dict[c] += 1

for key, value in counts_dict.items():
    print(key, value)

print(counts_dict)


#second method
sentence ="abbabcbdbabdbdbabababcbcbab"
def check_freq(x):
    freq = {}
    for c in set(x):
       freq[c] = x.count(c)
    return freq
print(check_freq(sentence))

count_value = {x:sentence.count(x) for x in sentence}
print(count_value)

#without using count and counter and regex method

count_number ={}
for c in list(sentence):
    if c not in count_number:
        count_number[c]=0
    count_number[c]+=1

for key,value in count_number.items():
    print(key,value)



