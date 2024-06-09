# ** PART 1 **
import string
from tkinter import E
intro = 'I am a student from Myanmar' # creating a string
intro = intro.split() # turning the string into a list of words

# delete  using "pop()" method
intro.pop(0) # from 'I' to '0'

# delete a single character using "remove()" method
intro.remove('am')

#delete a character using 'del' method
del intro[0] # 10th index => 'M'

# sorting the list
intro.sort()

# adding new words

# using operator '+'
intro = intro + ['Burmese']

# using 'append()' method
intro.append('Buddhist')

# using 'extend()' method
intro.extend(['Yangon'])

# Turing the list into a single string using 'join()' method
delimiter = ' ' # to put a space between each character
n_string = delimiter.join(intro) # putting the final string into a variablke

# printing the string
print(n_string)

# ** PART 2 **

# Nest lists
eg_nested_list = [1,[2,2],[3,3,3],[4,4,4,4]]

# The "*" operator
eg_operator = eg_nested_list * 2

# List slices
eg_list_slices = eg_operator[:4] # from first index to fifth index

# the "+=" operator
eg_operator += eg_nested_list

# a list filter
i = -1 # for starting as zero 
for e in eg_nested_list:
    i +=1 # increasing 1 every loop
    if isinstance(e,int) == False: # if the element is not a single integer, (filtering)
        eg_nested_list[i] = e[0] # element replaced with a single number

print(eg_nested_list)

# a list operation that is legal but does the wrong thing
n_list = eg_nested_list.remove(4)
print(n_list)


