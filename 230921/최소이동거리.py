import heapq

T = int(input())

def dijkstra(start) :

    pq = []

    heapq.heappush(pq,(0,start))
    distance[start] = 0

    while pq :

        dist,now = heapq.heappop(pq)

        if distance[now] < dist :

            continue

        for next in graph[now] :

            next_node = next[0]
            cost = next[1]

            new_cost = dist + cost

            if distance[next_node] <= new_cost :

                continue

            distance[next_node] = new_cost
            heapq.heappush(pq,(new_cost,next_node))

for tc in range(1,T+1) :

    N, E = map(int,input().split())

    graph = [[] for i in range(N + 1)]

    for i in range(E) :

        f,t,w = map(int, input().split())
        graph[f].append([t,w])

    distance = [1e9] * (N + 1)

    dijkstra(0)
    print(f"#{tc} {distance[-1]}")



