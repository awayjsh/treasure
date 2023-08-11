T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

max_count = 0
for i in range(N):
    j = 0
    count = 0
    while j < M:
        if arr[i][j] == 1:
            j += 1
            count += 1
        else:
            if max_count <= count:
                max_count = count
                count = 0
                j += 1
                # print(i, j, count)

for i in range(M):
    j = 0
    count = 0
    while j < N:
        if arr[j][i] == 1:
            j += 1
            count += 1
        else:
            if max_count <= count:
                max_count = count
                count = 0
                j += 1
                # print(j,i, count)


print(f'#{tc} {max_count}')