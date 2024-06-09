import math

# PART 1
def mysqrt(a): # defining a function named mysqrt()
    x = 3.0 # taking the estimated value of x as 3
    while True:
        y = (x+a/x)/2.0
        if y == x:
            break
        else : 
            x = y
    return x # return the result of y or the squared root of the added argument

# PART 2
def test_square_root(): # defining another function to print 
    a = 1 
    while a <= 25: # using while loop
        print("a =",a," |", "mysqrt(a) =", mysqrt(a), " |", "math.sqrt(a) =", math.sqrt(a)," | diff =",abs(math.sqrt(a)-mysqrt(a))) 
#              ^    ^     ^       ^              ^          ^         ^                 ^           ^                 ^
#             a =    1    |    mysqrt(a) =      1.0         |    math.sqrt(a) =        1.0         | diff =  0.0  this is the absolute value of difference between the results of my function and build-in function
#                                     the first print statement will be like the above one
        a = a + 1 # to terminate the loop
test_square_root() # calling the function