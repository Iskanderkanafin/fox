'''
def eveni_generator(N):
    for i in range(2 , N+1):
      if N % 2 == 0:
        yield i
N = int(input())
print(eveni_generator(N))
'''
list = []
def even(n):
    i = 0
    while(i <= n):
        if(i % 2 == 0):
            list.append(i)
        i = i + 2
n = int(input())
print(even(n))
print(*list)