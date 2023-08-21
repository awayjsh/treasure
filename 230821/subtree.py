T = int(input())



def preorder(n) :

    global count

    if n :

        count = count + 1
        preorder(ch1[n])
        preorder(ch2[n])

for tc in range(1,T+1) :

    count = 0

    E, N = map(int,input().split())
    arr = list(map(int, input().split()))
    V = max(arr)

    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)

    for i in range(E) :

        p,c = arr[i*2], arr[i*2+1]

        if ch1[p] == 0 :

            ch1[p] = c

        else :

            ch2[p] = c

    preorder(N)

    print(f"#{tc} {count}")

