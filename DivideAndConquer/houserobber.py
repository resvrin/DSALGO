array = [6, 7, 1, 30, 8, 2, 4, 150, 9, 80]
houses = [75 , 105, 120, 75, 90, 135]
def houserobber(houses, currentidx):
    if currentidx >= len(houses):
        return 0
    else:
        stealfirst = houses[currentidx] + houserobber(houses, currentidx + 2)
        skipfirst = houserobber(houses, currentidx + 1)
        #print(currentidx)
        return max(stealfirst, skipfirst)

print(houserobber(houses, 0))