#the given n number , number of ways can be using 1, 3, 4
#Using Top Down Method using dynamic programming
def numberFactorTD(n, dp):
    if n in [0,1,2]:
        return 1
    if n == 3:
        return 2
    else:
        if n not in dp:
            rec1 = numberFactor(n-1, dp)
            rec2 = numberFactor(n-3, dp)
            rec3 = numberFactor(n-4, dp)
            dp[n] = rec1 + rec2 + rec3
            print(dp)
        return dp[n]

#print(numberFactor(5, {}))

#Using Bottom Up method using dynamic programming

def numberFactorBU(n):
    temp = [1, 1, 1, 2]
    for i in range(4, n + 1):
        temp.append(temp[i - 1] + temp[i - 3]+ temp[i - 4])
    return temp[n]
print(numberFactorBU(5))
