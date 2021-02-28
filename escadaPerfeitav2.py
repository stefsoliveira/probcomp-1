def sumSteps(initialStair):
    sumOfSteps = 0
    for n in range(len(initialStair)):
        sumOfSteps = sumOfSteps + initialStair[n]
    return sumOfSteps

def findFirstElement(initialPiles, initialStair):
    n = initialPiles
    sumInitialStair = sumSteps(initialStair)
    a1 = (2 * sumInitialStair - n**2 + n)/(2*n) #soma dos termos de uma PA considerando a1 e an.
    if (a1 % 2 == 0 or a1 % 2 == 1) and a1>0:
        return a1
    else:
        return -1

def createStair(start, end):
    stair = [0]*(end)
    stair[0] = start
    for i in range(1,end):
        stair[i] = stair[i-1] + 1
        i+1
    return stair

def countMovedSteps(initialStair,stair):
    totalMovedSteps = 0
    for i in range(0, len(initialStair)):
        if initialStair[i] > stair[i]:
            totalMovedSteps = totalMovedSteps + (initialStair[i] - stair[i])
    return totalMovedSteps

initialPiles = int(input())
initialStair = list(map(int, input().split(" ")))
a1 = findFirstElement(initialPiles, initialStair)
if a1 == -1:
    print(a1)
else:
    print(int(countMovedSteps(initialStair, createStair(a1, initialPiles))))

