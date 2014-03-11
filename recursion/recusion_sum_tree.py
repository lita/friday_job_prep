"""
Find the sum of a binary tree
"""
class Node(object):
    def __init__(self, value, l=None, r=None):
        self.value = value
        self.left = l
        self.right = r

tree1 = Node(1, 
             Node(2,
                  Node(3),
                  Node(4)),
             Node(5,
                  Node(6),
                  Node(7)))

tree2 = Node(1,
             Node(2, 
                  Node(3)),
             Node(4))

def sumTree(node):
    total = node.value
    if node.right:
        total += sumTree(node.right)
    if node.left:
        total += sumTree(node.left)

    return total

print sumTree(tree2)

"""
Tail recursive
"""
def traverseHelper(tree, rightlist, total):
    total += tree.value
    if tree.right:
        rightlist.append(tree.right)
    if tree.left:
        return(traverseHelper(tree.left, rightlist, total))
    elif (tree.left is None) and rightlist:
        return(traverseHelper(rightlist.pop(), rightlist, total))
    else: 
        return(total)

def traverse(tree):
    return traverseHelper(tree, [], 0)