T = int(input())
ans = []

def battle(N,arr) :

    global ans

    # print(N,arr,ans)

    N = len(arr)

    if len(arr) == 2 :

        if (arr[0][1] == 1 and arr[1][1] == 3) or (arr[0][1] == 2 and arr[1][1] == 1) or (arr[0][1] == 3 and arr[1][1] == 2) :

            ans.append(arr[0])

        elif (arr[0][1] == 3 and arr[1][1] == 1) or (arr[0][1] == 1 and arr[1][1] == 2) or (arr[0][1] == 2 and arr[1][1] == 3) :

            ans.append(arr[1])

        elif (arr[0][1] == 3 and arr[1][1] == 3) or (arr[0][1] == 2 and arr[1][1] == 2) or (arr[0][1] == 1 and arr[1][1] == 1) :

            if arr[0][0] > arr[1][0] :

                ans.append(arr[1])

            elif arr[0][0] < arr[1][0] :

                ans.append(arr[0])

    elif len(arr) == 1 :

        ans.append(arr[0])

    else :

        if N // 2 == 0 :

            return

        if (N // 2) % 2 == 1 :

            battle(N//2, arr[:(N//2)+1])
            battle(N//2, arr[(N//2)+1:])

        else :

            battle(N // 2, arr[:(N // 2)])
            battle(N // 2, arr[(N // 2):])

    if len(ans) == 2 :

        n2 = ans.pop()
        n1 = ans.pop()
        battle(2,[n1,n2])

    return

for tc in range(1,T+1) :

    N = int(input())

    arr = list(map(int, input().split()))

    idx = [i for i in range(1,N+1)]

    idx_arr = [[idx[i], arr[i]] for i in range(0, N)]

    battle(N,idx_arr)

    print(f"#{tc} {ans[0][0]}")