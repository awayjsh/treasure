T = int(input())

def find_food(cal, score, count,idx) :

    global max_v

    if count <= N and cal <= L:

        if score >= max_v :

            max_v = score

    if cal > L :

        return

    if count > N :

        return

    else :

        for i in range(len(food)) :

            if idx[i] == 0 :

                idx[i] += 1
                find_food(cal + food[i][1], score + food[i][0], count + 1,idx)
                idx[i] -= 1

for tc in range(1,T+1) :

    N, L = map(int,input().split())

    food = [list(map(int,input().split())) for _ in range(N)]

    max_v = 0

    food_idx = [0]*N
    find_food(0,0,0, food_idx)

    print(f"#{tc} {max_v}")