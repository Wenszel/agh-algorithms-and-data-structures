from egz1btesty import runtests

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow


def wideentall( T ):
      
  def assign_nodes_to_levels(el, level=0):
    nonlocal levels_size
    if levels_size < level + 1:
      levels_size = level + 1
      levels.append([el])
    else:
      levels[level].append(el)
    if el.left is not None:
      assign_nodes_to_levels(el.left, level+1)
    if el.right is not None:
      assign_nodes_to_levels(el.right, level+1)
        
  def cutting_DFS(node):
    nonlocal output    
    if node.left is not None and node.left.x == None:
      output += 1
    if node.right is not None and node.right.x == None:
      output += 1
    if node.left is not None and node.left.x:
      cutting_DFS(node.left)
    if node.right is not None and node.right.x:
      cutting_DFS(node.right)
    
  levels = []
  levels_size = 0
  assign_nodes_to_levels(T)
  widths = [len(levels[i]) for i in range(levels_size)]
  maximum = max(widths)
  index = 0
  for i in range(levels_size-1, -1, -1):
    if maximum == widths[i]:
      index = i
      break
  
  for node in levels[index]:
    node.x = True
  
  for level in range(index - 1, -1, -1):
    for node in levels[level]:
      if node.left is not None and node.left.x:
        node.x = True
      if node.right is not None and node.right.x:
        node.x = True
  output = 0
  cutting_DFS(T)
  return output

runtests( wideentall, all_tests = True )
