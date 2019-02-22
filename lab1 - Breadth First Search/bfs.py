from queue import Queue

# map on 15 kõrge ja 31 lai

lava_map1 = [
    "      **               **      ",
    "     ***     D        ***      ",
    "     ***                       ",
    "                      *****    ",
    "           ****      ********  ",
    "           ***          *******",
    " **                      ******",
    "*****             ****     *** ",
    "*****              **          ",
    "***                            ",
    "              **         ******",
    "**            ***       *******",
    "***                      ***** ",
    "                               ",
    "                s              ",
]
start_row = 14
start_col = 16

lava_map2 = [
    "     **********************    ",
    "   *******   D    **********   ",
    "   *******                     ",
    " ****************    **********",
    "***********          ********  ",
    "            *******************",
    " ********    ******************",
    "********                   ****",
    "*****       ************       ",
    "***               *********    ",
    "*      ******      ************",
    "*****************       *******",
    "***      ****            ***** ",
    "                               ",
    "                s              ",
]


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
    
    frontier.put(startingPosition)
    
    came_from[startingPosition] = None

    while not frontier.empty():
        current = frontier.get()

        if matrix[current[0]][current[1]] == 'D':
            print("Diamond found!")
            traceBack(current, came_from)
            break

        neighbours = getNeighbours(current)

        for next in neighbours:
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    return


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

startingPosition = (14, 16)
matrix = []
createMatrix(matrix, lava_map2)
rows = len(matrix)
cols = len(matrix[0])

frontier = Queue()
came_from = {}

path = []

printMatrix(matrix)
print("")
expandFrontier(matrix, startingPosition)
addTrail()
printMatrix(matrix)
