numbers = []

while True:
    tempnum = int(input('Number: '))
    numbers.append(tempnum)
    print('~~~~~~~~~~~~~~~~~~~')
    b = input("Input another number?(n for no) ")
    if str(b) == 'n':
        break
S = sum(numbers)
L = len(numbers)
mean = S/L
print('The Average is: ' + str(mean))
