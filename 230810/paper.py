T = int(input())

def fibo2(n) :

    f = [0] * (n)

    f[0] = 1
    f[1] = 3

    for i in range(2,n) :

        f[i] = f[i-1] + f[i-2] + f[i-2]

    return f[n-1]

for tc in range(1, T+1) :

    N = int(input()) // 10

    print(f"#{tc} {fibo2(N)}")