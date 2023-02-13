import random


def You_guess(max):
    print('=====================')
    print('Welcome')
    print('=====================')
    print("The goal is to guess the number that the computer chose.")

    random_number = random.randint(1, max) #random number between 1 and "max"
    prediction = 0

    while prediction != random_number:
        prediction = int(input(f"Guess a number between 1 and {max}: ")) 
        
        if prediction < random_number:
            print("The number is bigger...")
        elif prediction > random_number:
            print("the number is smaller...")
    print(f'Yes! the number was: {random_number}')


You_guess(50)