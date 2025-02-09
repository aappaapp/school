import random

num = random.randint(1, 100)
minN = 1
maxN = 100
guess = minN - 1

creamExclude = [random.randint(1, 100), random.randint(1, 100)]

print(f"不用「食忌廉」的兩個數字{creamExclude}")

while True:
  guess = int(input(f"請輸入{minN}~{maxN}間的數字："))
  if guess > maxN or guess < minN:
    print(f"猜測數字超過範圍，", end="")
  elif guess > num:
    maxN = guess - 1
  elif guess < num:
    minN = guess + 1
  else:
    print("….….….….….….….….….….….….….….")
    print()
    print(f"答對了，密碼為{num}")
    dice = random.randint(1, 6)
    if dice not in creamExclude:
      print("食忌廉")
    break
