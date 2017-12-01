""" Allen Downey Think Python Exercise 10-6
    
    This function checks whether a list is sorted in ascending order and returns True or False,
    depending on the outcome.
    """

list_of_words = ['a','d','c']

def is_sorted(t):
    sorted_variable = sorted(t)
    if t == sorted_variable:
        return True
    else:
        return False

print is_sorted(list_of_words)

