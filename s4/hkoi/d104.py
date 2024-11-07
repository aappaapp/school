a, b, c = map(int, input().split())

delta = b * b - 4 * a * c

if delta < 0:
  print("None")
elif delta == 0:
  print(f"{-b / 2 / a:.3f}")
else:
  x = (-b + delta ** 0.5) / 2 / a
  y = (-b - delta ** 0.5) / 2 / a
  if x > y:
    print(f"{y:.3f} {x:.3f}")
  else:
    print(f"{x:.3f} {y:.3f}")
