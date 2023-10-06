from itertools import combinations

def generate_combination(N):
    lst = [i for i in range(N)]
    k = N // 2
    all_combinations = list(combinations(lst, k))
    return all_combinations

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    combinations_lst = generate_combination(N)
    min_v = 1e9

    for part_combination in combinations_lst:
        A = 0
        B = 0

        full = [i for i in range(N)]

        another_combination = [x for x in full if x not in part_combination]

        for i in range(len(part_combination)) :

            for j in range(i+1, len(part_combination)) :

                A += arr[part_combination[i]][part_combination[j]] + arr[part_combination[j]][part_combination[i]]

        for i in range(len(another_combination)) :

            for j in range(i+1, len(another_combination)) :

                B += arr[another_combination[i]][another_combination[j]] + arr[another_combination[j]][another_combination[i]]

        if abs(A-B) <= min_v :

            min_v = abs(A-B)

    print(f"#{tc} {min_v}")
