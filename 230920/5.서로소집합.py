# 1 ~ 10
# make set

parent = [i for i in range(10)]

# find

def find_set(x) :

    if parent[x] == x :

        return x

    # return find_set(parent[x])

    parent[x] = find_set(parent[x])

    return parent[x]

# union

def union(x,y) :

    x = find_set(x)
    y = find_set(y)

    if x == y :

        print("싸이클 발생")

        return

    if x < y :

        parent[y] = x

    else :

        parent[x] = y

union(0,1)

union(2,3)

union(0,2)

print(find_set(2))
print(find_set(3))

t_x = 0
t_y = 1

if find_set(t_x) == find_set(t_y) :

    print("같은 집합에 속해요")

else :

    print("안 속해요!")

