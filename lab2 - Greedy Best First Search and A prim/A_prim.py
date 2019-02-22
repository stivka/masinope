from queue import Queue, PriorityQueue
import math
import time

# map on 15 kõrge ja 31 lai

def createMatrix(matrix, map):
    for row in range(0, len(map)):
        matrixRow = []
        for col in range(0, len(map[0])):
            matrixRow.append(map[row][col])
        matrix.append(matrixRow)

    return

def getNeighbours(current):
    pRow = current[0]
    pCol = current[1]

    neighbours = []

    # above
    if (pRow + 1 < rows):
        if (matrix[pRow + 1][pCol] is " " or matrix[pRow + 1][pCol] is "D"):
            neighbour = (pRow + 1, pCol)
            neighbours.append(neighbour)
    # left
    if (pCol - 1 >= 0):
        if (matrix[pRow][pCol - 1] is " " or matrix[pRow][pCol - 1] is "D"):
            neighbour = (pRow, pCol - 1)
            neighbours.append(neighbour)
    # below
    if (pRow - 1 >= 0):
        if (matrix[pRow - 1][pCol] is " " or matrix[pRow - 1][pCol] is "D"):
            neighbour = (pRow - 1, pCol)
            neighbours.append(neighbour)
    # right
    if (pCol + 1 < cols):
        if (matrix[pRow][pCol + 1] is " " or matrix[pRow][pCol + 1] is "D"):
            neighbour = (pRow, pCol + 1)
            neighbours.append(neighbour)

    return neighbours


def expandFrontier(matrix, startingPosition):
    exploredPositions = 0

    # Take in the node.
    frontier.put(startingPosition, 0)
    # In the dictionary i set the the came_from for the startingPosition to None
    came_from[startingPosition] = None
    cost_so_far[startingPosition] = 0

    # We take from the frontier PriorityQueue the node with the smallest distance toward the goal, that is they are sorted as smallest priority on top.
    
    while not frontier.empty():

        current = frontier.get()
        exploredPositions += 1
        new_cost = 0

        if matrix[current[0]][current[1]] == 'D':
            print("Diamond found!")
            print(str(exploredPositions) + " positions visited.")
            traceBack(current, came_from)
            break 

        neighbours = getNeighbours(current)

        for next in neighbours:
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = MDistance(next, goalPosition) + new_cost
                frontier.put(next, priority)
                came_from[next] = current
                   
    return

# node is coordinates of position
def MDistance(node, goal):
    verticalDistance = goal[0] - node[0]
    horizontalDistance = goal[1] - node[1]
    distance = verticalDistance + horizontalDistance

    return distance

def traceBack(current, came_from):
    while current != startingPosition:
        path.append(current)
        current = came_from[current]
    path.append(startingPosition)
    path.reverse()

    print("Path length is " + str(len(path) - 1) + str(" movements."))
    return path

def addTrail():
    for position in path:
        matrix[position[0]][position[1]] = "o"
    matrix[path[0][0]][path[0][1]] = "S"
    matrix[path[-1][0]][path[-1][1]] = "D"

    return

def writeToFile(matrix):
    f = open('solved_map.txt', 'w')

    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            f.write(matrix[row][col])
        f.write("\n")
    f.close()
    return

# Set the map file
with open("lab2 - Greedy Best First Search and A prim\cave600x600") as f:
    map_data = [l.strip() for l in f.readlines() if len(l)>1]

startingPosition = (2, 2)

#Set the goalPosition for the selected map. The values below mark where the goal is located on the specific map

goalPosition = (598, 595)
#goalPosition300 = (295, 257)
#goalPosition600 = (598, 595)
#goalPosition900 = (898, 895)

matrix = []
createMatrix(matrix, map_data)
rows = len(matrix)
cols = len(matrix[0])

frontier = PriorityQueue()
came_from = {}
cost_so_far = {}

path = []

# The program starts of from the function expandFrontier, also a timer is set from here.
start_time = time.time()
expandFrontier(matrix, startingPosition)
elapsed_time = time.time() - start_time
print("Time taken to find diamond was " + str(round(elapsed_time, 2)) + str(" seconds."))

# Also adds a trail of the movenent from start to goal. Writes it to file since the maps are too large to display in console.
#addTrail()
#writeToFile(matrix)
