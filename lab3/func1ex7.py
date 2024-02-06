
#Учитывая список целых чисел, верните True, если массив содержит 3 где-то рядом с 3.

#def has_33(nums):
 #проходить

#has_33([1, 3, 3]) → Истина
#has_33([1, 3, 1, 3]) → Ложь
#has_33([3, 1, 3]) → Ложь

def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i]==nums[i+1]:
            return True
    return False
inp = input("Введите числа: ")
nums = inp.split()
if has_33(nums)==True:
    print("True")
else:
    print("False")