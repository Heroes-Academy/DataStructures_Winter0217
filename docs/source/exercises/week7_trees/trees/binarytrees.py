class Tree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.n_children = 0

    def printme(self, depth=0, side="root"):
        indenter = "--"*depth

        print("{}{}::{}".format(indenter,side, self.value))
        if self.left is not None:
            self.left.printme(depth+1, "left")
        if self.right != None:
            self.right.printme(depth+1, "right")

    def contains(self, value):
        if self.value == value:
            return True
        if self.left is not None:
            if self.left.contains(value):
                return True
        if self.right is not None:
            if self.right.contains(value):
                return True
        return False


class BalancedTree(Tree):
    def add_child(self, child):
        self.n_children += 1
        if self.left is None and self.right is None:
            self.left = child
        elif self.left is None:
            self.left = child
        elif self.right is None:
            self.right = child
        else:
            if self.left.n_children > self.right.n_children:
                self.right.add_child(child)
            else:
                self.left.add_child(child)

class BinarySearchTree(Tree):
    def add_child(self, child):
        if child.value > self.value:
            self.add_right(child)
        else:
            self.add_left(child)

    def add_left(self, child):
        if self.left is None:
            self.left = child
        else:
            self.left.add_child(child)

    def add_right(self, child):
        if self.right is None:
            self.right = child
        else:
            self.right.add_child(child)

    def contains(self, value):
        if self.value == value:
            pass