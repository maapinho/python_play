# To do
# pick the range of numbers
# Loop
# error catching for inputs (must be an integer)
# answers list from external files


import random

# Constants

DEFAULTRANGE = 10
WRONGANSWERLIST = ["wrong answer!",
                   "Dumbass!",
                   "WTF??? How old are you?"]
CORRECTANSWERLIST= ["Correct Answer!",
                    "Niiiice!",
                    "Einstein!"]
OPERATIONS = ["product","addition", "subtraction"]
INPUTQUESTION="What is the result of "
 
# Pick the highest number. Leave empty for default (10)

# function to pick a random item from a list

def randomitem(inputlist):
    return inputlist[random.randint(0,len(inputlist)-1)]

# Range of values for expression's input

valuerange=input("Pick a range of values from 0 to 10 (default is 10): ")

if valuerange=="":
    valuerange=DEFAULTRANGE

###### Pending error catching keeping within the value range of 0 to 10

valuerange=int(valuerange)


#valuerange=DEFAULTRANGE

value1 = random.randint(0,valuerange)
value2 = random.randint(0,valuerange)



operation = randomitem(OPERATIONS)
#print(operation)

# Get the result from that random operation

OPERATIONSMAP = {"product": {"character":"x","expression":value1*value2},
                "addition":{"character":"+", "expression":value1+value2},
                "subtraction":{"character":"-","expression":value1-value2}
                }

result = OPERATIONSMAP[operation]["expression"]

# Ask for the result from the user


print ("What is the result of",value1,OPERATIONSMAP[operation]["character"],value2)

inputresult=int(input(INPUTQUESTION))

#print("your answer",inputresult)
#print("result",result)

# Pick random answers from the answer lists
correct_answer=randomitem(CORRECTANSWERLIST)
wrong_answer=randomitem(WRONGANSWERLIST)

# Compare both results and present the answer.

#----------- old method with a single answer
#if inputresult==result:
#    print(CORRECTANSWER)
#else:
#    print(WRONGANSWER)
#----------------------------------------

if inputresult==result:
    print(correct_answer)
else:
    print(wrong_answer)

