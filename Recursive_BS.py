


def Recursive_BS(A, T, start, stop):
    if start == stop:
        if A[start] == T:
            return start
        else:
            return 0
    else:
        mid = (start + stop) // 2
        if A[mid] == T:
            return mid
        elif T < A[mid]:
            return Recursive_BS(A, T, start, mid -1)
        else:
            return Recursive_BS(A,T, mid +1 , stop)

A = [2,3,4,5,6,7,8,9,10]

print(Recursive_BS(A, 2, 0, len(A)))



