class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()
    
    def get_gramps(self):
        return self.parent.parent

    def uncle_is_black(self):
        if self.get_uncle() == None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
         return "(" + str(self.value) + "," + self.colour + ")"

    #rotates a parent to become a right child
    def rotate_right(self):
        if self.parent == None:
            pass
        elif self.is_left_child():
            self.parent.left = self.left
        elif self.is_right_child():
            self.parent.right = self.left
        temp = self.left.right
        self.left.parent = self.parent
        self.left.right = self
        self.parent = self.left
        self.left = temp

    #rotates a parent to become a left child
    def rotate_left(self):
        if self.parent == None:
            pass
        elif self.is_left_child():
            self.parent.left = self.right
        elif self.is_right_child():
            self.parent.right = self.right
        temp = self.right.left
        self.right.parent = self.parent
        self.right.left = self
        self.parent = self.right
        self.right = temp



class RBTree:

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

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def fix(self, node:RBNode):
        #You may alter code in this method if you wish, it's merely a guide.
        if node.parent == None:
            node.make_black()
        while node != None and node.parent != None and node.parent.is_red():  
            if node.get_uncle() == None or node.uncle_is_black(): #no uncle or black uncle (same process)
                #LL
                if node.is_left_child() and node.parent.is_left_child():
                    self.__LL(node)
                #RR
                elif node.is_right_child() and node.parent.is_right_child():
                    self.__RR(node)
                #LR
                elif node.is_left_child() and node.parent.is_right_child():
                    node.parent.rotate_right()
                    self.__RR(node.right)
                #RL
                elif node.is_right_child() and node.parent.is_left_child():
                    node.parent.rotate_left()
                    self.__LL(node.left)
            else: #red uncle
                node.parent.make_black()
                node.get_uncle().make_black()
                node.get_gramps().make_red()
                self.fix(node.get_gramps())
            if node.parent == None:
                self.root = node
            elif node.get_gramps() == None:
                self.root = node.parent
        self.root.make_black()
        
    def __LL(self, node:RBNode):
        node.get_gramps().make_red()
        node.get_gramps().rotate_right()
        node.parent.make_black()
        
    def __RR(self, node:RBNode):
        node.get_gramps().make_red()
        node.get_gramps().rotate_left()
        node.parent.make_black()
                    
        
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
