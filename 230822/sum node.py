T = int(input())

for tc in range(1,T+1) :

    N, M, L = map(int,input().split())

    H = [0] * (N+1)

    for i in range(M) :

        leaf, num = map(int,input().split())

        H[leaf] = num

    parent = N // 2

    while True :

        if parent * 2 + 1 <= N :

            H[parent] = H[parent * 2] + H[parent * 2 + 1]

        else :

            H[parent] = H[parent * 2]

        if parent == 1 :

            break

        parent -= 1

    print(f"#{tc} {H[L]}")