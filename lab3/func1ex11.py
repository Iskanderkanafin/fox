#Напишите функцию Python, которая проверяет, является ли слово или фраза палиндромом или нет. Примечание: Палиндром - это слово, фраза или последовательность, которые читаются как в обратном, так и в прямом направлении, например, мадам


def palindrome(s):
    for i in range(0, (int(len(s)/2))):
        if s[i]!=s[-(i+1)]:
            return False
    return True
if palindrome(input("Введите слово: ")):
    print("palindrome")
else:
    print("not palindrome")