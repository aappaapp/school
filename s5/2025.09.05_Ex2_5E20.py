score = [87, 42, 65, 23, 99, 75, 68, 67, 53, 90]

# Non-general case
for i in range(9):
    for j in range(9 - i):
        if score[j] > score[j + 1]:
            score[j], score[j + 1] = score[j + 1], score[j]

print(score)
