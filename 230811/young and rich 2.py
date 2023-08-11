T = int(input())

for tc in range(1,T+1) :

    N = int(input())

    arr = list(map(int,input().split()))

    ans = 0

    for i in reversed(range(N)) :

        if i == N-1 :

            max = arr[i]
            continue

        if arr[i] < max :

            ans = ans + (max - arr[i])

        elif arr[i] >= max :

            max = arr[i]
            continue

    print(f"#{tc} {ans}")