def qsort(A,l,r) :

    if l < r :

        s = partition(A,l,r)
        qsort(A,l,s-1)
        qsort(A,s+1,r)

def partition(A,l,r) :

    p = A[l]
    idx = l

    pivot = 0

    if A[l] <= A[(l+r)//2] and A[(l+r)//2] <= A[r] :

        pivot = (l+r)//2

    elif A[(l+r)//2] <= A[l] and A[l] <= A[r] :

        pivot = l

    else :

        pivot = r

    A[pivot], A[l] = A[l], A[pivot]


    i = l
    j = r

    while i <= j :

        while i <= j and A[i] <= p :

            i += 1

        while i <= j and A[i] >= p :

            j -= 1

        if i < j :

            A[i], A[j] = A[j], A[i]

    A[l],A[j] = A[j],A[l]
    return j

arr = [i for i in range(1,10)]
qsort(arr,0,len(arr)-1)
print(arr)
