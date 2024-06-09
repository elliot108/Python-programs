# fin = open('words.txt')
# for word in fin:
#     flag = True
#     for c in word:
#         if c == 'e':
#             flag = False
#     if flag == True:
#         print(word)
        
def has_no_e(s):
    flag = True
    for c in s:
        if c == 'e':
            flag = False
            break
    return flag

print(has_no_e('abecd'))