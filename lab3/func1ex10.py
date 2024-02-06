#Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.
def unique(myList):
    uniqueList = []
    for i in myList:
        if i not in uniqueList:
            uniqueList.append(i)
    print(uniqueList)
inp = input("Введите числа: ")
mylist = inp.split()
unique(mylist)