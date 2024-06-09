def uses_only(s,u):
    flag = True
    for c1 in s:
        for c2 in u:
            if c1 == c2:
                flag = True
                break
            else:
                flag = False
        if flag == False:
            return False
    return True

fin = open('words.txt')
for word in fin:
    if uses_only(word,'acefhlo'):
        print(word)


# print(uses_only('small','sla'))