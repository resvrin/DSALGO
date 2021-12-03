def findMinOperation(s1, s2, idx1, idx2):
    if idx1 == len(s1):
        return len(s2)  - idx2
    if idx2 == len(s2):
        return len(s1) - idx1
    if s1[idx1] == s2[idx2]:
        return  findMinOperation(s1, s2, idx1 +1, idx2 + 1)
    else:
        deleteOp = 1 + findMinOperation(s1, s2, idx1, idx2 + 1)
        print(deleteOp)
        insertOp = 1 + findMinOperation(s1, s2, idx1 + 1, idx2)
        print(insertOp)
        replaceOp = 1 + findMinOperation(s1, s2, idx1 + 1, idx2 + 1)
        print(replaceOp)
        return min(deleteOp, insertOp, replaceOp)

print(findMinOperation("madhu", "reshma", 0, 0))