from queue import Queue, PriorityQueue
import math

# map on 15 kõrge ja 31 lai

def createMatrix(matrix, map):
    for row in range(0, len(map)):
        matrixRow = []
        for col in range(0, len(map[0])):
            matrixRow.append(map[row][col])
        matrix.append(matrixRow)

    return


def printMatrix(matrix):
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            print(matrix[row][col], end=" ")
        print(" ")


def getNeighbours(pivot):
    pRow = pivot[0]
    pCol = pivot[1]

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
    
    frontier.put((0, startingPosition))
    came_from[startingPosition] = None

    # We take from the frontier PriorityQueue the node with the smallest distance toward the goal, that is they are sorted as smallest priority on top.
    
    while not frontier.empty():
        current = frontier.get()
        print(current)

        if matrix[current[0]][current[1]] == 'D':
            print("Diamond found!")
            traceBack(current, came_from)
            break

        neighbours = getNeighbours(current)

        for next in neighbours:
            if next not in came_from:
                priority = MDistance(next, goalPosition)
                frontier.put(priority, next)
                came_from[next] = current
    return

# node is coordinates of position
def MDistance(node, goal):
    verticalDistance = goal[0] - node[0]
    horizontalDistance = goal[1] - node[1]
    distance = math.sqrt(math.pow(verticalDistance, 2) + math.pow(horizontalDistance, 2))

    return distance

def traceBack(current, came_from):
    while current != startingPosition:
        path.append(current)
        current = came_from[current]
    path.append(startingPosition)  # optional
    path.reverse()  # optional

    print (path)
    return path

def printList(list):
    for x in list:
        print(x)
    return

def addTrail():
    for position in path:
        matrix[position[0]][position[1]] = "."
    matrix[path[0][0]][path[0][1]] = "S"
    matrix[path[-1][0]][path[-1][1]] = "D"

    return

with open("cave300x300") as f:
    map_data = [l.strip() for l in f.readlines() if len(l)>1]

startingPosition = (2, 2)
goalPosition = (295, 257)
#goalPosition300 = (295, 257)
#goalPosition600 = (598, 595)
#goalPosition900 = (898, 895)

matrix = []
createMatrix(matrix, map_data)
rows = len(matrix)
cols = len(matrix[0])

frontier = PriorityQueue()
came_from = {}

path = []

#printMatrix(matrix)
print("")
expandFrontier(matrix, startingPosition)
#addTrail()
#printMatrix(matrix)
