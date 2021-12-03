
S = [6,2,8,1,7,10, 78, 56, 34, 90, 11]
def insertionSort(S):

    for i in range(1, len(S)):
        k = S[i]
        j = i - 1
        while j >= 0 and k < S[j]:
            S[j+1] = S[j]
            j -= 1
        S[j+1] = k
    return S

print(insertionSort(S))