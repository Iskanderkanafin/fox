list_numbers = input("Введите числа(через пробел): ").split()

n = 1

for x in list_numbers:
    n *= int(x)

print("Результат умножения всех чисел:", n)