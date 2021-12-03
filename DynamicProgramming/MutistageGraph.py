def multiStageGraph(n, stage, graph):
    cost = [float("inf") for i in range(len(n) + 1)]
    min_distance = [float("inf") for i in range(len(n) + 1)]
    path =  [float("inf") for i in range(len(n) + 1)]

    cost[n] = 0
    i = n - 1
    k = i + 1

    while i >= 1:
        while






INF = float("inf")
graph = [[INF, 1, 2, 5, INF, INF, INF, INF],
         [INF, INF, INF, INF, 4, 11, INF, INF],
        [INF, INF, INF, INF, 9, 5, 16, INF],
        [INF, INF, INF, INF, INF, INF, 2, INF],
        [INF, INF, INF, INF, INF, INF, INF, 18],
        [INF, INF, INF, INF, INF, INF, INF, 13],
        [INF, INF, INF, INF, INF, INF, INF, 2]]



