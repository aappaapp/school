score = [87, 42, 65, 23, 99, 75, 68, 67, 53, 90]


def score_sum():
    sum = 0
    for i in range(len(score)):
        sum += score[i]
    return sum


def score_average():
    return score_sum() / len(score)


def score_max():
    max = score[0]
    for i in range(len(score)):
        if score[i] > max:
            max = score[i]
    return max


def score_min():
    min = score[0]
    for i in range(len(score)):
        if score[i] < min:
            min = score[i]
    return min


def score_greater_or_equal_50():
    count = 0
    for i in range(len(score)):
        if score[i] >= 50:
            count += 1
    return count


print(score_sum())
print(score_average())
print(score_max())
print(score_min())
print(score_greater_or_equal_50())
