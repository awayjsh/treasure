T = int(input())

for tc in range(1,T+1) :

    arr = [list(map(str, input())) for _ in range(5)]
    ans = []

    i = -1

    count = 0
    while True :

        i = (i+1) % 5

        if len(arr[i]) != 0 :

            ans.append(arr[i].pop(0))

        else :

            count = count + 1

        if count == 5 :

            break

    print(f"#{tc} {''.join(ans)}")
