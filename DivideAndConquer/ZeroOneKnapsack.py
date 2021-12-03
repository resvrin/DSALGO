class Items:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight


def zoKnapsack(items, capacity, currentidx):
    if capacity <= 0 or currentidx < 0 or currentidx >= len(items):
        return 0
    elif items[currentidx].weight <= capacity:
        profit1 = items[currentidx].profit + zoKnapsack(items, capacity - items[currentidx].weight, currentidx + 1)
        profit2 = zoKnapsack(items, capacity, currentidx + 1)
        return max(profit1, profit2)
    else:
        return 0

mango = Items(31, 3)
apple = Items(26, 1)
orange = Items(17, 2)
banana = Items(72, 5)
items = [mango, apple, orange, banana]
print(zoKnapsack(items, 7, 0))
