T = int(input())

for tc in range(1,T+1) :

    arr, N = map(int,input().split())

    arr = [int(a) for a in str(arr)]

    idx = [i for i in range(len(arr)-1,-1,-1)]

    for i in range(N) :

        max_v = 0
        max_idx = 0

        for j in range(i + 1, len(arr)) :

            if max_v < arr[j] :

                max_v = arr[j]
                max_idx = j

        if arr[i] != arr[max_idx] :

            arr[i], arr[max_idx] = arr[max_idx], arr[i]

        print(arr)