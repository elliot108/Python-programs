from itertools import count


def is_abecedarian(s):
    flag = True
    for i in range(1,len(s)-1):
        if s[i] < s[i-1]:
            flag = False
            return flag
    return flag

fin = open('words.txt')
count = 0
for word in fin:
    if is_abecedarian(word):
        count+=1
        print(word)
print(count)


# print(is_abecedarian('becbc'))

            

