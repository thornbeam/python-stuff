import random, time, copy

width = 6
height = 6

nextCells = []
for x in range(width):
    column = []
    for y in range(height):
        if random.randint(0, 1) == 0:
            column.append("#")
        else:
            column.append(' ')
    nextCells.append(column)

while True:
    print("\n\n\n")
    currentCells = copy.deepcopy(nextCells)

    for y in range(height):
        for x in range(width):
            print(currentCells[x][y], end="|")
        print()

    for x in range(width):
        for y in range(height):
            leftCoord = (x - 1) % width
            rightCoord = (x + 1) % width
            aboveCoord = (y - 1) % height
            belowCoord = (y + 1) % height

            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == "#":
                numNeighbors += 1
            if currentCells[x][aboveCoord] == "#":
                numNeighbors += 1
            if currentCells[rightCoord][aboveCoord] == "#":
                numNeighbors += 1
            if currentCells[leftCoord][y] == "#":
                numNeighbors += 1
            if currentCells[rightCoord][y] == "#":
                numNeighbors += 1
            if currentCells[leftCoord][belowCoord] == "#":
                numNeighbors += 1
            if currentCells[x][belowCoord] == "#":
                numNeighbors += 1
            if currentCells[rightCoord][belowCoord] == "#":
                numNeighbors += 1

            if currentCells[x][y] == "#" and (numNeighbors == 2
                                              or numNeighbors == 3):
                nextCells[x][y] = "#"
            elif currentCells[x][y] == " " and numNeighbors == 3:
                nextCells[x][y] = "#"
            else:
                nextCells[x][y] = " "
    time.sleep(1)
