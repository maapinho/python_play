

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


# Function for the computer pick
def computerpick():
    return OPTIONS[randint(0,len(OPTIONS)-1)]

# Decide on winner
# Return True if first element is winner
def winner(choice1,choice2):
    return [choice1,choice2] in WINNERLEFT

# Print options and ask for player option
for i in OPTIONS:
    print(OPTIONS.index(i)+1,':',i)

while True:
    try:
        optstr=input('Pick your option (1-3):')
        opt=int(optstr)
        player=OPTIONS[opt-1]
        break
    except ValueError:
        print('String input. The value must be a number between 1 and 3 \n')
    except IndexError:
        print('Wrong value. The number must be between 1 and 3 \n')

bars()
print('Player pick: ',player)
bars()
sleep(2)


# Computer pick
computer=computerpick()
bars()
print('Computer pick: ',computer)
bars()
print('\n')

# Compare picks and declare a winner

if computer == player:
    print(RESULTTIE,'\n')
elif winner(player,computer):
    print(RESULTWIN,'\n')
else:
    print(RESULTLOSE,'\n')


# hmmmm...
