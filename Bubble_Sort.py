
def bubblesort(L):
    for i in range(len(L) - 1):
        for j in range(len(L) -i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    return L

L = [67, 4, 2, 4, 7,1,9, 50]

print(bubblesort(L))
