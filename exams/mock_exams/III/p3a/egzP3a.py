from egzP3atesty import runtests

class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt 
    self.fundusze = fundusze 
    self.x = None
def wybory(T):
  
  
  def node_to_list(node: Node) -> list[tuple[int, int, int]]:
    array = []
    while node is not None:
      array.append((node.wyborcy, node.koszt, node.fundusze))
      node = node.next
    return array
  
  
  def knapsack(P: list[int], W: list[int], w: int) -> int:
    n = len(P)
    F = [[0 for _ in range(w + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(w + 1):
            if j == 0 or i == 0:
                F[i][j] = 0
            elif j - W[i-1] >= 0:
                F[i][j] = max(F[i-1][j], F[i-1][j-W[i-1]] + P[i-1])
            else:
                F[i][j] = F[i-1][j]
    return F[n][w]
  
  total = 0
  for wybory in T:
      a = node_to_list(wybory)
      profits = [x[0] for x in a]
      costs = [x[1] for x in a]
      funds = a[0][2]
      total += knapsack(profits, costs, funds)
  return total

runtests(wybory, all_tests = True)