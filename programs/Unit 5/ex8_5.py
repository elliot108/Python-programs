def rotate(str,num):
    i = 0
    n_str = ''
    for char in str:
        char = chr(ord(char)+num)
        n_str = n_str  + char
        i += 1
        # print(char)
    return n_str
print(rotate('IBM',-1))