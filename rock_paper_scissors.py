

### Rock, paper, scissors

from random import randint
from time import sleep

# Constants
BARS=20
OPTIONS=['Rock','Paper','Scissors']
WINNERLEFT = [
    ['Rock','Scissors'],
    ['Paper','Rock'],
    ['Scissors','Paper']
]

# Result sentences
RESULTWIN = 'You WON!'
RESULTLOSE = 'You lost. Try one more time'
RESULTTIE = 'Tie. Play again'

def bars():
    print('-'*BARS)

def emptyline():
    print('')


# Function for the computer pick
def computerpick():
    return OPTIONS[randint(0,len(OPTIONS)-1)]

# Decide on winner
# Return True if first element is winner
def winner(choice1,choice2):
    return [choice1,choice2] in WINNERLEFT

# main program loop
while True:
    # Print options and ask for player option
    for i in OPTIONS:
        print(OPTIONS.index(i)+1,':',i)

    # Ask for the player's option
    while True:
        try:
            emptyline()
            optstr=input('Pick your option (1-3):')
            opt=int(optstr)
            player=OPTIONS[opt-1]
            break
        except ValueError:
            print('String input. The value must be a number between 1 and 3 \n')
        except IndexError:
            print('Wrong value. The number must be between 1 and 3 \n')

    # show player's option
    bars()
    print('Your pick: ',player)
    #bars()
    sleep(2)


    # Computer pick
    computer=computerpick()
    #bars()
    print('Computer pick: ',computer)
    bars()
    emptyline()
    sleep(1)

    # Compare picks and declare a winner
    bars()
    if computer == player:
        print(RESULTTIE)
    elif winner(player,computer):
        print(RESULTWIN)
    else:
        print(RESULTLOSE)
    bars()
    sleep(2)
    emptyline()

# hmmmm...
