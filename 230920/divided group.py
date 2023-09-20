T = int(input())

def find_set(x) :

    if parent[x] == x :

        return x

    parent[x] = find_set(parent[x])

    return parent[x]

def union(x,y) :

    x = find_set(x)
    y = find_set(y)

    # if x == y :
    #
    #     return

    if x < y :

        parent[y] = x

    else :

        parent[x] = y

for tc in range(1,T+1) :

    N, M = map(int, input().split())

    arr = list(map(int, input().split()))

    parent = [i for i in range(N+1)]

    for i in range(M) :

        union(arr[i*2],arr[i*2+1])

    ans_set = set()

    for i in range(N+1) :

        ans_set.add(find_set(i))

    print(f"#{tc} {len(ans_set) - 1}")


