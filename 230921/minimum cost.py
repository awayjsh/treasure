import heapq

T = int(input())

def dijkstra(i,j) :

    pq = []

    heapq.heappush(pq,(0,i,j))

    distance[i][j] = 0

    di = [0,0,-1,1]
    dj = [1,-1,0,0]

    plus = 0

    while pq :

        dist,now_i,now_j = heapq.heappop(pq)

        if distance[now_i][now_j] < dist :

            continue

        for n in range(4) :

            ni = now_i + di[n]
            nj = now_j + dj[n]

            if 0 <= ni < N and 0 <= nj < N:

                if arr[ni][nj] > arr[now_i][now_j] :

                   plus = arr[ni][nj] - arr[now_i][now_j]

                new_cost = dist + plus + 1

                plus = 0

                if distance[ni][nj] <= new_cost :

                    continue

                distance[ni][nj] = new_cost
                heapq.heappush(pq,(new_cost,ni,nj))

for tc in range(1,T+1) :

    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    distance = [[1e9] * N for _ in range(N)]

    dijkstra(0,0)

    print(f"#{tc} {distance[N-1][N-1]}")