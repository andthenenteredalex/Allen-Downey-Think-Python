""" Allen Downey Think Python Exercise 10-9
    
    This function takes a list and removes duplicate items and returns a new list with no duplicates.
    
    """

def remove_duplicates(list):
    new_list = []
    t = sorted(list)
    counter = 1
    while counter < (len(list)-1):
        if t[counter] != t[counter]-1:
            new_list.append(t[counter])
        counter = counter + 1
    return new_list

list = [1,2,9,7,4,6,2,3]

print remove_duplicates(list)
