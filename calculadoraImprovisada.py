def somaum(a):
    sucessor = a + 1
    return sucessor

def soma(a, b):
    soma = a
    for i in range(b):
        soma = somaum(soma)
    return soma

def multiplicacao(a, b):
    mult = 0
    for i in range(b):
       mult= soma(mult, a)
    return mult

def exponenciacao(a, b):
    exp= 1
    for i in range(b):
       exp= multiplicacao(exp, a)
    return exp

while True:
    comando = input()
    if comando:
        comando = comando.split()
        operacao = comando[0]
        if operacao == 'Suc':
            print(somaum(int(comando[1])))
        elif operacao == 'Soma':
            print(soma(int(comando[1]), int(comando[2])))
        elif operacao == 'Mult':
            print(multiplicacao(int(comando[1]), int(comando[2])))
        else: #exponenciaçao
            print(exponenciacao(int(comando[1]), int(comando[2])))
    else:
        break
