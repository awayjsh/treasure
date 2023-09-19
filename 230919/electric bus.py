T = int(input())

def f(i, end, cnt, charge) :

    global min_v

    if i == end :

        if min_v > cnt :

            min_v = cnt

    elif min_v <= cnt :

        return

    else :

        f(i+1, end, cnt+1, bus_stop[i]-1)

        if charge > 0 :

            f(i+1, end, cnt, charge-1)

for tc in range(1,T+1) :

    bus_stop = list(map(int, input().split()))
    min_v = bus_stop[0]
    cnt = 0

    f(2,bus_stop[0],0,bus_stop[1]-1)

    print(f"#{tc} {min_v}")

