


def quickSort(A, a, b):
    if a >= b:
        return
    pivot = A[b]
    left = a
    right = b - 1
    while left <= right:
        while left <= right and A[left] < pivot:
            left += 1
        while left <= right and pivot < A[right]:
            right -= 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left,right = left + 1, right + 1
    A[left], A[b] = A[b], A[left]
    quickSort(A, a, left - 1)
    quickSort(A, left + 1, b )
    return A

A = [6, 2, 8, 1, 7, 10, 78, 56, 34, 90, 11]

print(quickSort(A, 0, len(A) - 1))


