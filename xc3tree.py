class XC3Node:
    def __init__(self, degree):
        self.degree = degree
        self.children = [(XC3Node(0) if i <= 2 else XC3Node(i-2)) for i in range(1, self.degree+1)]
    def is_leaf(self):
        return self.children == []
    def rightmost_child(self):
        return self.children[-1]

class XC3Tree:
    def __init__(self, degree):
        self.root = XC3Node(degree)
    def is_empty(self):
        return self.root == None
    def get_height(self):
        if self.root.degree == 0:
            return 1
        return self._get_height(self.root)
    
    def _get_height(self, node):
        if node.degree == 0:
            return 1
        return 1 + self._get_height(node.rightmost_child())
    def get_degree(self):
        return self.root.degree
    def number_of_nodes(self):
        return self._number_of_nodes(self.root)
    def _number_of_nodes(self, node):
        if node.degree == 0:
            return 1
        return 1 + sum(self._number_of_nodes(child) for child in node.children)