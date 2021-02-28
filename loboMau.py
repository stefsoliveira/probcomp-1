def readBoard(rows):
    board = []
    for n in range(rows):
        row = list(input())
        board.append(row)
    return board

def hasIndex(list, index):
    if index <= len(list) - 1 and index >= 0:
        return True
    else:
        return False

def isPasture(board, i, j):
    if board[i][j] == "." or board[i][j] == "v" or board[i][j] == "k":
        return True
    else:
        return False

def hasBeenVisited(pastures, i, j):
    for pasture in range(len(pastures)):
        for position in range(len(pastures[pasture])):
            if pastures[pasture][position] == [i, j]:
                return True
    return False

def hasPositionInArray(positions, i, j):
    for position in range(len(positions)):
        if positions[position] == [i, j]:
            return True

def findPasture(board, i, j, positions):
    if hasIndex(board, i) and hasIndex(board[i], j) and not hasPositionInArray(positions,i ,j):
        if board[i][j] == "f" or board[i][j] == "#":
            return
        else:
            positions.append([i, j])
            findPasture(board, i, j + 1, positions)
            findPasture(board, i + 1, j, positions)
            findPasture(board, i, j - 1, positions)
            findPasture(board, i - 1, j, positions)
            return
    else:
        return


def findEdges(board, i, j):
    if hasIndex(board, i) and hasIndex(board[i], j):
        if board[i][j] == "f" or board[i][j] == "#":
            return
        else:
            board[i][j] = 'f'
            findEdges(board, i, j + 1)
            findEdges(board, i + 1, j)
            findEdges(board, i, j - 1)
            findEdges(board, i - 1, j)
            return
    else:
        return


def explore(rows, columns, board):
    pastures = []
    for i in range(rows):
        for j in range(columns):
            if i == 0 or j==0 or i == rows-1 or j == columns-1:
                findEdges(board, i, j)
            if not hasBeenVisited(pastures, i, j):
                positions = []
                findPasture(board, i, j, positions)
                pastures.append(positions)
    return pastures

def findWolvesPositions(rows, columns, board):
    wolvesPositions = []
    for i in range(rows):
        for j in range(columns):
            if board[i][j] == "v":
                wolvesPositions.append([i,j])
    return wolvesPositions

def findSheepsPositions(rows, columns, board):
    sheetsPositions = []
    for i in range(rows):
        for j in range(columns):
            if board[i][j] == "k":
                sheetsPositions.append([i,j])
    return sheetsPositions

def findWolvesOnPastures(pastures, wolves):
    wolvesOnPastures = [0] * len(pastures)
    for pasture in range(len(pastures)):
        for coordinate in range(len(pastures[pasture])):
            for wolf in range(len(wolves)):
                if pastures[pasture][coordinate] == wolves[wolf]:
                    wolvesOnPastures[pasture] = wolvesOnPastures[pasture] + 1
    return wolvesOnPastures

def findSheepsOnPastures(pastures, sheeps):
    sheepsOnPastures = [0] * len(pastures)
    for pasture in range(len(pastures)):
        for coordinate in range(len(pastures[pasture])):
            for sheep in range(len(sheeps)):
                if pastures[pasture][coordinate] == sheeps[sheep]:
                    sheepsOnPastures[pasture] = sheepsOnPastures[pasture] + 1
    return sheepsOnPastures

def sumAnimals(animals):
    total = 0
    for n in range(len(animals)):
        total = total + animals[n]
    return total


def checkAnimalsAlive(wolvesOnPasture, sheepsOnPasture):
    for i in range(len(sheepsOnPasture)):
        if sheepsOnPasture[i]> wolvesOnPasture[i] and wolvesOnPasture[i]>0:
            wolvesOnPasture[i]=0
        if sheepsOnPasture[i] <= wolvesOnPasture[i] and sheepsOnPasture[i]>0:
            sheepsOnPasture[i]=0
    wolves =sumAnimals(wolvesOnPasture)
    sheeps=sumAnimals(sheepsOnPasture)
    return str(sheeps)+" "+str(wolves)


matrixSize = input().split(" ")
rows = int(matrixSize[0])
columns = int(matrixSize[1])
board = readBoard(rows)

print(checkAnimalsAlive(findWolvesOnPastures(explore(rows, columns, board), findWolvesPositions(rows, columns, board)), findSheepsOnPastures(explore(rows, columns, board), findSheepsPositions(rows, columns, board))))


# test cases
# print(findWolves([[[0, 0], [0, 1], [0, 2], [1, 0]], [[0, 4], [0, 5], [1, 5]], [[1, 3]], [[2, 1], [2, 2], [3, 2], [3, 1]], [[2, 4], [3, 4], [4, 4]], [[4, 0], [5, 0], [5, 1], [5, 2]]], [[1, 3], [2, 1]]))
# print(
#     checkAnimalsAlive(
#     findWolves([[[0, 0], [0, 1], [0, 2], [1, 0]], [[0, 4], [0, 5], [1, 5]], [[1, 3]], [[2, 1], [2, 2], [3, 2], [3, 1]], [[2, 4], [3, 4], [4, 4]], [[4, 0], [5, 0], [5, 1], [5, 2]]], [[1, 3], [2, 1]]),
#     findSheeps([[[0, 0], [0, 1], [0, 2], [1, 0]], [[0, 4], [0, 5], [1, 5]], [[1, 3]], [[2, 1], [2, 2], [3, 2], [3, 1]], [[2, 4], [3, 4], [4, 4]], [[4, 0], [5, 0], [5, 1], [5, 2]]], [[3, 2]]))
# #     )
# print(findSheetsPositions(rows, columns, board))
# print(findWolvesPositions(rows, columns, board))
# print((explore(rows, columns, board))==([
#     [[0, 0]],
#     [[0, 7]],
#     [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [5, 5], [6, 5], [6, 6], [6, 4],
#      [6, 3], [6, 2], [6, 1], [5, 1], [5, 2], [4, 1], [3, 1], [2, 1]],
#     [[3, 3], [3, 4], [4, 4], [4, 3]],
#     [[7, 0]],
#     [[7, 7]]
# ]))
# print(findSheepsOnPastures(explore(rows, columns, board), findSheepsPositions(rows, columns, board)))
# print(findWolvesOnPastures(explore(rows, columns, board),findWolvesPositions(rows, columns, board)))
