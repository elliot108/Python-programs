# creating a dictionary in which we can see the house names from Game of thrones as 'Keys' 
# and the lists of members as 'values'
houses = {
'Targaryen':['Rhaenyra','Viserys','Daemon','Alicent'], 
'Stark':['Arya','Sansa','Bran'],
'Hightower':['Otto','Alicent'] # since Alicent is married to Viserys, her house should be both Targaryen and Hightower
}

d = {1:'a',2:'a',3:'b',4:'c'}

# this dictionary can be employed to describe the members of the house
# by putting the house name as key
# for e.g.
print(houses['Stark']) # this will print a few members of house Stark as a list
print()

# modifying the invert_dict function
def invert_dict(d):
    inverse = dict()
    for key in d:
          val = d[key] 
          for item in val: # for each item in the list of the value of each key
            if item not in inverse: # if that item is not allocated as key
                inverse[item] = [key] # define that item as a key and the actual key of the dictionary becomes a value
            else: # if that itme is already allocated as key
                inverse[item].append(key) # another value is added to the existed one  
    return inverse

print("Orginal dictionary")
print(houses) # original dictionary
print() # printing a new line
print("Inverted dictionary")
print(invert_dict(houses)) # inverted dictionary

#-------------Describing what is useful about my dictionary---------------
# My dictionary will be very useful if we want to know the complicated family trees in Game of Thrones universe.
# The original one will describe all the names that belong to a house. (although not all the names are included for this assignment)

#-------------The inverted dictionary----------------------------------
# The inverted one will be useful when we want to know the house name of a character. 
# Since only a few names are included, this may be found less useful. 
