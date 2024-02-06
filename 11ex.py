#Insert the correct keyword to make the variable x belong to the global scope.
#В Python ключевое слово global позволяет изменять переменную за пределами текущей области видимости. Оно используется для создания глобальной переменной и внесения в нее изменений в локальном контексте.

def myfunc():
  global x
  x = "fantastic"