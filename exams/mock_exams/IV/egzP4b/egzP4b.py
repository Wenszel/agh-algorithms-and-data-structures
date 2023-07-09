from egzP4btesty import runtests 

class Node:
  def __init__(self, key, parent):
    self.left = None
    self.right = None
    self.parent = parent
    self.key = key
    self.x = None

def min_BST(node):
  while node.left is not None:
    node = node.left
  return node.key


def max_BST(node):
  while node.right is not None:
    node = node.right
  return node.key


def succ(node):
  if node.right is not None:
    return min_BST(node.right)
  else:
    while node.parent.right == node:
      node = node.parent    
    return node.parent.key
  
def pred(node):
  if node.left is not None:
    return max_BST(node.left)
  else:
    while node.parent.left == node:
      node = node.parent
    return node.parent.key  
  
def walk(root, A):
  if root.left:
    walk(root.left, A)
  A.append(root.key)
  if root.right:
    walk(root.right, A)
    
def sol(root, T):
    A = []
    output = 0
    for node in T:
      a = pred(node)
      b = succ(node)
      if node.key * 2 == a + b:
        output += node.key
        
    return output
    
  
runtests(sol, all_tests = True)