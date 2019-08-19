
import random

DEFAULTRANGE = 10
WRONGANSWER = "wrong answer!"
CORRECTANSWER= "correct answer!"
OPERATIONS = ["product","addition", "subtraction"]
INPUTQUESTION="What is the result?"
 
# Pick the highest number. Leave empty for default (10)

RANGE=DEFAULTRANGE

value1 = random.randint(0,RANGE)
value2 = random.randint(0,RANGE)

print("values",value1,value2)

# Pick a random operation
op_random = random.randint(0,len(OPERATIONS)-1)
print("op_random",op_random)

operation = OPERATIONS[op_random]
print(operation)

# Get the result from that random operation

OPERATIONSMAP = {"product": {"character":"x","expression":value1*value2},
                "addition":{"character":"+", "expression":value1+value2},
                "subtraction":{"character":"-","expression":value1-value2}
                }

result = OPERATIONSMAP[operation]["expression"]

print ("What is the result of",value1,operation,value2)

inputresult=int(input(INPUTQUESTION))

print("your answer",inputresult)
print("result",result)

if inputresult==result:
    print(CORRECTANSWER)
else:
    print(WRONGANSWER)


# Ask for the result from the user

# Compare both results and present the answer.

