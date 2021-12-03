
def houserobberBU(houses, currentidx):
    temp = [0] * (len(houses) + 2)
    for i in range(len(houses) -1, -1, -1):
        temp[i] = max(houses[i] + temp[i+2], temp[i+1])
    return temp[0]

array = [6, 7, 1, 30, 8, 2, 4]
print(houserobberBU(array, 0))
