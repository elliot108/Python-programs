prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes: # for every letter from 'JKLMNOPQ'
    if letter == 'O' or letter == 'Q': # if the letter is O or Q,
        print(letter + 'u' + suffix) # an extra letter 'u' will be added
    else : 
        print (letter + suffix) 
    

     

