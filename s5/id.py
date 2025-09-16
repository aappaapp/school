id = input("Your HKID number:").lower()

nums = []
sum = 36 * 9

for i, c in enumerate(id):
    if c.isalpha():
        sum += (ord(c) - ord("a") + 10) * (8 - i)
    else:
        sum += (int(c)) * (8 - i)

print(sum % 11 == 0)
