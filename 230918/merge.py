# 병합
def merge(l, mid, r):
    global cnt

    left = l  # 왼쪽 구간 시작 위치
    right = mid + 1  # 오른쪽 구간 시작 위치
    tidx = l

    if arr[mid] > arr[r] and :

        cnt += 1

    while left <= mid and right <= r:
        if arr[left] <= arr[right]:
            temp[tidx] = arr[left]
            left += 1

        else:
            temp[tidx] = arr[right]
            right += 1
        tidx += 1

    while left <= mid:
        temp[tidx] = arr[left]
        left += 1
        tidx += 1

    while right <= r:
        temp[tidx] = arr[right]
        right += 1
        tidx += 1

    for i in range(l, r + 1):
        arr[i] = temp[i]


# 분할
def merge_sort(l, r):
    if l < r:
        mid = (l + r) // 2

        merge_sort(l, mid)

        merge_sort(mid + 1, r)

        merge(l, mid, r)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    arr = list(map(int, input().split()))

    cnt = 0

    temp = [0] * N

    merge_sort(0, N - 1)

    print(f'#{tc} {arr[N // 2]} {cnt}')
