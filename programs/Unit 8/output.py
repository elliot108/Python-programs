import dbm
in_dic = dbm.open('inverted_dic')

for key in in_dic:
    print(key,':',in_dic[key])

print(in_dic)