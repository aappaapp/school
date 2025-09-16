## Normal version
def nroot(x, y):
  return x ** (1/y)

x = int(input("請輸入被開方數字:"))
y = int(input("請輸入開方數字:"))

print(f"{x}開{y}次方為{nroot(x, y)}")


## Advanced version
import numpy as np

def nroot(x, y):
  return np.roots([1] + [0]*(y-1) + [-x])

def to_string(x):
  return f"{np.real(x):.2f}{'+' if np.imag(x) > 0 else ''}{f"{np.imag(x):.2f}i" if np.imag(x) != 0 else ''}"

x = int(input("請輸入被開方數字:"))
y = int(input("請輸入開方數字:"))

print(f"{x}開{y}次方為{",".join(map(lambda x: to_string(x), nroot(x, y)))}")
