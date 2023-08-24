T = int(input())

def enq(n) :

    global last
    last += 1
    h[last] = n
    c = last
    p = last // 2

    while p > 0 and h[p] > h[c] :

        h[p], h[c] = h[c], h[p]
        c = p
        p = c // 2

for tc in range(1,T+1) :

    N = int(input())
    nums = list(map(int,input().split()))
    h = [0] * (N+1)
    last = 0

    for num in nums :

        enq(num)