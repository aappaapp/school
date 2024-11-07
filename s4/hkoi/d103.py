import math

a = int(input())
b = int(input())
c = int(input())

area = a * b * math.sin(c * math.pi / 180) / 2

print(f"{area:.3f}")
