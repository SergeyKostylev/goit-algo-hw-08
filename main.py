import heapq


def get_min_cost_to_connect_cables(cables_list: list) -> int:
    heapq.heapify(cables_list)

    res = 0

    while len(cables_list) > 1:
        first = heapq.heappop(cables_list)
        second = heapq.heappop(cables_list)

        cost = first + second
        res += cost

        heapq.heappush(cables_list, cost)

    return res


cables = [1, 7, 9, 10, 15]
print(f"Min cost: {get_min_cost_to_connect_cables(cables)}")
