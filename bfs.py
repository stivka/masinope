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
    
    

    return 0

def createMap(map):
    for row in range(0, len(map)):
        for col in range(0, len(map[0])):
            print (len(map[0]))
    return

minu_otsing(lava_map1)
createMap(lava_map1)
