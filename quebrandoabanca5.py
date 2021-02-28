def maiorDigito(A, i, j):
    maiorIndice = k = i
    while k <= j:
        if A[k] > A[maiorIndice]:
            maiorIndice = k
        k+=1
    return maiorIndice

while True:
    try:
        parametros = [int(i) for i in input().split()]
        if parametros:
            num_digitos_entrada, num_digitos_removidos = parametros
            digitos_entrada = [int(i) for i in input().strip()]
            num_digitos_restantes = num_digitos_entrada - num_digitos_removidos
            posicao_do_maior = -1
            for i in range(num_digitos_restantes):
                posicao_do_maior = maiorDigito(digitos_entrada, posicao_do_maior+1, (num_digitos_entrada - 1) - (num_digitos_restantes - 1 - i))
                print(digitos_entrada[posicao_do_maior], end="")
            print()
        else:
            break
    except EOFError:
        break
