
def findLcs(s1, s2, idx1, idx2):
    if idx1 == len(s1) or idx2 == len(s2):
        return 0
    if s1[idx1] == s2[idx2]:
        return 1 + findLcs(s1, s2, idx1 +1, idx2 + 1)
    else:
        op1 = findLcs(s1, s2, idx1 + 1, idx2)
        op2 = findLcs(s1, s2, idx1, idx2 + 1)
        return max(op1, op2)

print(findLcs("elephant", "erepat", 0, 0))
