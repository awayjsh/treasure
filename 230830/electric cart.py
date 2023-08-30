def f(i, N, K) :

    global min

    if i == K :

        distance = []

        for i in p :
            
            distance.append(i)

        stack = []
        stack.append(0)
        total = 0
        is_break = True

        while is_break :

            if len(distance) != 0 :
                stack.append(distance[0])
            else :
                stack.append(0)
                is_break = False

            j = stack.pop()
            i = stack.pop()

            total = total + arr[i][j]

            if len(distance) != 0 :
                stack.append(distance.pop(0))

        if min >= total :

            min = total

    else :

        for j in range(N) :

            if used[j] == 0 :

                p[i] = card[j]
                used[j] = 1
                f(i+1, N, K)
                used[j] = 0

T = int(input())

for tc in range(1,T+1) :

    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    card = [i for i in range(1, N)]

    K = len(card)

    used = [0] * K
    p = [0] * K

    min = 1e9

    f(0,K,K)

    print(f"#{tc} {min}")
