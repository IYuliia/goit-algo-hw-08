import heapq

def min_connection_order(cables):
    
    heapq.heapify(cables)
    total_cost = 0
    merge_steps = []  

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        cost = first + second
        total_cost += cost

        merge_steps.append((first, second))

        heapq.heappush(cables, cost)

    return total_cost, merge_steps


cables = [5, 9, 1, 13, 2, 10]
cost, order = min_connection_order(cables)

print("Мінімальні витрати на об'єднання кабелів:", cost)
print("Порядок об'єднання кабелів:")
for step in order:
    print(f"З'єднано {step[0]} і {step[1]}")
