T = int(input())

def Tree(n) :

    global count

    if n <= N :

        Tree(n*2)
        tree[n] = count
        count = count + 1
        Tree(n*2+1)

for tc in range(1,T+1) :

    N = int(input())
    count = 1
    tree = [0] * (N+1)
    Tree(1)

    print(f"#{tc} {tree[1]} {tree[N//2]}")