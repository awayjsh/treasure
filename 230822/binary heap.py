def insert(k) :

    global H

    H.append(k)
    percolate_up()

def percolate_up() :

    global H

    i = len(H) - 1
    parent = i // 2

    while parent > 0 :

        if H[i] < H[parent] :

            H[parent], H[i] = H[i], H[parent]

        i = parent
        parent = i // 2

T = int(input())

for tc in range(1,T+1) :

    N = int(input())

    arr = list(map(int,input().split()))

    H = [0]

    for i in arr :

        insert(i)

    ans = 0

    while True :

        N = N // 2
        ans = ans + H[N]

        if N <= 1 :

            break

    print(f"#{tc} {ans}")