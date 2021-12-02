def main():
    wordList = ['hi', 'hello', 'this', 'that', 'is', 'of']
    
    '''
     Iterate over the list using for loop
    '''
    for word in wordList:
        print(word)
        
    print("*************")    
    
    
    '''
     Iterate over the list using while loop
    '''
    i = 0
    sizeofList = len(wordList) 
    while i < sizeofList :
        print(wordList[i]) 
        i += 1
        
    print("*************")    
    
    '''
     Iterate over the odd number position elements in list using while loop
    '''
    i = 0
    sizeofList = len(wordList) 
    while i < sizeofList :
        if i % 2 == 1 :
            print(wordList[i]) 
        i += 1
        
    print("*************")    
    
    '''
     Iterate over the list using for loop and range()
    '''
    for  i in range(len(wordList)) :
        print(wordList[i]) 
        i += 1
        
    print("*************")    
    
    '''
     Iterate over the list using List Comprehension
    '''
    [print(i) for i in wordList]
if __name__ == '__main__':
    main()