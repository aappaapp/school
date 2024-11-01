a = int(input())

while True:
  if a / 1000 >= 1:
    print("1000")
    a -= 1000
  elif a / 500 >= 1:
    print("500")
    a -= 500
  elif a / 100 >= 1:
    print("100")
    a -= 100
  elif a / 50 >= 1:
    print("50")
    a -= 50
  elif a / 20 >= 1:
    print("20")
    a -= 20
  elif a / 10 >= 1:
    print("10")
    a -= 10
  else:
    break
