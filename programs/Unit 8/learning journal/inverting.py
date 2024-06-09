fin = open('input.txt') # opening the input file that contains a dictoinary
org_dic = dict() # declaring an empty dictionary
for line in fin: # for every line in the file
    keys_and_values = line.strip().split(':') # split each line as a list whose items are as keys and values for a dictionary
    org_dic[keys_and_values[0]] = keys_and_values[1] # first item of the list becomes key and second becomes value

# defining a function of invert dictionary (modified) from learning journal unit 7 
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key] 
        if val not in inverse: # if the value is not allocated as key 
            inverse[val] = [key] # define that item as a key and the actual key of the dictionary becomes a value
        else: # if value is already allocated as key
            inverse[val].append(key) # another value is added to the existed one  
    return inverse

in_dic = invert_dict(org_dic) # putting the inverted dictionary into a variable

fout = open('output.txt','w') # to write the dictionary into a file

for key in in_dic:
    line = key + ' : '+str(in_dic[key]) +'\n' # the words to write in each line of the file 
    fout.write(line) # writing each line
