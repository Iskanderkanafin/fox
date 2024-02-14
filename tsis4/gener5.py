def allnum(n):
    i = 0
    for i in range(i , n+1):
      yield i
      
n = int(input())
for ippon in allnum(n):
    print(ippon)
