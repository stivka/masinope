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
        #print("Queen " + str(self.col) + " on row " + str(self.row))
        matrix = board.matrix
        printMatrix(matrix)
        conflictOnCol = False
        conflictOnRow = False
        conflictOnDiag = False
        conflictOnCDiag = False

        for i in range (0, board.N):
            # checks whole column. If isn't itself and is a Queen
            if(i != self.row and matrix[self.col][i] == "Q" and not conflictOnCol):
                self.value += 1
                conflictOnCol= True
                print("Queen " + str(self.col) + " has conflict on column")

            # check row
            if(i != self.col and matrix[i][self.row] == "Q") and not conflictOnRow:
                self.value += 1
                conflictOnRow = True
                print("Queen " + str(self.col) + " has conflict on row")

        for i in range (1, board.N):
            # check diagonal down
            new_col = self.col + i
            new_row = self.row + i
            if (new_col < board.N and new_row < board.N):
                if(matrix[new_col][new_row] == "Q" and not conflictOnDiag):
                    self.value += 1
                    conflictOnDiag = True
                    print("Queen " + str(self.col) + " has conflict on diagonal")
            # check diagonal up
            new_col = self.col - i
            new_row = self.row - i
            if (new_col >= 0 and new_row >= 0):
                if(matrix[new_col][new_row] == "Q" and not conflictOnDiag):
                    self.value += 1
                    conflictOnDiag = True
                    print("Queen " + str(self.col) + " has conflict on diagonal")
            
            # check counter-diagonal down
            new_col = self.col + i
            new_row = self.row - i
            if (new_col < board.N and new_row >= 0):
                if(matrix[new_col][new_row] == "Q" and not conflictOnCDiag):
                    self.value += 1
                    conflictOnCDiag = True
                    print("Queen " + str(self.col) + " has conflict on counter-diagonal")

            # check counter-diagonal up
            new_col = self.col - i
            new_row = self.row + i
            if (new_col >= 0 and new_row < board.N):
                if(matrix[new_col][new_row] == "Q" and not conflictOnCDiag):
                    self.value += 1
                    conflictOnCDiag = True
                    print("Queen " + str(self.col) + " has conflict on counter-diagonal")


        print("Queen " + str(self.col) + " has " + str(self.value) + " conflict(s).")

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

def printMatrix(matrix):
        for col in range(0, len(matrix)):
            for row in range(0, len(matrix[0])):
                print(matrix[col][row], end=" ")
            print(" ")

# create 4x4 board
board = Board(4)
#board.printMatrix()

#for i in range(len(board.queens)):
    #board.queens[i].calculateValue(board)
board.queens[1].calculateValue(board)
    # board.getQueen(i).calculateValue
    # hill_climbing(q)
