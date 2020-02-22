# Reads 2 input files, compares the lines
# and prints every line they have in common
# ignoring leading and trailing spaces


#imports
import sys
print (sys.argv)

# constants
INPUTLIST1 = ["  valor","palavra","palavrinha","palavrona","fidacaia   "]
INPUTLIST2 = ["valor ","valor2","palavrinha","palavrona","fidacaixa"]

# Input process and parse
file1 = sys.argv[1]
file2 = sys.argv[2]
#print(files)

# File processing into 2 input lists
file = open(file1,"r")
list1 = list(file)
file.close()

file = open(file2,"r")
list2=list(file)
file.close()

#print(list1,'\n', list2)

compare = []

# loop over items and compare
for item1 in list1:
    for item2 in list2:
        item1 = item1.strip()
        item2 = item2.strip()
        #append to the compare list if items are the same
        if item1==item2:
            compare.append(item1)
            
print('result: ',compare)
