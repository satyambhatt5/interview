#check the duplicate in the list 

listofElems = [51, 52, 53, 54, 55, 52, 57, 52, 59]


#check the duplicate in the list
def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True
 
def checkIfDuplicates_2(listOfElems):
    ''' Check if given list contains any duplicates '''    
    setOfElems = set()
    for elem in listOfElems:
        if elem in setOfElems:
            return True
        else:
            setOfElems.add(elem)         
    return False
 
def checkIfDuplicates_3(listOfElems):
    ''' Check if given list contains any duplicates '''    
    for elem in listOfElems:
        if listOfElems.count(elem) > 1:
            return True
    return False
 
def main():
 
    listOfElems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']
    print('*** Check for duplicates in list using Set and comparing sizes ***')
    result = checkIfDuplicates_1(listOfElems)
    if result:
        print('Yes, list contains duplicates')
    else:
        print('No duplicates found in list')    
 
    print('*** Check for duplicates in list using Set and looking for first duplicate ***')
 
    result = checkIfDuplicates_2(listOfElems)
 
    if result:
        print('Yes, list contains duplicates')
    else:
        print('No duplicates found in list')        
 
    print('*** Check if list contains duplicates using list.count() ***')
    result = checkIfDuplicates_3(listOfElems)
 
    if result:
        print('Yes, list contains duplicates')
    else:
        print('No duplicates found in list') 
 
if __name__ == '__main__':
    main()

