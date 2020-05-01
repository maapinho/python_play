

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

opt=input('Pick your option (1-3):')

player=OPTIONS[int(opt)-1] 
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
    print("Tie. Play again")
elif winner(player,computer):
    print('You won!\n')
else:
    print('You lost\n')


# hmmmm...
