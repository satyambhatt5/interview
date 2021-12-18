
#*? find method find the occurne in the string with out using  count function 

names=['Deepak','Reema','John','Deepak','Munna','Reema','Deepak','Amit','John','Reema']
d={}
for i in range(len(names)-1):
    x=names[i]
    c=0
    for j in range(i,len(names)):
        if names[j]==names[i]:
            c=c+1
    count=dict({x:c})
    if x not in d.keys():
        d.update(count)
print (d)

#** second mehtod for counting occurance of names

names=['Deepak','Reema','John','Deepak','Munna','Reema','Deepak','Amit','John','Reema']
nameset=set(names)
d={name:names.count(name) for name in nameset}
print(d)
