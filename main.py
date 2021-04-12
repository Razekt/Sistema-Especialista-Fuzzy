import os
import BD

# Constantes
escala = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
var_linguistica = ['Muito Baixo', 'Baixo', 'Médio', 'Alto', 'Muito Alto']

# Variáveis globais
especialistas = {
                'E1':['1', '1-4', '3-6', '6-9', '8'], 
                'E2':['2', '2-5', '3-7', '7-10', '9'],
                'E3':['2', '2-4', '4-8', '7-9', '10'],
                'E4':['3', '2-5', '3-7', '7-10', '10']
                }
vNumeroUniformeFuzzy = {}

def numeroUniformeFuzzy():
    numeroUniforme = []
    for esp in especialistas:
        limite_inf = []
        limite_sup = []
        chave = especialistas[esp]
        
        i = 0
        while i < len(chave):
            valor = chave[i]
            if '-' in valor:
                limite_inf.append(int(valor.split('-')[0]))
                limite_sup.append(int(valor.split('-')[1]))
            else:
                limite_inf.append(int(valor))
                limite_sup.append(0)
            i += 1
        
        i = 0
        while i < len(var_linguistica):
            if limite_inf[i] > limite_sup[i]:
                numeroUniforme.append([limite_sup[i], limite_inf[i]])
            else:
                numeroUniforme.append([limite_inf[i], limite_sup[i]])
            i += 1
        
    fator_soma = int(len(numeroUniforme) / len(especialistas))

    i = 0
    j = 0
    qtd_elementos = fator_soma
    while True:
        vNumeroUniformeFuzzy[i] = numeroUniforme[j:fator_soma]
        i += 1
        j += qtd_elementos
        fator_soma += qtd_elementos
        
        if i >= len(especialistas):
            break

    # Verificar para obter uma única tupla [menor, maior] do conjunto de tuplas.
    i = 0
    j = []
    while i < qtd_elementos:
        for vetor in vNumeroUniformeFuzzy[i]:
            for v in vetor:
                j.append(v)
        #tupla += verificaNumMaxEMin(j)
        i += 1

def inserirDados():
    os.system('cls')
    limites = []
    nome = input('Insira o nome do especialista: ')

    for i in var_linguistica:
        limites.append(input('Digite o limite mínimo para a categoria ' + i + ': '))

    especialistas[nome] = limites
    os.system('cls')

def consultarDados():
    os.system('cls')
    print(especialistas.keys())
    nome = input('Digite o nome do especialista que deseja visualizar a classificação: ')
    print(especialistas[nome])
    os.system('pause')
    os.system('cls')

def main():
    opcao = ''
    while opcao != 'q':
        os.system('cls')
        print('''
        1 - Inserir dados de especialistas
        2 - Consultar dados de especialistas
        3 - Obter número uniforme Fuzzy
        4 - Consultar base de dados
        q - Sair
        ''')
        
        opcao = input('Digite uma opção: ')

        if opcao == '1':
            inserirDados()
        elif opcao == '2':
            consultarDados()
        elif opcao == '3':
            numeroUniformeFuzzy()
        elif opcao == '4':
            os.system('cls')
            BD.main()
        elif opcao == 'q':
            print('Encerrando sistema...')

main()