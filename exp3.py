from math import ceil
from matplotlib import pyplot as plt
from xc3tree import XC3Tree


def h(i):
    return ceil(i/2)+1

tree_degrees=25
lengths=[]
hlengths=[]
degs=[]
for i in range(0,tree_degrees):
    tree = XC3Tree(i)
    lengths.append(tree.get_height())
    hlengths.append(h(i))
    degs.append(i)
plt.plot(degs, lengths)
plt.plot(degs, hlengths)
plt.xlabel("Tree Degree")
plt.ylabel("Tree Height")
plt.title("h(i) and getHeight() comparison")
plt.show()