class BST_Node:
  '''
  Creates node objects used to build binary search tree.
  '''
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.count = 1

class BST:
  '''
  Implimentation of a binary search tree.
  '''
  def __init__(self):
    self.root = None

  def add(self, val):
    '''
    Adds a value to the tree, if the value is less than the leaf of the tree it becomes .left edge else .right.
    '''
    new_node = BST_Node(val)
    if not self.root:
      self.root = new_node
    else:
      current_node = self.root
      while True:
        if val == current_node.val:
          self.count += 1
          return
        elif val < current_node.val:
          if current_node.left:
            current_node = current_node.left
          else:
            current_node.left = new_node
            return
        else:
          if current_node.right:
            current_node = current_node.right
          else:
            current_node.right = new_node
            return
