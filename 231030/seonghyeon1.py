
import heapq

def dijk(si,sj) :

    pq = []
    v[si][sj] = arr[si][sj]
    heapq.heappush(pq,(arr[si][sj],si,sj))

    while True :

        cost,i,j = heapq.heappop(pq)

        if cost > v[i][j] :

            continue

        for di, dj in ((0,1),(0,-1),(1,0),(-1,0)) :

            ni = i + di
            nj = j + dj

            if 0 <= ni < N and 0 <= nj < N :

                new_cost = arr[ni][nj] + cost

                if new_cost >= v[ni][nj] :

                    continue

                v[ni][nj] = new_cost
                heapq.heappush(pq,(new_cost,ni,nj))

while True :

    N = int(input())

    if N == 0 :

        break

    else :

        arr = [list(map(int,input().split())) for _ in range(N)]

        v = [int(1e9) * N for _ in range(N)]

        dijk(0,0)

        print(v[N-1][N-1])



        # 정성현 핵존잘 ㅇㅈ?
        # ㅇ ㅇㅈ
        