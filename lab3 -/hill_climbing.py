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
        # indicates number of conflicts, 0 is no conflicts - best value
        self.value = 0

    # calculate no. of conflicts
    def calculateValue(self, board):
        print("Queen " + str(self.col) + " on row " + str(self.row))

    def best_move(self):
        # find the best move and the value function after making that move
        # return move, value
        return


class Board:
    def __init__(self, N):
        self.N = N
        # i don't really use the array, but just in case, maybe for the future
        self.array = []
        self.matrix = []
        self.queens = []

        self.createMatrix()
        # places all queens on row 0
        self.placeQueens(0)

    def makeMove(self, move):
        # actually execute a move (change the board)
        return 0

    def getArray(self):
        return self.array

    def getQueens(self):
        return self.queens
    
    def getQueen(self, col):
        return self.queens[col]

    def createArray(self):
        for i in range(0, self.N):
            self.array.append(0)
        return self.array

    def createMatrix(self):
        for col in range(0, self.N):
            matrixCol = []
            for row in range(0, self.N):
                # O signifies empty
                matrixCol.append("O")
            self.matrix.append(matrixCol)

    def placeQueens(self, row):
        for col in range(self.N):
            queen = Queen(col, row)
            self.queens.append(queen)
            self.matrix[0][col] = "Q"

    def printMatrix(self):
        for col in range(0, len(self.matrix)):
            for row in range(0, len(self.matrix[0])):
                print(self.matrix[col][row], end=" ")
            print(" ")


# create 4x4 board
board = Board(4)
board.printMatrix()

for i in range(len(board.queens)):
    board.queens[i].calculateValue(board)
    #board.getQueen(i).calculateValue
    #hill_climbing(q)