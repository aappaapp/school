card_list=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
points = 0
card = ""

for i in range(1,6):
    while card not in card_list:
        card = input(f"Please input card {i}: ")
    points += card_list.index(card) + 1
    card = ""

print(points)
