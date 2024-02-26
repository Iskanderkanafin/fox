'''
list = []
def twonumi(n):
   i = 0
   while(i <= n):
    if (i % 4 == 0 and i % 3 == 0):
        list.append(i)
        i = i + 1
n = int(input())
print(twonumi(n))
print(*list)
'''

def divisible_by_3_and_4(n):
    i = 0
    for i in range(n):
        if (i % 3 == 0 and i % 4 == 0):
            
            yield i

n = int(input())
for num in divisible_by_3_and_4(n):
    print(num)

