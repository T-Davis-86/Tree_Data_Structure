class node_Tree:
  def __init__(self,value):
    self.value = value
    self.children = []

  def add_child(self,child):
    self.children.append(child)

class Gen_tree:
  def __init__(self,root):
    self.root = root

  def preorder_list(self,node = None):
    if node is None:
      node = self.root  
    result = [node.value]
    for child in node.children:
      result.extend(self.preorder_list(child))
    return result
  
  def postorder_list(self,node = None):
    if node is None:
      node = self.root
    result = []
    for child in node.children:
      result.extend(self.postorder_list(child))
    result.append(node.value)
    return result    
        
  def display_tree_preorder(self,node = None, level = 0):
    if node is None:
      node = self.root
    print("_" * level + str(node.value))
    for child in node.children:
      self.display_tree_preorder(child,level+1)

  
  def display_tree_postorder(self,node = None, level = 0):
    if node is None:
      node = self.root
    if len(node.children) == 0:
      pass
    for child in node.children:
      self.display_tree_postorder(child,level+1)
    print("_" * level + str(node.value))