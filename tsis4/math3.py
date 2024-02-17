import math
def polygon_area(sides , length ):
    return (length / (2 * math.tan(math.pi / sides))) * (sides * length) /2
sides = int(input())
length = int(input())
area = polygon_area(sides , length)
print(area)