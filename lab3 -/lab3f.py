class Board(object):
    def __init__(self, N):
        self.N = N
        self.queens = []
        self.placeQueens()
    
    def placeQueens(self):
        for col in range(0, self.N):
            self.queens.append(Queen(col))
    
    def printQueens(self):
        for q in self.queens:
            q.show()

class Queen(object):
    def __init__(self, col):
        self.col = col
    
    
        

board = Board(4)
board.printQueens()
