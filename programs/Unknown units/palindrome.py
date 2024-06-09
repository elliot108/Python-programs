# from itertools import count


# def first (word):
#     return word[0]

# def last (word):
#     return word[-1]

# def middle(word):
#     return word[1:-1]

# # print(middle("abcdefg"))
# def is_palindrome(word):
#     if len(word)<=3:
#         if first(word)==last(word):
#             return True
#         else:
#             return False
#     else:
#         if first(word)==last(word):
#            is_palindrome(middle(word))
#         else:
#             return False
        
# print(is_palindrome("return"))

def is_palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False

print(is_palindrome('noon'))
        

