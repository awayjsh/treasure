def solution(n, wires):
    answer = -1

    graph = [[0] * (n + 1) for _ in range(n+1)]

    for i in wires :

        graph[i[0]][i[1]] = 1
        graph[i[1]][i[0]] = 1

    return answer


n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]

solution(n,wires)