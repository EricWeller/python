numbers = []

while True:
    tempnum = int(input('Number: '))
    numbers.append(tempnum)
    print('~~~~~~~~~~~~~~~~~~~')
    b = input("Input another number?(n for no) ")
    if str(b) == 'n':
        break
def calculatemedian(number):
    N = len(number)
    numbers.sort()

    if N % 2 == 0:
        #even
        m1 = N/2
        m2 = (N/2) + 1
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (number[m1] + number[m2])/2
    else:
        m = (N+1)/2
        m = int(m) - 1
        median = number[m]
    return(median)

med = calculatemedian(numbers)
print("The median is: " + str(med))
