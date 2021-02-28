def readModalitiesResults(numModalities):
    modalitiesResults = []
    for n in range(numModalities):
        modality = list(map(int,input().split(" ")))
        modalitiesResults.append(modality)
    return modalitiesResults

def emptyArray(numCountries):
    medalsByCountry=[]
    for i in range(numCountries):
        medalsByCountry.append([0,0,0,i+1])
    return medalsByCountry

def arrangeMedals(modalitiesResults, medalsByCountry):
    for i in range(len(modalitiesResults)):
        for j in range(len(modalitiesResults[i])):
            medalsByCountry[modalitiesResults[i][j]-1][j]+=1
    return medalsByCountry

def hasHigherScore(countryOne, countryTwo):
    if countryOne[0]>countryTwo[0]:
        return True
    if countryOne[0]<countryTwo[0]:
        return False
    else: #prata
        if countryOne[1]>countryTwo[1]:
            return True
        if countryOne[1]<countryTwo[1]:
            return False
        else: #bronze
            if countryOne[2]>countryTwo[2]:
                return True
            if countryOne[2]<countryTwo[2]:
                return False
            else: #indice
                if countryOne[3] < countryTwo[3]:
                    return True
                if countryOne[3] > countryTwo[3]:
                    return False
                else:
                    return False

def sortCountriesbyScore(countries): #insertionsort
    for i in range(1, len(countries)):
        key = countries[i]
        j = i - 1
        while j >= 0 and hasHigherScore(key,countries[j]):
            countries[j + 1] = countries[j]
            j -= 1
        countries[j + 1] = key
    return countries

def printWinningList(countries):
    for i in range(len(countries)):
        print(countries[i][3], end=' ')

numbers = input().split(" ")
numCountries = int(numbers[0])
numModalities = int(numbers[1])
printWinningList(sortCountriesbyScore(arrangeMedals(readModalitiesResults(numModalities), emptyArray(numCountries))))

# # print(*range(1,len(sortCountriesbyScore(arrangeMedals(readModalitiesResults(numModalities), emptyArray(numCountries))))+1))

# printWinningList([[1,1,1,1], [2,2,2,2]])R