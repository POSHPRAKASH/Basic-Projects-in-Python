import random

def dice_roll():
    dice_number = random.randint(1,6)
    return dice_number

print('------Welcome to Dice Rolling Simulator------')

while 1:
    choice = input('Do You Want to Roll a Dice(y,n)')
    if 'y' in choice.lower():
        print('Dice Rolling.....')
        number = dice_roll()
        print('Number on the Dice : ',number)
    elif 'n' in choice.lower():
        print('Exiting......Exited')
        break
    else:
        print('Invalid Input. Please Try Again')
