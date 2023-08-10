# graph = dict()
#
# graph['A'] = ['B', 'C']
# graph['B'] = ['A', 'D']
# graph['C'] = ['A', 'G', 'H', 'I']
# graph['D'] = ['B', 'E', 'F']
# graph['E'] = ['D']
# graph['F'] = ['D']
# graph['G'] = ['C']
# graph['H'] = ['C']
# graph['I'] = ['C', 'J']
# graph['J'] = ['I']
#
#
# def dfs(graph, start_node):
#     ## 기본은 항상 두개의 리스트를 별도로 관리해주는 것
#     need_visited, visited = list(), list()
#
#     ## 시작 노드를 시정하기
#     need_visited.append(start_node)
#
#     ## 만약 아직도 방문이 필요한 노드가 있다면,
#     while need_visited:
#
#         ## 그 중에서 가장 마지막 데이터를 추출 (스택 구조의 활용)
#         node = need_visited.pop()
#
#         ## 만약 그 노드가 방문한 목록에 없다면
#         if node not in visited:
#             ## 방문한 목록에 추가하기
#             visited.append(node)
#
#             ## 그 노드에 연결된 노드를
#             need_visited.extend(graph[node])
#
#     return visited
#
# print(dfs(graph, "A"))


'''
V E
v1 w1 v2 w2 ...
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(n, V, adj_m) :

    stack = [] # stack 생성
    visited = [0] * (V+1) # visited 생성
    visited[n] = 1 # 시작점 방문 표시
    print(n)
    while True :

        # print('adj',adj_m[n])
        for w in range(1, V+1) :
            if adj_m[n][w] == 1 and visited[w] == 0 : # 현재 정점 n에 인접하고 미방문 w 찾기
                # print('!',end=' ')
                stack. append(n)
                n = w
                print(n)
                visited[n] = 1
                break

        else :
            if stack :
                # print('!!')

                n = stack.pop()

            else :
                print('end')
                break
        # print('?', visited)
    return




V, E = map(int, input().split()) # V : 정점 개수, E : path 개수
arr = list(map(int, input().split()))
adj_m = [[0] * (V+1) for _ in range (V+1)]

for i in range(E) :

    v1, v2 = arr[i*2], arr[i*2+1]

    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1
# print('adj_m',adj_m[5])

dfs(1, V, adj_m)