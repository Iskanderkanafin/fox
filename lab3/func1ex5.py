#Напишите функцию, которая принимает строку от пользователя и выводит все перестановки этой строки.
from itertools import permutations
def perm(s):
    per = permutations(s)
    result = [''.join(i) for i in per]
    return " ".join(result)
s = input("Введите строку: ")
print(perm(s))