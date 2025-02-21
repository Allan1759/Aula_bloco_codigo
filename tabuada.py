def tabuada():
    print('Seja bem vindo a tabuada virtual')
    n= int(input('Digite a tabuada que deseja saber:>> '))
    for j in range(0,11):
        c = n * j
        print(n,'X',j,'=',c)

tabuada()