x1: float = float(input("輸入A點的x座標："))
y1: float = float(input("輸入A點的y座標："))
x2: float = float(input("輸入B點的x座標："))
y2: float = float(input("輸入B點的y座標："))

print(f"A點座標為({x1}, {y1})")
print(f"B點座標為({x2}, {y2})")
print(f"兩點距離為{((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5:.4f}")
