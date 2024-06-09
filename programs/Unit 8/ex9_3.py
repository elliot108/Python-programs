def avoids(s,f):
    flag = True
    for c1 in s:
        for c2 in f:
            if c1 == c2:
                flag = False
                break
        if flag == False:
            break
    return flag

print(avoids('small','lm'))
