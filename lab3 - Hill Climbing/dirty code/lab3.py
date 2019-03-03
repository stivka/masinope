def hill_climbing(pos):
    curr_value = pos.value()
    while True:
        move, new_value = pos.best_move()
        if new_value >= curr_value:
            # no improvement, give up
            return pos, curr_value
        else:
            # position improves, keep searching
            curr_value = new_value
            pos.make_move(move)

def calculateConflicts(q):
    conflicts = 0
    
    # Check same row
    while(q < N):
        if(array[q] == Q):
            conflicts += 1
            break
        else:
            q += 1

    return

def printBoard():
        for col in range(0, len(array)):
            for row in range(0, len(array)):
                if (array[col] == col):
                    print("Q    ", end="")
                else:
                    print("O    ", end="")
            print("\n")
        return

def createArray():
        for i in range(0, N):
            array.append(0)
        return array


# create 4x4 board

# creates and Adds Queen objects, as to better acquire coordinates
# also adds to row 0!! array and object positions must match
# puts all queens on row 0

N = 4
array = []
createArray()
printBoard(array)
