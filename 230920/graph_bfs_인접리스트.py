# graph = [
#     [0,1,0,1,0],
#     [1,0,1,1,1],
#     [0,1,0,0,0],
#     [1,1,0,0,1],
#     [0,1,0,1,0]
# ]

# 주의 사항 : 각 노드마다 갈 수 있는 지점의 개수가 다르다
# 메모리 적으로 인접 행렬에 비해 훨씬 효율적이다.

# graph = {
#     '0' : [1,3],
#     '1' : [0,2,3,4],
#     '2' : [1],
#     '3' : [0,1,4],
#     '4' : [1,3]
# }

graph = [
    [1,3],
    [0,2,3,4],
    [1],
    [0,1,4],
    [1,3]
]

# DFS
# Stack 버전

def dfs_stack(start) :

    visited = []
    stack = [start]

    while stack :

        now = stack.pop()

        # 이미 방문한 지점이라면 pass

        if now in visited :

            continue

        # 방문하지 않은 지점이라면, 방문 표시
        visited.append(now)

        # 갈 수 있는 곳들을 stack에 추가
        # 작은 번호 부터 조회
        # for next in range(4,-1,-1) :

        for to in range(len(graph[now])-1,-1,-1) :

            next = graph[now][to]

            # # 연결이 안되어 있다면 continue
            # if graph[now][next] == 0 :
            #
            #     continue

            # 방문한 지점이라면 stack에 추가하지 않음

            if next in visited :

                continue

            stack.append(next)

    return visited

print("dfs stack = ", end = "")
print(*dfs_stack(0))

# 재귀 버전
# map 크기를 알 때 append 형식 말고, visited를 사용하는 것이 더 유리
visited = [0] * 5
path = []

def dfs(now) :

    visited[now] = 1
    print(now, end = " ")

    # 인접한 노드들을 방문

    for to in range(len(graph[now])) :

        next = graph[now][to]

        # if graph[now][next] == 0 :
        #
        #     continue

        if visited[next] :

            continue

        dfs(next)

    return visited

print('dfs 재귀 = ', end = "")
dfs(0)