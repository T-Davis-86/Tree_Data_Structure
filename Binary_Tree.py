class bin_node:
  def __init__(self,value):
    self.value = value
    self.right = None
    self.left = None

class Bin_tree:
    def __init__(self,root):
        self.root = bin_node(root)

    def insert(self,value):
        self._insert_recursive(self.root,value)

    def _insert_recursive(self,current_node,value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = bin_node(value)
            else:
                self._insert_recursive(current_node.left,value)
        else:
            if current_node.right is None:
                current_node.right = bin_node(value)
            else:
                self._insert_recursive(current_node.right,value)

    def display_tree(self, root):
        if root is not None:
            self.display_tree(root.left)
            print(root.value, end=' ')
            self.display_tree(root.right)

    def search_tree(self,current_node, value):
        if current_node is None:
            print("False")
            return False
        if current_node.value == value:
            print("True")
            return True
        elif current_node.value > value:
            return self.search_tree(current_node.left, value)
        else:
            return self.search_tree(current_node.right, value)
        
    def find_min(self,node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def delete_node(self,root,value):
        if root is None:
            print("Not in Tree")
            return root
        if value < root.value:
            root.left = self.delete_node(root.left, value)
        elif value > root.value:
            root.right = self.delete_node(root.right, value)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            else:
                temp = self.find_min(root.right)
                root.value = temp.value
                root.right = self.delete_node(root.right,temp.value)
                return root
        return root

        