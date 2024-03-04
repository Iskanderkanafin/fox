import os

path = int(input("write"))


if os.path.exists(path):
    print("exists")
    
    
    directory, filename = os.path.split(path)
    
    print("Directory:", directory)
    print("Filename:", filename)
    
else:
    print("not exist")