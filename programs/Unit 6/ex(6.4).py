def is_power(a,b):
    if a%b==0 and a/b == 1:
        return True
    elif a%b==0:
        return is_power(a/b,b)
    else:
        return False
print(is_power(121,11))