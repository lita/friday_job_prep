"""
Find the number of ways to go up n-steps if you can only jump 3, 2 or 1 steps.
"""
def numStepsHelper(n, ways):
	if n == 0:
		return ways+1
	elif n < 0:
		return ways
	return numStepsHelper(n-3, ways) + numStepsHelper(n-2, ways) + numStepsHelper(n-1, ways)

def numSteps(n):
	return numStepsHelper(n, 0)

assert(numSteps(15)==5768)

"""
Calculate Fibonacci
"""
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	return fib(n-1) + fib(n-2)

assert(fib(15)==610)

"""
Calculate Fibonacci by tail recursion
"""
def fibTail(n):
	def fibTailHelper(term, cur, prev):
		if term==0:
			return prev
		if term==1:
			return  cur
		return fibTailHelper(term-1, cur+prev, cur)
	return fibTailHelper(n, 1, 0)
	
assert(fib(15)==610)

"""
Calculate the sum of a list.
"""
def sum(list):
	if len(list) == 0:
		return 0
	else:
		return list[0] + sum(list[1:])

assert(sum(range(1,6)) == 15)

"""
Calculate the sum of a list by tail recusion.
"""
def sumTail(list):
	def sumHelper(cur, list):
		if len(list) == 0:
			return cur
		else:
			return sumHelper(cur+list[0], list[1:])
	return sumHelper(0, list)

assert(sumTail(range(1,6))==15)

"""
Find the index where the number occured last. 
"""
def lastIndexOfTail(n, list):
	def lastIndexHelper(n, index, count, list):
		if not list:
			return index
		if n == list[0]:
			index = count
		return lastIndexHelper(n, index, count+1, list[1:])
	return lastIndexHelper(n, -1, 0, list)

assert(lastIndexOfTail(5, [1, 2, 4, 6, 5, 2, 7]) == 4)
assert(lastIndexOfTail(5, [1, 2, 4, 6, 2, 7]) == -1)
assert(lastIndexOfTail(5, [1, 2, 5, 4, 6, 5, 2, 7]) == 5)

# Explain Linked List to Peter
"""
Find the last node that n was seen
"""
def lastIndexOfLinkedList(n, linkedList):
	def lastIndexHelper(n, index, count, linkedList):
		if linkedList == None:
			return index
		if linkedList[0] == n:
			index = count
		return lastIndexHelper(n, index, count+1, linkedList[1])
	return lastIndexHelper(n, -1, 0, linkedList)

assert (lastIndexOfLinkedList(5, [1, [2, [4, [6, [5, [2, [7, None]]]]]]]) == 4)
assert (lastIndexOfLinkedList(5, [1, [2, [4, [6, [2, [7, None]]]]]]) == -1)

"""
Binary Tree
"""
class Node(object):
    def __init__(self, value, l=None, r=None):
        self.value = value
        self.left = l
        self.right = r

def sumOfBinaryTree(tree):
	if not tree:
		return 0
	return sumOfBinaryTree(tree.left) + sumOfBinaryTree(tree.right) + tree.value


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

assert (sumOfBinaryTree(tree2) == 10)
assert (sumOfBinaryTree(tree1) == 28)

def sumOfBinaryTreeTail(tree):    
    def flattenTree(tree, nodes, list):
        if tree == None:
            return
        list.append(tree.value)

        if tree.right:
            nodes.append(tree.right)
        if tree.left:
            return flattenTree(tree.left, nodes, list)
        elif tree.left == None and nodes:
            return flattenTree(nodes.pop(), nodes, list)

    def sumTail(counter, newList):
        if not newList:
            return counter
        else:
            return sumTail(counter+newList[0], newList[1:])

    newList = []
    flattenTree(tree, [], newList)
    return sumTail(0, newList)


assert (sumOfBinaryTreeTail(tree2) == 10)
assert (sumOfBinaryTreeTail(tree1) == 28)

"""
Tail recursion of summing a tree
"""
# Alex Whitney's Solution
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

assert (traverse(tree2) == 10)
assert (traverse(tree1) == 28)