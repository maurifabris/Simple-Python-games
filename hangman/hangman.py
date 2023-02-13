from words import words

import string

import random

from diagram import visual_lifes


#function to use a random word of "words.py" file
def get_words(list):
    word = random.choice(list).upper()
    return word


def hangman():
    print('==========================')
    print('Hangman!')
    print('==========================')

    word = get_words(words)
    missing_letters = set(word)
    uncovered_letters = set()
    alphabet = set(string.ascii_uppercase)

    lifes = 7
    # Loop for play, it will end when you pick seven wrong letters
    while len(missing_letters) > 0 and lifes > 0:

        print(f'You have {lifes} and you use this letters: {" ".join(uncovered_letters)}')
        #This print the word in the terminal
        see_word = [letter if letter in uncovered_letters else '-' for letter in word]
        #this print generet a diagram to see your lifes
        print(visual_lifes[lifes])

        print(f'word: {"".join(see_word)}')

        user_letter = input('Choose a letter: ').upper()

        if user_letter in alphabet - uncovered_letters:
            uncovered_letters.add(user_letter)

            if user_letter in missing_letters:
                missing_letters.remove(user_letter)
                print('')
            else:
                lifes -= 1
                print(f'\nYour letter, {user_letter} not is in the word')
                
        elif user_letter in uncovered_letters:
            print("\nyou already tried with that letter, Please try another")
        else:
            print("\n This letter is not valid :c")

    if lifes == 0:
        print(visual_lifes[lifes])
        print(f'Sorry, The word was {word}')
        print(f'Game over')
    else:
        print(f'Exelent! the word is {word}')

hangman()