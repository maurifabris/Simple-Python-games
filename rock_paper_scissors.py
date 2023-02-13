# here you can play Rock, Paper or Scissors whit the computer

import random


def player_win(player, oponent):
    if  ((player == 'a' and oponent == 'b') 
    or (player == 'b' and oponent == 'c') 
    or (player=='c' and oponent == 'a')):
        return True
    else:
        return False


def play():
    user = input("Take an option: A for rock, B for a scissors or C for a paper./n").lower()
    computer = random.choice(['a','b','c'])
    
    if user == computer:
        return 'Tie!'

    if player_win(user,computer):
        return 'You win!'

    return 'You lose :C'

print(play())



