mytuple = (0, True, False, True)

a = all(mytuple)


if a:
    print(f"Все элементы {mytuple} тру")
else:
    print(f"Не все в {mytuple} тру")