"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero = input('Vou dobrar o número que você digitar: ')

# numero = float(numero)
# print(f'O dobro de {numero} é {numero * 2:.2f}')

try: 
    # Se ocorrer algum erro no try, irá pular para o except
    print('Estou no Try:')
    print('STR: ', numero)
    numero = int(numero)
    print('INT : ', numero)
    # print('FLOAT: ', float(numero))
    print(f'O dobro de {numero} será {numero*2}')
except:
    print('Isso não é um número')

