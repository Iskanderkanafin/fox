#Напишите функцию, которая принимает строку от пользователя, возвращает предложение с перевернутыми словами. Мы готовы -> готовы ли мы
def revers(zoro):
    zoro.reverse()
    x=" ".join(zoro)
    
    return x
    
        
str=input().split()
x=revers(str)
print(x)