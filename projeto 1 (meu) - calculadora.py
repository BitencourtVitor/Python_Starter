import os
import time

while True:
    timer_voltar = 10

    os.system('clear')
    print('Escolha a operação:')
    operacoes = ['Adição', 'Subtração', 'Multiplicação', 'Divisão']
    index = range(len(operacoes))
    opcoes = [x + 1 for x in index]
    for i in index:
        print(str(i+1) + '- ' + operacoes[i])

    escolha = int(input('Digite sua opção (0 para sair): '))

    if escolha == 0:
        break

    while escolha not in opcoes:
        escolha = input('Opção inválida, tente novamente: ')
    os.system('clear')

    def voltar():
        for i in range(timer_voltar, -1, -1):
            print(f"\rTempo restante: {i} segundos", end="")
            time.sleep(1)

    def adicao():
        loop = int(input('Quantos números você quer inserir? Entre 1 e 10: '))
        
        while loop < 1 or loop > 10:
            loop = int(input('A quantidade de números precisa estar 1 e 10: '))

        total = 0
        i = 1
        while i <= loop:
            valor = float(input(str(i) + 'º número: '))
            total = total + valor
            i += 1
        print('Resultado: {:.2f}'.format(total))
        voltar()

    def subtracao():
        loop = int(input('Quantos números você quer inserir? Entre 1 e 10: '))
        
        while loop < 1 or loop > 10:
            loop = int(input('A quantidade de números precisa estar 1 e 10: '))

        total = float(input('Número inicial: '))
        i = 1
        while i <= (loop-1):
            valor = float(input(str(i+1) + 'º número: '))
            total = total - valor
            i += 1
        print('Resultado: {:.2f}'.format(total))
        voltar()

    def multiplicacao():
        loop = int(input('Quantos números você quer inserir? Entre 1 e 10: '))
        
        while loop < 1 or loop > 10:
            loop = int(input('A quantidade de números precisa estar 1 e 10: '))

        total = float(input('1º número: '))
        i = 1
        while i <= (loop-1):
            valor = float(input(str(i) + 'º número: '))
            total = total * valor
            i += 1
        print('Resultado: {:.2f}'.format(total))
        voltar()

    def divisao():
        loop = int(input('Quantos números você quer inserir? Entre 1 e 10: '))
        
        while loop < 1 or loop > 10:
            loop = int(input('A quantidade de números precisa estar 1 e 10: '))

        total = float(input('Número inicial: '))
        i = 1
        while i <= (loop-1):
            valor = float(input(str(i+1) + 'º número: '))
            total = total / valor
            i += 1
        print('Resultado: {:.2f}'.format(total))
        voltar()

    match escolha:
        case 1:
            adicao()
        case 2:
            subtracao()
        case 3:
            multiplicacao()
        case 4:
            divisao()