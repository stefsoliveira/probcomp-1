def readPatients(numberPatients):
    patients = []
    for n in range(numberPatients):
        patient = list(map(str,input().split(" ")))
        patients.append(patient)
    return patients

def hasHigherPriority(patientOne,patientTwo):
    plan = {
        "premium": 4,
        "ouro": 3,
        "prata": 2,
        "bronze": 1,
        "resto": 0
    }
    if plan[patientOne[1]]>plan[patientTwo[1]]:
        return True
    if plan[patientOne[1]]<plan[patientTwo[1]]:
        return False
    else: #gravidade
        if int(patientOne[2])>int(patientTwo[2]):
            return True
        if int(patientOne[2])<int(patientTwo[2]):
            return False
        else: #ordem alfabética
            if patientOne[0] < patientTwo[0]:
                return True
            if patientOne[0] > patientTwo[0]:
                return False
            else:
                return False

def sortPatientsbyPriority(patients): #insertionsort
    for i in range(1, len(patients)):
        key = patients[i]
        j = i - 1
        while j >= 0 and hasHigherPriority(key,patients[j]):
            patients[j + 1] = patients[j]
            j -= 1
        patients[j + 1] = key
    return patients

def printArray(arr):
    for i in range(len(arr)):
         print (arr[i][0])

numberPatients= int(input())
printArray(sortPatientsbyPriority(readPatients(numberPatients)))




#testcases
# print(comparePlans(['maria', 'resto', '270'], ['valentina', 'premium', '550'])==True)

# print("caso plano", hasHigherPriority(['amora', 'premium', '200'], ['maria', 'resto', '270']))
# print("caso gravidade", hasHigherPriority(['amora', 'resto', '300'], ['maria', 'resto', '270']))
# print("caso nome", hasHigherPriority(['amora', 'resto', '270'], ['maria', 'resto', '270']))

# print("caso à esquerda",listPatients(([['maria', 'premium', '270'], ['valentina', 'resto', '550']])))
# print("caso à direita",listPatients(([['maria', 'resto', '270'], ['valentina', 'premium', '550']])))
# print("caso igual plano",listPatients(([['maria', 'resto', '270'], ['valentina', 'resto', '550']])))
# print("caso igual plano, gravidade da esquerda menor",listPatients(([['maria', 'resto', '280'], ['valentina', 'resto', '550']])))
# print("caso igual plano, igual gravidade, ordem alfab.",listPatients(([['maria', 'resto', '280'], ['valentina', 'resto', '280']])))

# print(listPatients([['maria', 'resto', '270'], ['valentina', 'premium', '550']]))
# print(listPatients([['maria', 'premium', '270'], ['valentina', 'premium', '550']]))
# print(listPatients([['maria', 'premium', '270'], ['amora', 'resto', '270']]))

# print(sortPatientsbyPriority([
#     ['carla', 'prata', '151'],
#     ['maria', 'resto', '270'],
#     ['valentina', 'premium', '550'],
#     ['jonatan', 'resto', '40'],
#     ['enzo', 'prata', '700'],
#     ['enzo', 'ouro', '300'],
#     ['juvenal', 'resto', '234'],
#     ['kelly', 'prata', '151']
# ]))