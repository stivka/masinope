def printBoard(self):
        for col in range(0, len(self.array)):
            for row in range(0, len(self.array)):
                if (self.array[col] == col):
                    print ("Q    ", end="")
                else:
                    print ("O    ", end="")
            print("\n")
        return
    
    def printQueenPositions(self):
        for q in range(len(self.queens)):
            print("Queen " + str(q.col) + " on row " + str(q.row))
        return