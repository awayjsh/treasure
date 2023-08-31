T = int(input())

def nCr(n,r,s,N,arr) :

    global ans

    if r == 0 :

        new_arr = []

        for i in arr:

            new_arr.append(i)

        new_arr[comb[0]], new_arr[comb[1]] =  new_arr[comb[1]],new_arr[comb[0]]

        value = 0

        for i in range(len(new_arr)) :

            value = value + new_arr[i] * (10 ** (len(arr) - i - 1))

        ans.append(value)
        nCr(n,r,s,N,new_arr)


    else :

        for i in range(s,n-r+1) :

            comb[r-1] = idx[i]
            nCr(n,r-1,i+1,N,arr)

for tc in range(1,T+1) :

    arr, N = map(int,input().split())

    arr = [int(a) for a in str(arr)]

    idx = [i for i in range(len(arr)-1,-1,-1)]

    comb = [0] * 2

    ans = []

    nCr(len(arr),2,0,N,arr)

    print(ans)

    print(f"#{tc} {max}")