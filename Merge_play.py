
def merge(S1, S2, S):
    """Merge two sorted list S1 and S2 to S"""
    i = j = 0
    while i + j < len(S):
        if j == len(S) or (i < len(S)) or S1[i] < S2[j]:
            print(S)
            S[i + j] = S1[i]
            i += 1
        else:
            S[i + j] = S2[j]
            j += 1
    return S
def merge_sort(S):
    n = len(S)
    if n < 2:
        return 0
    mid =  n //2
    S1 = S[0:mid]
    S2 = S[mid +1: n]
    merge_sort(S1)
    merge_sort(S2)
    merge(S1,S2,S)

S = [6,7,4,65,55, 345,3,2,4,6]
print(merge_sort(S))




