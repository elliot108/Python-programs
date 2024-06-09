def divide(N,D):
    i = 1
    while True:
        if N*i == D:
            break
        elif N*i > D:
            i =i-1
            break
        i = i+1
    return i

print(divide(3,15))
    
