

### Rock, paper, scissors

from random import randint
from time import sleep

# Constants

OPTIONS=['Rock','Paper','Scissors']

# Function for the computer pick
def computerpick():
    return OPTIONS[randint(0,len(OPTIONS)-1)]

# Print options and ask for player option
for i in OPTIONS:
    print(OPTIONS.index(i),':',i)

opt=input('Pick your option (1-3):')

player=OPTIONS[int(opt)-1] 
print('-'*10)
sleep(2)
print('Player pick: ',player)

# Computer pick
computer=computerpick()
print('Computer pick: ',computer)
print('-'*10)

# Compare picks and declare a winner

# hmmmm...
