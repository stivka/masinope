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
start_row=14
start_col=16

def minu_otsing(kaart):
    # start(y, x) ehk start(row, col)
    start = (14, 16)
    
    return

def createMatrix(map):
    
    

    

    matrix = []

    for row in range(0, len(map)):
        matrixRow = []
        for col in range(0, len(map[0])):
            matrixRow.append(map[row][col])
        matrix.append(matrixRow)
    
    print (len(map))
    print (len(map[0]))
    print (len(matrix))
    print (len(matrix[0]))
    
    return



createMatrix(lava_map1)
minu_otsing(lava_map1)
