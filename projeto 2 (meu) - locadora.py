import os
import time
import sys

timer_voltar = 3

veiculos = [
    {
        "id": "fusca",
        "modelo": "Volkswagen Fusca",
        "ano": 1969,
        "preco_diario": 150.00,
        "status": True
    },
    {
        "id": "civic",
        "modelo": "Honda Civic",
        "ano": 2020,
        "preco_diario": 200.00,
        "status": False
    },
    {
        "id": "palio",
        "modelo": "Fiat Palio",
        "ano": 2015,
        "preco_diario": 120.00,
        "status": True
    },
    {
        "id": "corolla",
        "modelo": "Toyota Corolla",
        "ano": 2021,
        "preco_diario": 220.00,
        "status": True
    },
    {
        "id": "fiesta",
        "modelo": "Ford Fiesta",
        "ano": 2017,
        "preco_diario": 100.00,
        "status": False
    },
    {
        "id": "compass",
        "modelo": "Jeep Compass",
        "ano": 2019,
        "preco_diario": 250.00,
        "status": True
    },
    {
        "id": "tucson",
        "modelo": "Hyundai Tucson",
        "ano": 2022,
        "preco_diario": 280.00,
        "status": True
    },
    {
        "id": "sandero",
        "modelo": "Renault Sandero",
        "ano": 2016,
        "preco_diario": 90.00,
        "status": False
    },
    {   
        "id": "renegade",
        "modelo": "Jeep Renegade",
        "ano": 2018,
        "preco_diario": 230.00,
        "status": True
    },
    {
        "id": "onix",
        "modelo": "Chevrolet Onix",
        "ano": 2020,
        "preco_diario": 110.00,
        "status": True
    }
]

def voltar():
    for i in range(timer_voltar, -1, -1):
        print(f"\rVoltando em {i} segundos", end="")
        time.sleep(1)

def listar(aluga, index):
    for v in veiculos:
        if v["status"] == aluga:
            print("[{}] - {} | {} | Diária: R${:.2f}".format(v['id'], v['modelo'], v['ano'], v['preco_diario']))
            index.append(v['id'])

def portfolio():
    os.system('clear')

    print('Este é o porfólio de carros no momento:')
    index = []
    listar(True, index)

    opcao = input('\n[menu] - Voltar ao Menu Inicial | [999] - Sair: ')
    while opcao != '':
        match opcao:
            case '999':
                sys.exit()
            case 'menu':
                break

def alugar():
    os.system('clear')

    print('Escolha um veículo para alugar:')
    index = []
    listar(True, index)

    opcao = input('\n[ID do carro] - Escolha para alugar | [menu] - Voltar ao Menu Inicial | [999] - Sair |  Digite aqui: ')
    while opcao != '' and opcao not in index:
        if opcao == '999':
            sys.exit()
        elif opcao == 'menu':
            return
        else:
            opcao = input('\nATENÇÃO: [menu] - Volta pro Menu | [999] - Encerra | [ID] Escolhe um carro | Digite aqui: ')
        
    dias = int(input('Por quantos dias? '))

    escolha = next((v for v in veiculos if v['id'] == opcao), None)
    preco_total = escolha['preco_diario'] * dias

    print(f"\nVocê escolheu: {escolha['modelo']} ({escolha['ano']}) - Valor total por {dias} dias: R${preco_total}")
    
    ctz = ''
    ctz = input('Você confirma essa movimentação? Y ou N: ').upper()
    while ctz not in ['Y', 'N']:
        ctz = input('Opção inválida, digite apenas Y (yes) ou N (no): ').upper()
    if ctz == 'Y':
        escolha['status'] = False
        print("\nVeículo alugado com sucesso!")
    
    input('Insira qualquer coisa para voltar ao Menu. ')

def devolver():
    os.system('clear')

    print('Escolha um veículo para devolver:')
    index = []
    listar(False, index)

    opcao = input('\n[ID do carro] - Escolha para devolver | [menu] - Voltar ao Menu Inicial | [999] - Sair |  Digite aqui: ')
    while opcao != '' and opcao not in index:
        if opcao == '999':
            sys.exit()
        elif opcao == 'menu':
            return
        else:
            opcao = input('\nATENÇÃO: [menu] - Volta pro Menu | [999] - Encerra | [ID] Escolhe um carro | Digite aqui: ')
        
    escolha = next((v for v in veiculos if v['id'] == opcao), None)

    print(f"\nVocê está devolvendo: {escolha['modelo']} ({escolha['ano']}) - alugado por R${escolha['preco_diario']:.2f} ao dia")
    
    ctz = ''
    ctz = input('Você confirma essa movimentação? Y ou N: ').upper()
    while ctz not in ['Y', 'N']:
        ctz = input('Opção inválida, digite apenas Y (yes) ou N (no): ').upper()
    if ctz == 'Y':
        escolha['status'] = True
        print("\nVeículo devolvido com sucesso!")
    
    input('Insira qualquer coisa para voltar ao Menu. ')

while True:
    os.system('clear')
    print('Bem vindo a locadora de carros!')
    print('Selecione uma das opções: \n1- Ver portfólio \n2- Alugar um veículo \n3- Devolver um veículo alugado \n0- Sair')
    opcao_inicial = int(input('Digite aqui: '))

    match opcao_inicial:
        case 1:
            portfolio()
        case 2:
            alugar()
        case 3:
            devolver()
        case 0:
            break