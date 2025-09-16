x = int(input("請輸入底數數字:"))
y = int(input("請輸入次方數字:"))

def power(a, b):
  return a ** b

print(f"{x}的{y}次方為{power(x, y)}")
