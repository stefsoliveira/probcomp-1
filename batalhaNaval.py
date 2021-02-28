def readBoard(rows):
    board = []
    for n in range(rows):
        row = list(input())
        board.append(row)
    return board

def toIndex(value):
    return value - 1

def readShots():
    shotsAmount = int(input())
    shotsList = []
    for n in range(shotsAmount):
        shot = list(map(toIndex, map(int, input().split())))
        shotsList.append(shot)
    return shotsList

def hasIndex(list, index):
    if index <= len(list) - 1 and index >= 0:
        return True
    else:
        return False

def hasShip(board, i, j):
    if hasIndex(board, i) == True and hasIndex(board[i], j) == True and board[i][j] == "#":
        return True
    else:
        return False

def hasBeenVisited(ships, i, j):
    for ship in range(len(ships)):
        for position in range(len(ships[ship])):
            if ships[ship][position] == [i, j]:
                return True
    return False

def hasPositionInArray(positions, i, j):
    for position in range(len(positions)):
        if positions[position] == [i, j]:
            return True

def findShip(board, i, j, positions):
    if hasShip(board, i, j + 1) and not hasPositionInArray(positions, i, j + 1):
        positions.append([i, j + 1])
        findShip(board, i, j + 1, positions)
    if hasShip(board, i, j - 1) and not hasPositionInArray(positions, i, j - 1):
        positions.append([i, j - 1])
        findShip(board, i, j - 1, positions)
    if hasShip(board, i + 1, j) and not hasPositionInArray(positions, i + 1, j):
        positions.append([i + 1, j])
        findShip(board, i + 1, j, positions)
    if hasShip(board, i - 1, j) and not hasPositionInArray(positions, i - 1, j):
        positions.append([i - 1, j])
        findShip(board, i - 1, j, positions)
    return positions

def explore(rows, columns, board):
    ships = []
    for i in range(rows):
        for j in range(columns):
            if hasShip(board, i, j) and not hasBeenVisited(ships, i, j):
                positions = []
                positions.append([i, j])
                ships.append(findShip(board, i, j, positions))
    return ships

def checkShots(ships, shots):
    shipsLife = []
    for ship in range(len(ships)):
        shipsLife.append(len(ships[ship]))
        for coordinate in range(len(ships[ship])):
            for shot in range(len(shots)):
                if ships[ship][coordinate] == shots[shot]:
                    shipsLife[ship] = shipsLife[ship] - 1
    return shipsLife

def countDestroyedShips(shipslife):
    total = 0
    for n in range(len(shipslife)):
        if shipslife[n]==0:
            total = total +1
    return total

matrixSize = input().split(" ")
rows = int(matrixSize[0])
columns = int(matrixSize[1])
board = readBoard(rows)
shots = readShots()
print(countDestroyedShips(checkShots(explore(rows, columns, board), shots)))



# test cases
# print("direita",len(explore(2,2,[['#', '#'], ['.', '.']]))==1)
# print("esquerda",len(explore(3,3,[['.', '#', '#'],['.', '.','.'],['.', '.','.']]))==1)
# print("baixo",len(explore(2,3,[['.', '#', '.'],['.', '#','.']]))==1)
# print("cima",len(explore(2,3,[['.', '#', '.'],['.', '#','.']]))==1)
# print("cenariobarcoU",len(explore(3,3,[['#', '.', '#'],['#', '.','#'],['#', '#','#']])))
# print("cenariodoisbarquitos",explore(3,3,[['#', '.', '#'],['#', '.','#'],['#', '.','#']]))
# print('deve destruir um barquinho', checkShots([[[0, 0], [1, 0]]], [[0,0],[1,0]]))
# print('deve destruir dois barquinhos', checkShots([[[0, 0], [1, 0]],[[1, 1],[1, 2]]],[[0,0],[1,0],[1,1],[1,2]]))
# print('deve destruir dois barquinhos', checkShots(explore(3,3,[['#', '.', '#'],['#', '.','#'],['.', '.','.']]),[[0,0],[1,0],[0,2],[1,2]]))
# print('deve destruir zero barquinhos', checkShots(explore(3,3,[['#', '.', '#'],['#', '.','#'],['#', '.','#']]),[[0,0],[1,0],[0,2],[1,2]]))
# print(countDestroyedShips([0,0,0,0,0]))
#  return len(list(filter(isDeath, shipsLife)))
# def isDeath(life):
#     return life == 0