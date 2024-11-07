x = input()

if x[-2:] in ["11", "12", "13"]:
  print(x + "th")
elif x[-1] == "1":
  print(x + "st")
elif x[-1] == "2":
  print(x + "nd")
elif x[-1] == "3":
  print(x + "rd")
else:
  print(x + "th")
