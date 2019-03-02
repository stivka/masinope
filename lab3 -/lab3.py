


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

class Queen:
    def __init__(self, col, row):
        self.col = col
        self.row = 0
        #self.value

    '''def value(self):
        # calculate number of conflicts (queens that can capture each other)
        for col in range(0, len(array)):
            for r in range(0, len(array)):
                    
        return value'''
    
    def make_move(self, move):
        # actually execute a move (change the board)
        return 0

    def best_move(self):
        # find the best move and the value function after making that move
        # return move, value
        return

class Board:
    def __init__(self, N):
        self.N = N
        # puts all queens on row 0
        self.array = []
        # creates and Adds Queen objects, as to better acquire coordinates
        # also adds to row 0
        self.queens = []

    def addAll(self, row):
        for col in range(self.N):
            queen = Queen(col, row)
            self.queens.append(queen)

    def createArray(self, N, row):
        array = []
        for i in range(0, N):
            self.array.append(row)
        
    def printBoard(self, array):
        for col in range(0, len(array)):
            for row in range(0, len(array)):
                if (array[col] == col):
                    print ("Q    ", end="")
                else:
                    print ("O    ", end="")
            print("\n")
        return
    
board = Board(4)
board.createArray(4, 0)
board.addAll(0)

pos = Position(4) # test with the tiny 4x4 board first
print("Initial position value", pos.value())
best_pos, best_value = hill_climbing(pos)
print("Final value", best_value)
# if best_value is 0, we solved the problem

    