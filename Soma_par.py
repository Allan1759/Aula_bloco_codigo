def soma_pares():

    n1 = int(input('Digite um numero:> '))
    lista_01 = []
    for i in range(0, n1 + 1, 2):
        lista_01.append(i)
    soma = sum(lista_01)
    print(soma)

soma_pares()


