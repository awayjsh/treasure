T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_count = 0

    for i in range(N):

        count = 0

        for j in range(M):

            if arr[i][j]:

                count = count + 1

            else:

                max_count = max(count, max_count)
                count = 0

            if j == M - 1:

                max_count = max(count, max_count)
                count = 0

    for j in range(M):

        count = 0

        for i in range(N):

            if arr[i][j]:

                count = count + 1

            else:

                max_count = max(count, max_count)
                count = 0

            if i == N - 1:

                max_count = max(count, max_count)
                count = 0

    print(f"#{tc} {max_count}")