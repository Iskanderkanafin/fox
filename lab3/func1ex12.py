'''
Определите функцию histogram(), которая принимает список целых чисел и выводит гистограмму на экран. Например, histogram([4, 9, 7]) должна выводить следующее:

****
*********
*******
'''




def histogramm(mylist):
    for i in mylist:
        j=0
        while j<int(i):
            print("*", end='')
            j=j+1
        print('')
mylist = input("Введите числа: ").split()
histogramm(mylist)