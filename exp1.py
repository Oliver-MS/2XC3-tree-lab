import random as rand
from rbt import RBTree
from bst import BST

#optionally allows to specify max and min values, but min defaults to 0 and max defaults to size
def random_list(size):
    L = []
    for _ in range(size):
        L.append(rand.randint(0,size))
    return L

list_size = 10000
experiments = 500

total_RB_height = 0
max_RB_height = 0
total_BST_height = 0
max_BST_height = 0

for i in range(experiments):
    curr = random_list(list_size)
    rb = RBTree()
    rb.insert_list(curr)
    rb_height = rb.get_height()
    total_RB_height += rb_height
    if rb_height > max_RB_height:
        max_RB_height = rb_height
    
    bst = BST()
    bst.insert_list(curr)
    bst_height = bst.get_height()
    total_BST_height += bst_height
    if bst_height > max_BST_height:
        max_BST_height = bst_height
    
print(f"The average height of an RBT containing {list_size} elements over {experiments} experiments is {total_RB_height / experiments}.")
print(f"The maximum height of an RBT containing {list_size} elements over {experiments} experiments is {max_RB_height}.")  
print(f"The average height of a BST containing {list_size} elements over {experiments} experiments is {total_BST_height / experiments}.") 
print(f"The maximum height of a BST containing {list_size} elements over {experiments} experiments is {max_BST_height}.") 
