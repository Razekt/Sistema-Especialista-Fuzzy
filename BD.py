import os
import pandas as pd
import mysql.connector as mysql

def importar(arquivo):
    xls = pd.read_excel(arquivo)
    df = pd.DataFrame(xls)
    matriz_riscos = df.values

    cont = 0
    for a in matriz_riscos:
        c = ''
        for b in a:
            c += '\'' + str(b) + '\','
        cont += 1
        inserir('riscos', c[:-1], cont)
    
    os.system('pause')

def conexao():
    # Mudar depois (aumentar segurança)
    host = 'localhost'
    usuario = 'root'
    pwd = '#Sl22012011'
    database = 'especialistafuzzy'
    
    conn = mysql.connect(host = host, user = usuario, password = pwd, database = database)
    return conn

def inserir(tabela, valores, PK = 0):
    y = consultar('SELECT COUNT(*) FROM ' + tabela)
    if int(y[0]) > 0:
        PK = int(y[0]) + 1
    
    conn = conexao()
    cursor = conn.cursor()
    SQL = 'INSERT INTO ' + tabela + ' VALUES (\'' + str(PK) + '\', ' + valores + ', null)'
    cursor.execute(SQL)
    cursor.close()
    conn.commit()
    print(cursor.rowcount, 'linha(s) inserida(s).')

def atualizar(tabela, valores, condicao):
    pass

def consultar(SQL):
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute(SQL)

    if 'COUNT' in SQL:
        y = cursor.fetchone()
    else:
        y = cursor.fetchall()

    cursor.close()
    return y

def main():
    opcao = ''
    while opcao != 'q':
        os.system('cls')
        print('''
        1 - Tabelas
        2 - Dados de uma tabela específica
        3 - Importar tabela de Riscos
        q - Retornar
        ''')

        opcao = input('Digite uma opção: ')

        if opcao == '1':
            os.system('cls')
            print(consultar('SHOW TABLES'))
            os.system('pause')
        elif opcao == '2':
            pass
        elif opcao == '3':
            os.system('cls')
            importar(input(''))
            os.system('cls')
        elif opcao == 'q':
            os.system('cls')