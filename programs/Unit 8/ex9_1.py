
fin = open('words.txt')

# print(fin.readline() + fin.readline()

for word in fin:
    count = 0
    for c in word:
        count += 1
    if count > 20:
        print(word)
    
