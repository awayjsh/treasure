T = int(input())

for tc in range(1,T+1) :

    N = int(input())

    ans = []

    for i in range(1, N+1) :

        part = [1] * i
        ans.append(part)

    for i in range(2,N+1) :

        for j in range(1,i-1) :

            ans[i-1][j] = ans[i-2][j-1] + ans[i-2][j]

    print(f"#{tc}")

    for i in ans :

        for j in i :

            print(j,end = " ")
        print()