from collections import deque

class Tree:
    def __init__(self, root, left=None, right=None):
        self.left = left
        self.right = right
        self.value = root
        
            
    def DFS(self, mode="preorder"):
        our_list = []
        
        if mode == "preorder":
            our_list.append(self.value)
        
        if self.left is not None:
            our_list = our_list + self.left.DFS(mode) 
        
        if mode == "inorder":
            our_list.append(self.value)
        
        if self.right is not None:
            our_list += self.right.DFS(mode)
        
        if mode == "postorder":
            our_list.append(self.value)
        
        return our_list


a = Tree('a')
b = Tree('b')
c = Tree('c')
d = Tree('d')
e = Tree('e')

b.right = d
b.left = e
a.left = b
a.right = c

#print(a.DFS("postorder"))
stackDFS(a)

"""
        
    mom = Tree('mom')
    
    mom.have_kids()
    
    def have_kids(self):
        new_kid = Tree('billy')
        self.children.append(new_kid)
"""