T = int(input())

for tc in range(1,T+1) :

    N = int(input())

    arr = list(map(int,input().split()))

    max_carrot = max(arr)

    count_carrot = [0] * (max_carrot + 1)

    box = []

    sml = [[] for _ in range(3)]

    for i in range(max_carrot + 1) :

        count_carrot[i] = arr.count(i)

    if N//2 < max(count_carrot) :

        print(f"#{tc} -1")
        continue

    for i in range(N//2,0,-1) :

        for j in range(0,i+1) :

            part = []
            part.append(i)

            if i + j >= N :

                part = []
                break

            else :

                part.append(j)
                part.append(N-i-j)

            if 0 in part or N//2 < max(part) :

                continue

            else :

                part.sort()

                box.append(part)

    idx = 0
    eight = 0
    ans = 100000000000000000000000
    is_break = False
    lenlen = []

    for i in box :

        for j in i :

            for k in range(j) :

                sml[idx].append(arr[eight])
                eight = (eight + 1) % N

                if arr[eight] == arr[(eight + 1) % N] :

                    print(f"#{tc} -1")
                    is_break = True
                    break

            if is_break == True :

                break

            idx = (idx + 1) % 3

        if is_break == True :

            break


        print(sml)
        sml = [[] for _ in range(3)]
        is_break = False





