from math import ceil
from matplotlib import pyplot as plt
from xc3tree import XC3Tree

def fib(i):
    if i == 0:
        return 1
    if i == 1:
        return 2
    return fib(i-1) + fib(i-2)

tree_degrees=25
nodes=[]
nodesfib=[]
degs=[]
for i in range(0,tree_degrees):
    tree = XC3Tree(i)
    nodes.append(tree.number_of_nodes())
    nodesfib.append(fib(i))
    print("i: " + str(i) + " nodes: " + str(tree.number_of_nodes()) + " " + str(tree.get_height()))
    degs.append(i)
plt.plot(degs, nodes)
plt.plot(degs, nodesfib)
plt.xlabel("Tree Degree")
plt.ylabel("Tree Nodes")
plt.title("Fibonacci and number_of_nodes() comparison")
plt.show()