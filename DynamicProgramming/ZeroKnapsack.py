
#knapsack iterative method

def knapsack(profit, weight, m, n):
    k = [[0 for x in range(n + 1)] for y in range(m+1)]
    for i in range(n+1):
        for w in range(m+1):
            if i == 0 or w == 0:
                print(k)
                k[i][w] = 0
            elif weight[i-1] <= w:
                print(k)
                k[i][w] = max(k[i - 1][w-weight[i]], k[i-1][w] + profit[i])
            else:
                k[i][w] = k[i-1][w]

    return k[n][w]


profit = [1,2,5,6]
weight = [2,3,4,5]

print(knapsack(profit, weight, 4, 8))