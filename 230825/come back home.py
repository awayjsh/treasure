T = int(input())

for tc in range(1,T+1) :

    N = int(input()) # 학생 수

    arr = [list(map(int,input().split())) for _ in range(N)]

    cnt = [0] * 201 # 방 사이 공간을 지나는 사람 수

    for a, b in arr : # a <= b 라는 보장이 없음

        a = (a + a % 2) // 2
        b = (b + b % 2) // 2

        for i in range(min(a,b), max(a,b)+1) :

            cnt[i] += 1


    print(f"#{tc} {max(cnt)}")
