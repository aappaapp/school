# 4E21 Aden
# https://github.com/aappaapp/school/blob/main/s4/python3.py

sex: str = input("請輸入性別：(M/F) ")
assert sex == "M" or sex == "F"
height: float = float(input("請輸入身高：(m) "))
assert height > 0
weight: float = float(input("請輸入體重：(kg) "))
assert weight > 0


bmi: float = weight / (height * height)

underweight_limit = 20 if sex == "M" else 18
overweight_limit = 25 if sex == "M" else 22

match bmi:
  case bmi if bmi < underweight_limit:
    print(f"您的BMI為{bmi:.2f}, 你的體重過輕")
  case bmi if underweight_limit <= bmi <= overweight_limit:
    print(f"您的BMI為{bmi:.2f}, 你的體重正常")
  case _:
    print(f"您的BMI為{bmi:.2f}, 你的體重過重")
