import dbm
org_dic = dbm.open('org_dic','c')
print(org_dic)
dic = dict()
for key in org_dic:
    print(key)

print(dic)

def invert_dict(d):
    inverse = dict()
    for key in d:
          val = d[key] 
          for item in val: # for each item in the list or key of the dictionary
            if item not in inverse: # if that item is not allocated as key
                inverse[item] = [key] # define that item as a key and the actual key of the dictionary becomes a value
            else: # if that itme is already allocated as key
                inverse[item].append(key) # another value is added to the existed one  
    return inverse

in_dic = invert_dict(dic)

print(in_dic)

invert_dic = dbm.open('inverted_dic','c')

for key in in_dic:
    print('blah blah')
    invert_dic[key] = in_dic[key]

for key in invert_dic:
    print(key,':',invert_dic[key])
