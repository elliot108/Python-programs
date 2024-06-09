import math

# PART 1
def mysqrt(a):
    x = 3
    while True:
        y = (x+a/x)/2.0
        if y == x:
            break
        else : 
            x = y
    return y

# PART 2
def test_square_root():
    for a in range(25):
        print("a =",a+1," |", "mysqrt(a) =", mysqrt(a+1), " |", "math.sqrt(a) =", math.sqrt(a+1)," | diff =",math.sqrt(a+1)-mysqrt(a+1))
test_square_root()