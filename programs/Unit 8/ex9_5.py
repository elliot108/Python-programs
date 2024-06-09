from itertools import count


def uses_all(s,u):
    flag = True
    for c1 in u:
        for c2 in s:
            if c1 == c2:
                flag = True
                break
            else:
                flag = False
        if flag == False:
            return False
    return True

fin = open('words.txt')
count = 0
for word in fin:
    if uses_all(word,'aeiouy'):
        count += 1
print(count)


# print(uses_all('smbcall','sla'))