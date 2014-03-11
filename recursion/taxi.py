""" 
How many ways are there for a taxi driver to get from the top left of a grid
city to the bottom right? The city is exactly 10 blocks in each direction, all
streets are two ways, and you know the city well enough that you'd balk if the
driver actually went drove away from the goal - so never up or left, only right
and down.

Note: For our convenience, We've defined it so that 0,0 is on the
bottom left and we are trying to go to the upper right.
"""

def taxi (start, goal, paths):
    if start == goal:
        return paths+1

    elif start[0] > 10 or start[1] > 10:
        return paths

    up = (start[0], start[1]+1)
    right = (start[0]+1, start[1])

    return taxi(right, goal, paths) + taxi(up, goal, paths)

print taxi((0,0), (10,10), 0)
