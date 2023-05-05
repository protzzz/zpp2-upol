class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_helper(value, self.root)
            
    def _insert_helper(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value, parent=current_node)
            else:
                self._insert_helper(value, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = Node(value, parent=current_node)
            else:
                self._insert_helper(value, current_node.right)
