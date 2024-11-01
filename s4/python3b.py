# 4E21 Aden
# https://github.com/aappaapp/school/blob/main/s4/python3b.py

sex: str = ""
height: float = 0.0
weight: float = 0.0 


while sex != "M" and sex != "F":
  sex = input("請輸入性別：(M/F) ").strip().upper()

while height <= 0:
  try: 
    height = float(input("請輸入身高：(m) "))
  except ValueError:
    print("請輸入數字")

while weight <= 0:
  try: 
    weight = float(input("請輸入體重：(kg) "))
  except ValueError:
    print("請輸入數字")


bmi: float = weight / (height * height)


LIMITS = {
  "M": {
    "underweight": 20,
    "overweight": 25
  },
  "F": {
    "underweight": 18,
    "overweight": 22
  }
}

match bmi:
  case bmi if bmi < LIMITS[sex]["underweight"]:
    print(f"您的BMI為{bmi:.2f}, 你的體重過輕")
  case bmi if LIMITS[sex]["underweight"] <= bmi <= LIMITS[sex]["overweight"]:
    print(f"您的BMI為{bmi:.2f}, 你的體重正常")
  case _:
    print(f"您的BMI為{bmi:.2f}, 你的體重過重")
