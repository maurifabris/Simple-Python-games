#In this game the computer will try to guess the number you are thinking, 
# be careful not to give wrong values or everything will boom!!


import random

import sys

def computer_guess(max):
    print('=========================')
    print('Welcome!')
    print('=========================')
    print(f'imagine  a number between 1 and {max}, the computer will try to guess what it is')

    lower_limit = 1
    upper_limit= max
    play = True
    prediction = ''
    while play:
        #validate number
        if (lower_limit > upper_limit)  or (upper_limit > max) or (lower_limit < 1) or ( upper_limit < lower_limit):
            print('That number is impossible')
            sys.exit()

            #If the lower limit and upper is equal that number must be the solution
        if lower_limit == upper_limit:
            print(f'Yes! Your number is {lower_limit}')
            play = False

        if lower_limit != upper_limit:
            prediction = random.randint(lower_limit, upper_limit)
        else:
            prediction = lower_limit
        answer = input(f'My prediction is {prediction}. If it is very high enter "A", if it is very low enter "B" and if it is correct enter "C"').lower()
        if answer == 'a':
            upper_limit = prediction - 1
        elif answer == 'b':
            lower_limit = prediction + 1
        elif answer == 'c':
            print(f'Yes! Your number is {prediction}')
            play = False


computer_guess(50)