fin = open('words.txt')
for letter in fin:
    if len(letter)>=6:
        for i in range(1,len(letter)-1):
            if i+4 <= len(letter)-1 and letter[i] == letter[i-1] and letter[i+1]==letter[i+2] and letter[i+3]== letter[i+4]:
                print (letter)
