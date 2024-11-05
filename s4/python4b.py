# 4E21 Aden

x_start = 2
x_end = 9
y_start = 1
y_end = 9

for y in range(y_start, y_end + 1):
  row = ""
  for x in range(x_start, x_end + 1):
    row += f"{x}*{y}={x * y}\t"
  print(row)
