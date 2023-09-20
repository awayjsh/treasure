T = int(input())

def find_ans(start, N, idx):
    global ans

    if start == N:
        ans.add(tuple(idx))  # 리스트를 튜플로 변환하여 집합에 추가

    if start > N:
        return

    else:
        idx[0] += 1
        find_ans(start + 1, N, idx)
        idx[0] -= 1

        idx[1] += 1
        find_ans(start + 2, N,idx)
        idx[1] -= 1

        idx[2] += 1
        find_ans(start + 3, N,idx)
        idx[2] -= 1

for tc in range(1,T+1):
    N = int(input())
    ans = set()   # 결과값을 저장할 집합(set) 생성
    find_ans(0,N,[0,0,0])
    print(len(ans))
