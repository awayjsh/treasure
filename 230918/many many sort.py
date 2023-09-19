def qsort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        qsort(A, l, s - 1)
        qsort(A, s + 1, r)


def partition(A, l, r):
    p = A[l]  # 가장 왼쪽 원소를 피봇으로 하는 경우
    i = l
    j = r
    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j


arr = list(map(int, input().split()))
qsort(arr, 0, len(arr) - 1)
print(arr[500000])