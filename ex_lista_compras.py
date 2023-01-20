"""
Faça uma lista de compras com listas:

O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.

Não permita que o programa quebre com erros de indices inexistentes na lista.

Quando listar deve aparecer assim:

0 objeto
1 objeto
2 objeto

"""
import os
print('\n')

lista_compras = []

while True:
    
    opcao = input('\nSelecione uma das opções:\n[1]INSERIR\n[2]APAGAR\n[3]LISTAR\n[4]SAIR\nSELECIONE: ')

    if opcao == '1':
        os.system('cls')
        item_adicionar = input('\nDigite um item a ser adicionado: ')
        if not item_adicionar:
            print('Digite algo!')
            continue
        else:
            lista_compras.append(item_adicionar)
            # continue
    elif opcao == '2':
        os.system('cls')
        indice_apagar = input('\nDigite qual item você deseja apagar pelo indice: ')
        try:
            indice_apagar = int(indice_apagar)
            lista_compras.pop(indice_apagar)
        except IndexError:
            print('Digite um número que está na lista.')
        except ValueError:
            print('Digite um número inteiro')
    elif opcao == '3':
        print('\n')
        for indice,item in enumerate(lista_compras):
            print(indice,item)
    elif opcao == '4':
        break
    else:
        print('Selecione uma opção válida!')

# print(lista_compras)
print('\n')