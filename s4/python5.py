import random

num = random.randint(1, 100)
minN = 1
maxN = 100
guess = minN - 1

while True:
  guess = int(input(f"請輸入{minN}~{maxN}間的數字："))
  if guess > maxN or guess < minN:
    print(f"猜測數字超過範圍，", end="")
  elif guess > num:
    maxN = guess
  elif guess < num:
    minN = guess
  else:
    print("….….….….….….….….….….….….….….")
    print()
    print(f"答對了，密碼為{num}")
    break
