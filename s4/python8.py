def is_prime_optimized(n):
    if n < 2:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

while True:
  num = int(input("請輸入數字:"))
  if num == -9999:
      break
  elif is_prime_optimized(num):
      print(f"{num}是質數")
  else:
      print(f"{num}不是質數")
