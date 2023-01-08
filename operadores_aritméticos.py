"""
Operadores aritméticos (matemática)

Adição +
Subtração -
multiplicação *
divisao /               retorna um ponto flutuante
divisão_inteira //      retorna um inteiro se não tiver um valor de ponto flutuante, 10 // 2 = 5, não 5.0
                        e não retorna as casas decimais.
exponenciação **        potêncialização numero elevado ao outro
modulo %                retorna o resto da divisão, 

"""

soma = 5 + 5

print('Soma 5+5 :', soma)

subtracao = 10 - 5

print('Subtração 10-5 :', subtracao)

multiplicacao = 10 * 2

print('Multiplicacao 10*2 : ', multiplicacao)

divisao = 10 / 2

print('Divisao 10/2 : ', divisao)

divisao_inteira = 10 // 2 

print('Divisao inteira 10//2 : ', divisao_inteira)

exponenciacao = 5 ** 2

print('Exponenciação 5**2 :', exponenciacao)

modulo = 10 % 3

print('Modulo 10 % 3 : ', modulo)

print('')

#____________________________________________________________________________________________________________
"""
Concatenação - juntar os valores ( + )
"""

concatenacao = 'Lucas' + ' ' + 'Bindeli' # nas aspas vazias tem um espaço

print(f'Concatenação : {concatenacao}')
#____________________________________________________________________________________________________________
"""
Repetição - repetir os valores por uma quantidade de vezes ( * )
"""

t_dez_vezes = 'T' * 10
nome_3_vezes = 3 * '_Bindeli'
print(t_dez_vezes)
print(nome_3_vezes)
#____________________________________________________________________________________________________________

"""
Precedência entre os operadores aritméticos

Primeiro algumas coisas serão executadas antes das outras, uma ordem.

1° : (n + n)    , o primeiro são os parênteses.
2° : **         , segundo é a Exponenciação
3° : * multiplicação, / divisão, // divisão inteira e % módulos
4° : + soma e - subtração

as que tem a mesma precedência, 
exemplo multiplicação e divisão, elas serão executadas da esquerda para direita
"""
print('\nPrecedências dos operadores: ')
conta_1 = (1 + 1) ** (5 + 5)    # resultado 1024
conta_2 = 1 + 1 ** 5 + 5        # resultado 7
print(f'Conta 1 : {conta_1} / e Conta 2: {conta_2}')






print('\nFim')