def new_line():
    print('.')

def three_lines():
    new_line()
    new_line()
    new_line()
def nine_lines():
    three_lines()
    three_lines()
    three_lines()
def clear_screen():
    nine_lines()
    three_lines()
    nine_lines()
    three_lines()
    new_line()

print("printing nine lines")
nine_lines()
print("printing 25 lines")
clear_screen()

    
