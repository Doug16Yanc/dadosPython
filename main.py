def main():

    print(f'Bem-vindo ao estudo inicial da ciência de dados')
    print(f'Aqui temos um exemplo de um algoritmo simples que apresenta dados estatísticos acerca de casos de doença.')

    total = 0
    contador = 0

    casos = int(input("Digite o número de casos no dia:"))

    maior = -1
    menor = 10000000000

    while casos > 0:
        total += casos
        contador += 1

        if casos > 0:
            casos = int(input("Digite o número de casos no dia:"))
            if casos > maior:
                maior = casos
            if casos < menor and casos > 0:
                menor = casos

    media = total//7

    print(f'A média semanal é igual a:', media)
    print(f'O maior número de casos em determinado dia foi ', maior)
    print(f'O menor número de casos em determinado dia foi ', menor)



main()