from lab_06 import topological_sort
list_graph = [[1, 3], [2, 5], [4, 5], [1, 2], [], [4]]
costs = [[3, 5], [7, 4], [-1, 1], [2, 6], [], [-2]]
sorted_graph = topological_sort.topological_sort(list_graph)
print(sorted_graph)
inf = float('inf')
total_cost = [0, inf, inf, inf, inf, inf]
for u in sorted_graph:
    for v in range(len(list_graph[u])):
        print(u, list_graph[v])
        if total_cost[list_graph[u][v]] > total_cost[u] + costs[u][v]:
            total_cost[list_graph[u][v]] = total_cost[u] + costs[u][v]
print(total_cost)