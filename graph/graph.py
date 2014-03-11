
tree = {'a':['b','c','d'],
        'd':['b','d','e'],
        'e':['a']}

def findNodes(start, end, graph, visited):
     if start == end:
          return True
     
     elif start not in graph:
          return False

     paths = graph[start]
     visited.append(start)

     for path in paths:
          if path not in visited and path in graph:
               result = findNodes(path, end, graph, visited)
               if result:
                    return True
          elif path == end:
               return True

     return False

print findNodes('c','b',tree,[])

"""
write a function that tells if a tree is a subtree of another tree
"""

class Node (object):
     def __init__(self, value):
          self.left = None
          self.right = None
          self.value = value

     def insert(self, value):
          if self.value < value:
               if self.left == None:
                    self.left = Node(value)
               else:
                    self.left.insert(value)
          else:
               if self.right == None:
                    self.right = Node(value)
               else:
                    self.right.insert(value)


     def find(self, value):
          if self.value == value:
               return self
          if self.value < value:
               if self.left:
                    return self.left.find(value)
               else:
                    return None
          else:
               if self.right:
                    return self.right.find(value)
               else:
                    return None

     def printInOrder(self):
          if self.left:
               self.left.printInOrder()
          print self.value
          if self.right:
               self.right.printInOrder()

root = Node(500)
root.insert(10)
root.insert(90)
root.insert(2600)
root.insert(3000)
root.insert(2000)
root.insert(9)
root.insert(34)
root.insert(50)

subroot = Node(10)
subroot.insert(90)
subroot.insert(9)
subroot.insert(34)
subroot.insert(50)


def findHelper(node1, node2):
     if node1.value == node2.value:
          if node1.right and node2.right:
               result = findHelper(node1.right, node2.right)
               if not result:
                    return False
          if node1.left and node2.left:
               return findHelper(node1.left, node2.left)
          return True
     else:
          return False
     
def findSubTree(tree, subtree):
     node = tree.find(subtree.value)
     if not node:
          return False

     return findHelper(node, subtree)


print findSubTree(root, subroot)



"""
Find a path from 1 to 10
"""
g = [[],
     [2, 4],
     [1, 3, 5],
     [2],
     [1, 7],
     [2, 6, 8],
     [5, 9, 10],
     [4],
     [5],
     [6, 12],
     [6, 11],
     [10],
     [9]]

def findPath(start, end, g, path, visited):
     if start == end:
          path.append(end)
          return True

     routes = g[start]
     
     if routes == []:
          return False

     path.append(start)
     visited.append(start)
     for route in routes:
          if route not in visited:
               result = findPath(route, end, g, path, visited)
               if result:
                    return True

     path.remove(start)
     return False

#path = []
#findPath(1, 12, g, path, [])
#print path

"""
Find the shortest path from 1 to 12
"""
g = [[1, 2],
     [1, 4],
     [2, 1],
     [2, 3],
     [2, 5],
     [3, 2],
     [3, 11],
     [4, 1],
     [4, 5],
     [4, 7],
     [5, 2],
     [5, 4],
     [5, 6],
     [5, 8],
     [6, 5],
     [6, 9],
     [6, 10],
     [7, 4],
     [7, 13],
     [8, 5],
     [8, 14],
     [9, 6],
     [9, 12],
     [10, 6],
     [10, 11],
     [11, 3],
     [11, 10],
     [12, 9],
     [13, 7],
     [13, 14],
     [14, 8],
     [14, 13]]

import Queue

def findPaths(node, g):
     children = []
     for edge in g:
          if edge[0] == node:
               children.append(edge[1])
     return children

def _findShortestPath(end, g, q, visited):
     if q.empty():
          return None

     start, path = q.get()
     visited.append(start)
     
     if start == end:
          return path

     children = findPaths(start, g)

     children = filter(lambda x: not x in visited, children)

     for child in children:
          q.put((child, path + [child]))

     return _findShortestPath(end, g, q, visited)

def findShortestPath(start, end, g):
     q = Queue.Queue()
     q.put((start, [start]))
     return _findShortestPath(end, g, q, [])


print findShortestPath(1, 14, g)
