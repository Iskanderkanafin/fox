import math
def degree_to_radian(grad):
   return grad * (math.pi / 180)
grad = float(input())
radian = degree_to_radian(grad)
print(radian)
