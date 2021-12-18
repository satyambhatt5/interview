def get_index_positions_2(list_of_elems, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    index_pos_list = []
    for i in range(len(list_of_elems)):
        if list_of_elems[i] == element:
            index_pos_list.append(i)
    return index_pos_list
list_of_elems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test', 'Ok']
# Get indexes of all occurrences of 'Ok' in the list
index_pos_list = get_index_positions_2(list_of_elems, 'Ok')
print('Indexes of all occurrences of a "Ok" in the list are : ', index_pos_list)


#compresension example 
index_pos_list = [ i for i in range(len(list_of_elems)) if list_of_elems[i] == 'Ok' ]
print('Indexes of all occurrences of a "Ok" in the list are : ', index_pos_list)