N = int(input())

field = [list(map(int, input().split(" "))) for _ in range(N)]
flower = [[0] * N for _ in range (N)]

di = [0, 0, 1, 0, -1]
dj = [0, 1, 0, -1, 0]
ans = []
count = 0
total = 0

for i in range(0, N-1) :

    for j in range(0,N-1) :

        part_ans = []

        for k in range(5) :

            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < N :

                part_ans.append(field[ni][nj])

        if len(part_ans) == 5 :

            ans.append([sum(part_ans),[i,j]])

ans.sort()
print(ans)

for i in ans :

    is_empty = True

    for k in range(5) :

        ni = i[1][0] + di[k]
        nj = i[1][1] + dj[k]

        if flower[ni][nj] == 1 :

            is_empty = False

    if is_empty == True :

        for k in range(5):

            ni = i[1][0] + di[k]
            nj = i[1][1] + dj[k]

            flower[ni][nj] = 1

        count = count + 1
        total = total + i[0]

    if count == 3 :

        break

print(total)