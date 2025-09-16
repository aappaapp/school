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
    maxN = guess - 1
  elif guess < num:
    minN = guess + 1
  else:
    print("….….….….….….….….….….….….….….")
    print()
    print(f"答對了，密碼為{num}")

    exclude1 = random.randint(1, 6)
    exclude2 = random.randint(1, 6)
    while exclude2 == exclude1:
        exclude2 = random.randint(1, 6)

    print(f"不用「食忌廉」的兩個數字{exclude1}, {exclude2}")

    dice = random.randint(1, 6)
    print(f"你的數字是{dice}")
    if dice == exclude1 or dice == exclude2:
      print("No食忌廉")
    else:
      print("食忌廉")
    break
