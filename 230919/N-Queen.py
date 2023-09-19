def isPromsing(x) :

    for i in range(x) :

        if queen[x] == queen[i] or abs(queen[x] - queen[i]) == x-i :

            return False

    return True

T = int(input())

for tc in range(1,T+1) :

    n = int(input())
    queen = [0] * n
    cnt = 0

    def dfs(x) :

        global cnt

        if x == n :

            cnt += 1

            return

        else :

            for i in range(n) :

                queen[x] = i

                if isPromsing(x) :

                    dfs(x+1)

    dfs(0)
    print(f"#{tc} {cnt}")