import os
import random
eu = 0
computador = 0
jogadas = {1: "pedra", 2: "papel", 3: "tesoura"}

while True:
    os.system('clear')
    
    print('============================== \nBem vindo ao jogo Pedra, Papel e Tesoura! \n==============================\n')
    print(f'Placar \nVocê: {eu} \nComputador: {computador}')

    opcao = int(input('\n[1] - Pedra | [2] - Papel | [3] - Tesoura: '))
    while type(opcao) != int or opcao not in [1, 2, 3, 0]:
        opcao = int(input('Opção inválida, tente novamente: '))
    
    if opcao == 0:
        break

    opcao_pc = random.choice(list(jogadas.keys()))

    os.system('clear')

    if (opcao == 1 and opcao_pc == 3) or (opcao == 2 and opcao_pc == 1) or (opcao == 3 and opcao_pc == 2):
        eu += 1
        print('============================== \nVocê venceu! \n============================== \n')
        print(f'Placar \nVocê: {eu} \nComputador: {computador}')
        
    if (opcao == 1 and opcao_pc == 2) or (opcao == 2 and opcao_pc == 3) or (opcao == 3 and opcao_pc == 1):
        computador += 1
        print('============================== \nO computador venceu... \n============================== \n')
        print(f'Placar \nVocê: {eu} \nComputador: {computador}')

    if opcao == opcao_pc:
        print('Temos um empate! \n')
        print(f'Placar \nVocê: {eu} \nComputador: {computador}')

    entao = int(input('Deseja jogar novamente? [1] - Sim | [2] - Não: '))
    while type(entao) != int or entao not in [1, 2]:
        opcao = int(input('Opção inválida, tente novamente: '))
    
    if entao == 2:
        break