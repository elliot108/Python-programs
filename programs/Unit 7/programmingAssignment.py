# ---- copying the codes from instructor --------
alphabet = "abcdefghijklmnopqrstuvwxyz"   
test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 
test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"] 
# From Section 11.2 of: 
# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press. 
def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d 
# -----------------------------------------------

# ** PART 1 ** #

def has_duplicates(s): # defining function 
    d = histogram(s) # making a dictionary in which contains the characters as keys and number of that charater as values
    for i in d:
        if d[i] > 1: # if a key of that dictionary has a value more than 1
            return True  # return True and function's work ends
    return False  # if the looping ends, return False

# a loop over the strings in the provided test_dups list

for str in test_dups: # for each element (that are strings) of the list test_dups
    if has_duplicates(str): # if has_duplicates funciton returns true
        print(str,'has duplicates.')
    else: # if has_duplicates funciton returns false
        print(str,'has no duplicates.')

# ** PART 2 ** #

# missing_letters function 

def missing_letters(s):
    d = histogram(s) # making a dictionary in which contains the characters as keys and number of that charater as values
    li = list() # creating an empty list
    for letter in alphabet: # for every character in string alphabet
        if d.get(letter,False) == False: # if a character is not found in the argument string
            li += letter # that missing character is added to the list
    delimter = ',' # to write a comma between the missing letters
    str = delimter.join(li) # convert that list into string using join method
    return str

# a loop over the strings in list test_miss and calling missing_letters with each string
for letter in test_miss:
    miss = missing_letters(letter)
    if miss:
        print(letter,'is missing letters',miss)
    else:
        print(letter,'uses all letters')



