"""
Função INPUT

Função para coletar dados do usuário solicitando.

Dica : Deixa um espaço no final
"""

informacao = input('Digite algo aqui: ')

# não irá finalizar até o usuário realizar uma ação

print(f'Você digitou isso: {informacao}\n')

print(f'\nVocê digitou isso : {informacao=}')

print('')

#__________________________________________________________________________________________

# Soma

print('Soma:')
numero1 = input('Digite um número inteiro: ')
numero2 = input('Digite outro número inteiro: ')

if numero1.isdigit() and numero2.isdigit():
    print(f'A soma dos dois números será : {numero1 + numero2}')
else:
    print('Digite números inteiros!')

#__________________________________________________________________________________________
print('\nFinal\n')