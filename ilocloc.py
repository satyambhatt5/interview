import pandas as pd
def main():
    
    students = [ ('jack', 34, 'Sydeny') ,
                 ('Riti', 30, 'Delhi' ) ,
                 ('Aadi', 16, 'New York') ]
    
    # Create a DataFrame object
    dfObj = pd.DataFrame(students, columns = ['Name' , 'Age', 'City'], index=['a', 'b', 'c']) 
    
    print("Original DataFrame : ", dfObj, sep="\n")
    
    print("***** Select Columns in DataFrame by [] *********")
  
    '''
    Select a Column by Name using []
    '''
    column2 = dfObj['Age']
    
    print("Select column By Name using [] " , column2 , sep='\n')
    print("Type : " , type(column2))
    '''
    Select  Multiple Column by Name using []
    '''
    column2 = dfObj[ ['Age', 'Name'] ]
    
    print("Select multiple columns By Name using [] " , column2 , sep='\n')
    print("Type : " , type(column2))
       
    
    print("**** Selecting by Column Names & Rows Index Labels Using df.loc ******")
    
    '''
    Selecting a Single Column by Column Names
    '''
    columnsData = dfObj.loc[ : , 'Age' ]
    
    print("Select a column By Name using loc " , columnsData , sep='\n')
    print("Type : " , type(columnsData))
    
    '''
    Selecting multiple Columns by Column Names
    '''
    
    # Select only 2 columns from dataFrame and create a new subset DataFrame
    columnsData = dfObj.loc[ : , ['Age', 'Name'] ]
    
    print("Select multiple columns By Name using loc " , columnsData , sep='\n')
    print("Type : " , type(columnsData))
    
    '''
    Selecting a Single Row by Index label
    '''
    
    rowData = dfObj.loc[ 'b' , : ]
    
    print("Select a Single Row " , rowData , sep='\n')
    print("Type : " , type(rowData))
    
    '''
    Selecting multiple Rows by Index labels
    '''
    rowData = dfObj.loc[ ['c' , 'b'] , : ]
    
    print("Select multiple Rows" , rowData , sep='\n')
    
    '''
    Select both Rows & Columns by Index labels
    '''
    
    subset = dfObj.loc[ ['c' , 'b'] ,['Age', 'Name'] ]
    
    print("Select both columns & Rows" , subset , sep='\n')
    
    subset = dfObj.loc[ 'a' : 'c' ,'Age' : 'City' ]
    
    print("Select both columns & Rows with selection range " , subset , sep='\n')
    
    
    print("**** Selecting by Column Indexes & Rows Index Positions Using df.iloc ******")
    
    '''
    Select a single column by Index Position
    '''
    print(" Select column at index 2 ")
    print( dfObj.iloc[ : , 2 ] )
    
    '''
    Select multiple columns by Index range 
    '''
    print(" Select columns in column index range 0 to 2")
    print(dfObj.iloc[:, 0:2])
    
    '''
    Select multiple columns by Indexes in a list 
    '''
    print(" Select columns at column index  0 and 2")
    print(dfObj.iloc[: , [0, 2]])
    
    
    '''
    Select single row by Index Position
    '''
    print(" Select row at index 2 ")
    print( dfObj.iloc[ 1 , :  ] )
    
    '''
    Select multiple rows by Index range 
    '''
    print(" Select rows in row index range 0 to 2")
    print(dfObj.iloc[ 0:2 , : ])
    
    '''
    Select multiple rows by Index positions in a list 
    '''
    print(" Select rows at row index  0 and 2")
    print(dfObj.iloc[[2 ,0 ] , : ])
    
    
    '''
    Select multiple rows & columns by  Index positions
    '''
    print(" Select rows at index 0 & 2 . Also columns at row  1 and 2")
    print(dfObj.iloc[[0 , 2] , [1 , 2] ])
    '''
    Select multiple rows & columns by  Indexes in a range
    '''
    print(" Select rows at index 0 to 2 (2nd index not included) . Also columns at row  0 to 2 (2nd index not included)")
    print(dfObj.iloc[ 0 : 2 ,  1 : 2 ])
 
       
if __name__ == '__main__':
    main()
