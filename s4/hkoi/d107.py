import math

x = int(input())

sqrt = math.isqrt(x)
isSquare = sqrt * sqrt == x
sqrt2 = math.isqrt(8 * x + 1)
isTriangular = sqrt2 * sqrt2 == 8 * x + 1

if isSquare:
  if isTriangular:
    print("Both")
  else:
    print("Square")
else:
  if isTriangular:
    print("Triangular")
  else:
    print("Neither")
