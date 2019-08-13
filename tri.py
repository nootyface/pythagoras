import sys
import string

def inputSide(side):
    sides.append(int(side))

def compare(list):
    a = 0
    b = 0
    for i in list:
        if i > a:
            a = i
    for i in list:
        if i == a:
            continue
        b = b + (i*i)
    if (a*a) == b:
        print('This is a pythagorean triangle')
    else:
        print('This is not a pythagorean triangle')

while True:
    sides = []
    for i in range(1, 4):
        inputSide(input('Please enter the length of side ' + str(i) + ': '))
    compare(sides)
    answer = input('Type \'t\' to try another triangle, or \'q\' to quit: ')
    if answer == 'q':
        sys.exit()
    elif answer == 't':
        continue