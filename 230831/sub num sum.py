T = int(input())

def subset(i,N) :

    global count

    if i == N :

        s = 0

        for j in range(N) :

            if bit[j] :

                s += arr[j]

        if s == K :

            count = count + 1

        return

    else :

        bit[i] = 1
        subset(i+1, N)
        bit[i] = 0
        subset(i+1, N)

        return

for tc in range(1,T+1) :

    N, K = map(int,input().split())

    arr = list(map(int,input().split()))

    bit = [0] * N

    count = 0

    subset(0,N)

    print(f"#{tc} {count}")