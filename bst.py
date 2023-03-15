
class BSTNode:
    def __init__(self, val):
        self.value = val
        self.right = None
        self.left = None
        self.parent = None
        
    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()
        
    def __str__(self):
        return "(" + str(self.value) + ")"

    def __repr__(self):
         return "(" + str(self.value) + ")"
        
class BST:
    def __init__(self):
        self.root = None
        
    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))
    
    def insert_list(self, L:list):
        for i in L:
            self.insert(i)
        
    def insert(self, val):
        if self.root == None:
            self.root = BSTNode(val)
        else:
            self.__insert(self.root, val)
            
    def __insert(self, node, val):
        if val < node.value:
            if node.left == None:
                node.left = BSTNode(val)
                node.left.parent = node
            else:
                self.__insert(node.left, val)
        else:
            if node.right == None:
                node.right = BSTNode(val)
                node.right.parent = node
            else:
                self.__insert(node.right, val)
                
    def __str__(self):
        if self.is_empty():
            return "[]"
        return self.__str_helper(self.root)

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"