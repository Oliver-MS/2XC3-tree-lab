import random as rand
from rbt import RBTree
from bst import BST
import matplotlib.pyplot as plt

#create a random sorted list of size elements and then the number of random swaps to perform
def random_list(size, swaps):
    L = []
    for _ in range(size):
        L.append(rand.randint(0,size))
    L.sort()
    for _ in range(swaps):
        i = rand.randint(0,size-1)
        j = rand.randint(0,size-1)
        L[i], L[j] = L[j], L[i]
    return L

list_size = 100
experiments = 500
randomness = 200
RB_height = []
BST_height = []
swaps = []

for i in range(randomness):
    total_RB_height = 0
    total_BST_height = 0
    for _ in range(experiments):
        curr = random_list(list_size, i)
        rb = RBTree()
        rb.insert_list(curr)
        total_RB_height += rb.get_height()
        
        bst = BST()
        bst.insert_list(curr)
        total_BST_height += bst.get_height()
    swaps.append(i)
    RB_height.append(total_RB_height)
    BST_height.append(total_BST_height)

diff = []
for i in range(randomness):
    diff.append((BST_height[i] - RB_height[i]) / experiments)

plt.plot(swaps, diff)
plt.xlabel("Number of random swaps")
plt.ylabel("Average difference in height")
plt.title("Average difference in height between RBT and BST")
plt.show()