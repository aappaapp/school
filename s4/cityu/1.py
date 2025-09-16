N, R, B = map(int, input().split())

if (R+B) % N == 0:
    K = (R+B)//N
    if (R % K + B % K) == 0:
        print("Possible: Same colours")
    else:
        print("Possible: Mixed colours")
else:
    print("Impossible")
