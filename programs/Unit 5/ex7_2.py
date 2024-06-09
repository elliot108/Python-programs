def eval_loop():
    while True:
        a = input("Type something \t")
        if a == 'done':
            break
        else:
            print( eval(a))
eval_loop()
