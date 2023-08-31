T = int(input())

for tc in range(1,T+1) :

    N, M = map(int,input().split())

    box = list(map(int,input().split()))

    truck = list(map(int,input().split()))

    box.sort()
    box.reverse()
    truck.sort()
    truck.reverse()
    i = 0
    j = 0
    ans = 0

    while True :

        if box[i] <= truck[j] :

            ans = ans + box[i]
            i += 1
            j += 1

        else :

            i += 1

        if j == M or i == N:

            break

    print(f"#{tc} {ans}")