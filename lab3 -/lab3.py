array = []

for i in range(0, 4):
    array.append(0)

for col in range(0, len(array)):
    for row in range(0, len(array)):
        if (array[col] == col):
            print ("Q    ", end="")
        else:
            print ("O    ", end="")
    print("\n")
    