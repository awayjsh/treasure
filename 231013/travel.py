N = int(input())

M = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

city = list(map(int,input().split()))

parents = [i for i in range(N)]

cnt = 0

