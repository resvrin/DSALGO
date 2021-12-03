
S = [4,6,3,7,2]
def selectionSort(S):
    for i in range(len(S)):
        min_idx = i
        for j in range(i + 1, len(S)):
            if S[min_idx] > S[j]:
                min_idx = j
        S[i], S[min_idx] = S[min_idx], S[i]
    return S

print(selectionSort(S))
