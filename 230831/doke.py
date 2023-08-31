T = int(input())

for tc in range(1,T+1) :

    N = int(input())

    meet = []

    for _ in range(N) :

        s,f = map(int,input().split())

        meet.append([s,f])

    meet.sort(key = lambda x : x[1])

    meet = [[0,0]] + meet

    s = [1]
    j = 1

    for i in range(1,N+1) :

        if meet[i][0] >= meet[j][1] :

            s.append(i)
            j = i

    print(f"#{tc} {len(s)}")