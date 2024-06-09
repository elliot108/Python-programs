#  10.1
from itertools import count
from re import I, T


def nested_sum(t): # 't' is a parameter for a list
    total = 0
    for e in t: # for each element in the list 
        total = total + sum(e) # accumulating the total value of adding numbers in each element  
    return total # return that total value

# creating a list with variable 't'
t = [[1,2],[3],[4,5,6]] # variable 't' has a reference to the object [[1,2],[3],[4,5,6]]

nested_sum(t) # putting the list 't' as an argument


#  10.2
def consum(t):
    for i in range(0,len(t)):
        if i > 0:
            t[i] = t[i] + t[i-1]
# t = [1,2,0,4,5,6]
# consum(t)
# print(t)

# 10.3
def middle(t):
    del t[0]
    del t[len(t)-1]
# middle(t)
# print(t)

def middle(t):
    del t[0]
    del t[len(t)-1]
    return t

# print(middle(t))

# 10.5
t=[1,2,2,3]
def is_sorted(t):
    for i in range(0,len(t)-1):
        if i > 0:
            if t[i-1] > t[i]:
                return False
    return True
# print(is_sorted (t))

# 10.6
def is_anagram(a,b):
    al = list(a)
    bl = list(b)
    jc = -1
    count =0
    if len(a) == len(b):
        i =0
        for i in range(0,len(a)):
            for j in range(0,len(b)):
                if al[i] == bl[j]: 
                    bl[j] = 1
                    count+=1
                    break        
        if count == len(a):
            return True
        else:
            return False
        # while (i<len(bl)):
        #     if al[i] == bl


    else:
        return False

# print(is_anagram('after','long'))


                

