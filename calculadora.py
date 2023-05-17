from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao!= 5:
    print('''O que deseja fazer com esses valores? 
[1]Somar
[2]Multiplicar
[3]Qual o maior valor
[4]Digitar novos números
[5]Sair do programa 
                 -> ''')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma do valor {n1} com o valor {n2} é {soma}!')
        sleep(1)
    if opcao == 2:
        soma1 = n1 * n2
        print(f'A multiplicação de {n1} por {n2} é {soma1}!')
        sleep(1)
    if opcao == 3:
        if n1 > n2:
            print(f'O valor {n1} é maior que o valor {n2}')
            sleep(1)
        if n2>n1:
            print(f'O valor {n2} é maior que o valor {n1}')
            sleep(1)
        if n1 == n2:
            print('Os 2 valores são iguais!')
            sleep(1)
    if opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        sleep(1)
    elif opcao >5:
            print('Opção inválida, tente novamente!')
            sleep(1)
            print('-' * 40)
    else:
        sleep(1)
print('Fim do programa! Volte sempre!!')
