#Dice Rolling
#Import Statements
from random import randint

#Define the dice conditions
dice1 = -1
dice2 = -1
total_roll = 0
game = True

#dice rolling function
def roll_dice():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    total_roll = dice1 + dice2
    print(f'You have rolled {total_roll}')


while game == True:
    roll_dice()
    roll_again = input('Would you like to roll again? (y/n)')
    print('')
    
    if roll_again.lower() == 'y':
        game == True
    elif dice1 == dice2:
        print('You have rolled a double.')
        game = False
    else:
        game = False
        print('Game has ended.')