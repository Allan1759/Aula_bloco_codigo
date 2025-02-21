import random

def aleatorio():
    
    Sort_1 = int(input('Insira o numero inicial do sorteio:> '))
    sort_2 = int(input('Insira o numero final do sorteio:> '))
    
    for sorteio in range(3):
        sorteio = random.randint(Sort_1,sort_2)
        print(sorteio)

aleatorio()