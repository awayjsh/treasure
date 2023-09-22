T = int(input())

def recur(acc_month, acc_price,mon,mon_3,year) :

    global min_v

    if acc_month > 12 :

        if min_v >= acc_price :

            min_v = acc_price

            return
    else :
        recur(acc_month + 3, acc_price + mon_3,mon,mon_3,year)
        recur(acc_month + 1, acc_price + min(mon,arr[acc_month] * day),mon,mon_3,year)

for tc in range(1,T+1) :

    day,one_month,three_month,year = map(int,input().split())

    arr = [0] + list(map(int,input().split()))

    min_v = year

    recur(1,0,one_month,three_month,year)

    print(f"#{tc} {min_v}")