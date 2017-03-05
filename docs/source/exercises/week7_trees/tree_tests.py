import random
from trees import BalancedTree, Tree

def add_random(current_tree, depth=0):
    if depth <= 0:
        return
    new_left = Tree(random.randint(0,100))
    current_tree.left = new_left
    add_random(new_left, depth-1)

    new_right = Tree(random.randint(0,100))
    current_tree.right = new_right
    add_random(new_right, depth-1)

def add_random_balanced(root, number_subtrees):
    for i in range(number_subtrees):
        new_tree = BalancedTree(random.randint(0,100))
        root.add_child(new_tree)

root = BalancedTree(88)
add_random_balanced(root, 20)
root.printme()
root.contains(11)