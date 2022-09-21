def wiggleWalk(number):
    #input
    (numberOfInstructions, rows, columns, currentRow, currentCol) = tuple(map(int, (input().split())))
    instructions = input()

    #algortihm
    visitedSquares = [(currentRow, currentCol)]
    i = 0
    while i < numberOfInstructions:
        #movement
        move = instructions[i]
        if move == "N":
            currentRow -= 1
        elif move == "E":
            currentCol += 1
        elif move == "S":
            currentRow += 1
        else:
            currentCol -= 1
        #checking if robot has been in current square before
        if (currentRow, currentCol) not in visitedSquares:
            visitedSquares.append((currentRow, currentCol))
            i += 1

    #output
    print(f"Case #{number}: {currentRow} {currentCol}")


cases = int(input())
i = 1
while i <= cases:
    wiggleWalk(i)
    i += 1
