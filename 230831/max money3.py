T = int(input())

for tc in range(1,T+1) :

    num, N = input().split()
    card = list(map(int,num))
    N = int(N)
    max_v = 0
    memo = [0] * (10**len(card))
    f(0,N)
    print(f"#{tc} {}")

