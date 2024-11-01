for x in range(1, 10):
  row = ""
  for y in range(2, 10):
    row += f"{y}*{x}={x * y}\t"
  print(row)
