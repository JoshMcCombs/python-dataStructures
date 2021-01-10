class BST_Node:
  '''
  Creates node objects used to build binary search tree.
  '''

  def __init__(self, val):
      self.val = val
      self.left = None
      self.right = None
      self.count = 1

  def __repr__(self):
      '''
      Allows for printable representation of a node.
      '''
      return f"val: {self.val}, count: {self.count}"


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

  def add_multiple(self, *args):
      """
      Accepts multiple arguments to add to tree.
      """
      for arg in args:
          self.add(arg)

  def search(self, val):
      '''
      Returns the node that contains the argument else false.
      '''
      if not self.root:
          return None
      else:
          current_node = self.root
          while True:
              if val == current_node.val:
                  return current_node
              elif val < current_node.val:
                  if not current_node.left:
                      return False
                  else:
                      current_node = current_node.left
              else:
                  if not current_node.right:
                      return False
                  else:
                      current_node = current_node.right

  def BreadthFirstTraverse(self):
      '''
      Travels the tree breadth first and returns a list in search order.
      '''
      current = self.root
      node_list = [current]
      travel_order = []
      while len(node_list):
          current = node_list.pop(0)
          travel_order.append(current.val)
          if current.left:
              node_list.append(current.left)
          if current.right:
              node_list.append(current.right)
      return travel_order

tree = BST()
tree.add_multiple(10,6,15,3,8,20)
print(tree.BreadthFirstTraverse())
