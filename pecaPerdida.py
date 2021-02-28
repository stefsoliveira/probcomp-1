n = int(input())
pecas = list(map(int, input().split(" ")))

def soma_elementos(lista):
    total = 0
    for i in lista:
       total = total + i
    return total

pecaPerdida = (int((n*(n+1))/2)) - soma_elementos(pecas)
print(pecaPerdida)



