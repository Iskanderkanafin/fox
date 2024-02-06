'''
Напишите функцию, которая принимает список целых чисел и возвращает значение True, если оно содержит 007 в порядке
def spy_game(nums):
 проходить

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False"'

'''

def spy_game(nums):
    myString = ""
    for i in nums:
        if int(i)==0:
            myString+="0"
        elif int(i)==7:
            myString+="7"
    x=myString.find("007")
    if x==-1:
        return False
    else:
        return True
inp = input("Введите числа: ")
nums=inp.split()
if spy_game(nums)==True:
    print("True")
else:
    print("False")