import numpy as np

def nroot(x, n):
  return np.roots([1] + [0]*(n-1) + [-x])

def to_string(x):
  return f"{np.real(x)}{'+' if np.imag(x) > 0 else '-'}{np.imag(x)}i"

x = int(input("請輸入底數數字:"))
y = int(input("請輸入次方數字:"))

print(f"{x}的{y}次方為{to_string(nroot(x, y))}")
