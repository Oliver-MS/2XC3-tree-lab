import random as rand
from rbt import RBTree
from bst import BST

#optionally allows to specify max and min values, but min defaults to 0 and max defaults to size
def random_list(size):
    L = []
    for _ in range(size):
        L.append(rand.randint(0,size))
    return L

list_size = 500
experiments = 500
total_RB_height = 0
total_BST_height = 0

for _ in range(experiments):
    curr = random_list(list_size)
    rb = RBTree()
    rb.insert_list(curr)
    total_RB_height += rb.get_height()
    
    bst = BST()
    bst.insert_list(curr)
    total_BST_height += bst.get_height()
    
print(f"The average height of an RBT containing {list_size} elements over {experiments} experiments is {total_RB_height / experiments}.") 
print(f"The average height of a BST containing {list_size} elements over {experiments} experiments is {total_BST_height / experiments}.") 
