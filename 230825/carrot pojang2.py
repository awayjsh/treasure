T = int(input())

for tc in range(1,T+1) :

    N = int(input())

    arr = list(map(int,input().split()))

    max_carrot = max(arr)

    count_carrot = [0] * (max_carrot + 1)

    box = []

    for i in range(max_carrot + 1) :

        count_carrot[i] = arr.count(i)

    if N//2 < max(count_carrot) :

        print(f"#{tc} -1")
        continue

    