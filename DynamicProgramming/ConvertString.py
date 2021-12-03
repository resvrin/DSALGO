#BottomUp in Dynamic Programming

def findMinOperationBU(s1, s2, tempDict):
    for i1 in range(len(s1)+1):
        dictkey = str('i1') + '0'
        tempDict[dictkey]= i1
    for i2 in range(len(s2)+1):
        dictkey = '0' + str(i2)
        tempDict[dictkey] = i2

    for i1 in range(1, len(s1) +1):
        for i2 in range(1, len(s2) + 1):
            if s1[i1 -1] == s2[i2 -1]:
                dictkey = str(i1) +str(i2)
                dictkey1 = str(i1-1) + str(i2 -1)
                tempDict[dictkey] =tempDict[dictkey1]