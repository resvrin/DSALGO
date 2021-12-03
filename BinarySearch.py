def binarysearch(A, target):
    start = 0
    stop = len(A)

    #print(start,stop,mid)
    while start <= stop:
        mid = (start + stop) // 2
        if target == A[mid]:
            return mid
        elif target < A[mid]:
            stop = mid -1

        else:
            start = mid + 1




    return 0

A = [2,3,4,5,6,7,8,9,10]
print(binarysearch(A, 10))
