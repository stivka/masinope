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
        if (matrix[pRow + 1][pCol] is " "):
            neighbour = (pRow + 1, pCol)
            neighbours.append(neighbour)
    # left
    if (pCol - 1 >= 0):
        if (matrix[pRow][pCol - 1] is " "):
            neighbour = (pRow, pCol -1)
            neighbours.append(neighbour)
    # below
    if (pRow - 1 >= 0):
        if (matrix[pRow - 1][pCol] is " "):
            neighbour = (pRow - 1, pCol)
            neighbours.append(neighbour)
    # right
    if (pCol + 1 < cols):
        if (matrix[pRow][pCol + 1] is " "):
            neighbour = (pRow, pCol +1)
            neighbours.append(neighbour)

    return neighbours


def expandFrontier(matrix, startingPosition):
    frontier = Queue()
    frontier.put(startingPosition)
    came_from = {}
    came_from[startingPosition] = None

    while not frontier.empty():
        current = frontier.get()
    
        neighbours = getNeighbours(current, matrix)
        
        for x in neighbours:
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current


    


    return


    
startingPosition = (14, 16)
matrix = [] 
createMatrix(matrix, lava_map1)
rows = len(matrix)
cols = len(matrix[0])

printMatrix(matrix)
expandFrontier(matrix, startingPosition)
