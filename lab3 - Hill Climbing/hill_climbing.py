def hill_climbing(N):
    current_board = Board(N)
    new_board = current_board
    best_board = current_board
    boards = []
    used_states = 0
    

    while (used_states <= N**N):
        used_states += 1
        boards = []
        
        # Adds all boards with one different move made by 
        for q in current_board.queens:
            for row in range(0, N):
                #print ("Moving queen " + str(q.row) + " of row " + str(q.col))
                # if isn't the current row that queen is on
                if (current_board.matrix[row][q.col] == "O"):
                    #print("Can move Queen " + str(q.col) + " to row " + str(row))
                    new_board = current_board
                    
                    new_board.makeMove(q, row)
                    new_board.calculateValue()
                    boards.append(new_board)
        # for 4 boards we get 4 * (4-1) boards everytime 
        #print (len(boards))

        for b in boards:
            if(b.value < best_board.value):
                print (b.value)
                print (best_board.value)
                best_board = boards[b]
                if(best_board.value == 0):
                  return best_board.printMatrix

        else:
            return best_board.printMatrix
        
class Queen:
    def __init__(self, row, col):
        self.col = col
        self.row = row
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

        for i in range(0, board.N):
            # checks whole column. If isn't itself and is a Queen
            if(i != self.row and matrix[i][self.col] == "Q" and not conflictOnCol):
                self.value += 1
                #conflictOnCol= True
                #print("Queen " + str(self.col) + " has conflict on column")

            # check row
            if(i != self.col and matrix[self.row][i] == "Q") and not conflictOnRow:
                self.value += 1
                #conflictOnRow = True
                #print("Queen " + str(self.col) + " has conflict on row")

        for i in range(1, board.N):
            # check diagonal down
            new_col = self.col + i
            new_row = self.row + i
            if (new_col < board.N and new_row < board.N):
                if(matrix[new_row][new_col] == "Q" and not conflictOnDiag):
                    self.value += 1
                    #conflictOnDiag = True
                    #print("Queen " + str(self.col) + " has conflict on diagonal")
            # check diagonal up
            new_col = self.col - i
            new_row = self.row - i
            if (new_col >= 0 and new_row >= 0):
                if(matrix[new_row][new_col] == "Q" and not conflictOnDiag):
                    self.value += 1
                    #conflictOnDiag = True
                    #print("Queen " + str(self.col) + " has conflict on diagonal")

            # check counter-diagonal up
            new_col = self.col + i
            new_row = self.row - i
            if (new_col < board.N and new_row >= 0):
                if(matrix[new_row][new_col] == "Q" and not conflictOnCDiag):
                    self.value += 1
                    #conflictOnCDiag = True
                    #print("Queen " + str(self.col) + " has conflict on counter-diagonal down")

            # check counter-diagonal down
            new_col = self.col - i
            new_row = self.row + i
            if (new_col >= 0 and new_row < board.N):
                if(matrix[new_row][new_col] == "Q" and not conflictOnCDiag):
                    self.value += 1
                    #conflictOnCDiag = True
                    #print("Queen " + str(self.col) + " has conflict on counter-diagonal down")
                    # print("Col " + str(self.col) + " Row " + str(self.row)
                    # + " New-col " + str(new_col) + " New-row " + str(new_row))

        #print("Queen " + str(self.col) + " has " +
              #str(self.value) + " conflict(s).")
        return self.value

class Board:
    def __init__(self, N):
        self.N = N
        # i don't really use the array, but just in case, maybe for the future
        #self.array = []
        self.matrix = []
        self.queens = []
        self.value = 0

        self.createMatrix()
        # places all queens on row 0
        self.placeAndCreateQueens(0)
        self.calculateValue()

    def makeMove(self, q, row):
        self.matrix[q.row][q.col] = "O"
        self.matrix[row][q.col] = "Q"

        q.row = row
        #print("Queen " + str(q.col) + " now on row " + str(q.row))
        return

    '''def createArray(self):
        for i in range(0, self.N):
            self.array.append(0)
        return self.array'''

    def calculateValue(self):
        self.value = 0
        for i in range(len(self.queens)):
            self.value += self.queens[i].calculateValue(self)
            #print("Value for board state is: " + str(self.value))
        return self.value

    def createMatrix(self):
        for row in range(0, self.N):
            matrixRow = []
            for col in range(0, self.N):
                # O signifies empty
                matrixRow.append("O")
            self.matrix.append(matrixRow)

    def placeAndCreateQueens(self, row):
        for col in range(self.N):
            queen = Queen(row, col)
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

# start hill_climbing solution finding for queens problem on 4x4 board
hill_climbing(4)