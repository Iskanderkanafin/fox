def squares_generator(N):
    for i in range(1, N+1):
        yield i**2


N = int(input())
square = squares_generator(N)
for square in squares_generator(N):
    print(square)
        
            