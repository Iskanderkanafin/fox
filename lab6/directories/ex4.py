import os
garou = int(input("write:"))
count = 0
file = open(garou,'r')
for x in file:
    count += 1
    file.close()
    print("numbers of lines",count)