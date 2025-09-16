N = int(input())
T_cold, T_hot = map(int, input().split())
T = list(map(int, input().split()))

last_c = -1
last_h = -1
min_dist = float("inf")

for i in range(N):
    if T[i] <= T_cold:
        last_c = i
        if last_h != -1:
            min_dist = min(min_dist, abs(last_h - last_c))
    elif T[i] >= T_hot:
        last_h = i
        if last_c != -1:
            min_dist = min(min_dist, abs(last_h - last_c))

print(min_dist)
