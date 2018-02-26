while True:
    a = input('Input an integer: ')
    if int(a) % 2 == 0:
        print(a + " is an even number")
    else:
        print(a + " is an odd number")
    b = input("Type in (y/n) to use again? ")
    if str(b) == 'n':
        break
