""" Allen Downey Think Python Exercise 10-7
    
    This function checks if two words are anagrams and returns True if they are.
    
    """
def is_anagram(word_one, word_two):
    one = sorted(list(word_one))
    two = sorted(list(word_two))
    if one == two:
        return True
    elif one != two:
        return False



word = 'hello'
word2 = 'hlehol'

anagram = is_anagram(word, word2)
print anagram
