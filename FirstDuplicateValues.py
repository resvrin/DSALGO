def firstDuplicateValue(array):
    for value in array:
        absValue = abs(value)
        if array[absValue - 1] < 0:
            print(absValue)
        array[absValue - 1] *= -1
    return -1


s = [2, 4, 2, 3, 3,5,6,7]

firstDuplicateValue(s)
