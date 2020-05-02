
FILENAME='t_.txt'

def bars():
    print('#' * 20)

inputtext = input('write something: \n')

with open(FILENAME,'r') as f:
    line=f.readline().rstrip('\n')

bars()

if inputtext==line:

    print('You wrote the same thing')
else:
    print('Text in the file: ',line)
    # write the new value
    with open(FILENAME,'w') as f:
        f.write(inputtext)
    print('You put in a new value')

