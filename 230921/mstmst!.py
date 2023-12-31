T = int(input())

def find_set(x) :

    if parents[x] == x :

        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y) :

    x = find_set(x)
    y = find_set(y)

    if x == y :

        return

    if x < y :

        parents[y] = x

    else :

        parents[x] = y

for tc in range(1,T+1) :

    V,E = map(int,input().split())

    edge = []

    for _ in range(E) :

        f,t,w = map(int, input().split())
        edge.append([f,t,w])

    edge.sort(key = lambda x : x[2])

    parents = [i for i in range(V + 1)]

    cnt = 0

    sum_weight = 0

    for f,t,w in edge :

        if find_set(f) != find_set(t) :

            cnt += 1
            sum_weight += w
            union(f,t)

            if cnt == V + 1 :

                break

    print(f"#{tc} {sum_weight}")