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


def expandFrontier(matrix, startingPosition):
    frontier = Queue()


frontier.put(startingPosition)
came_from = {}
came_from[startingPosition] = None

while not frontier.empty():
   current = frontier.get()
   for next in getNeighbours(current):
      if next not in came_from:
         frontier.put(next)
         came_from[next] = current


    if (matrix[startingPosition[0] + 1][startingPosition[1]] is " "):
        print("is empty")


    return

def getNeighbours(pivot):
    
    
    return

def minu_otsing(kaart):
    startingPosition = (14, 16)
    matrix = [] 
    createMatrix(matrix, lava_map1)
    printMatrix(matrix)
    expandFrontier(matrix, startingPosition)
    
    return

minu_otsing(lava_map1)
