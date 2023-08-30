def f(i,N,K) :

    global min

    if i == N :

        d = []

        for i in p:

            d.append(i)

        stack = []
        stack.append((arr[0],arr[1]))
        total = 0
        is_break = True

        while is_break :

            if len(d) != 0 :

                stack.append((arr[d[0]],arr[d[0]+1]))

            else :

                stack.append((arr[2],arr[3]))
                is_break = False

            x2, y2 = stack.pop()
            x1, y1 = stack.pop()

            total = total + abs(x1 - x2) + abs(y1 - y2)

            if len(d) != 0 :

                n = d.pop(0)
                stack.append((arr[n],arr[n+1]))


        if min >= total :

            min = total

    else :

        for j in range(N) :

            if used[j] == 0 :

                p[i] = spot[j]
                used[j] = 1
                f(i+1,N,K)
                used[j] = 0

T = int(input())

for tc in range(1,T+1) :

    N = int(input())

    arr = list(map(int,input().split()))

    spot = [i for i in range(4,(N+2)*2-1,2)]

    K = len(spot)

    used = [0] * K
    p = [0] * K

    min = 1e9

    f(0,K,K)

    print(f"#{tc} {min}")