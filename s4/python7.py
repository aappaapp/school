def quadratic(a, b, c) -> tuple[float, float] | None:
  delta = b * b - 4 * a * c
  if delta < 0:
    return None
  elif delta == 0:
    print(f"方程式解為 2.5, -1.0")
  else:
    x = (-b + delta ** 0.5) / 2 / a
    y = (-b - delta ** 0.5) / 2 / a
    return x, y

a = float(input("請輸入方程式係數a:"))
b = float(input("請輸入方程式係數b:"))
c = float(input("請輸入方程式係數c:"))

ans = quadratic(a, b, c)
if ans is not None:
  if ans[0] == ans[1]:
    print(f"方程式解為{ans[0]}")
  else:
    print(f"方程式解為{ans[0]}, {ans[1]}")
else:
  print("方程式無解")
