"""
Formatação de String

"""

#Começando com fstring, posso colocar variáveis dentro de uma string ou no começo do print só de colocar o f''
# e as variáveis colocamos dentro de {}

nome_Lucas = 'Lucas'
variavel = f'Meu nome é {nome_Lucas}'
print(f'\n{variavel} , isso no começo desta frase é uma variável puxando uma string')

"""
Podendo até colocar quantas casas decimais quero que apareça depois do ponto.
"""
calculo_1 = 10 / 3
print(f'Calculo 10/3: {calculo_1:.2f}') # no caso vai ter somente duas casas depois da vírgula

#_____________________________________________________________________________________________________

#format 

a = 'A'
b = 'B'
c = 10.5545

# se eu colocar as chaves, irá puxar o valor pela ordem
formato = '{}, {}, {:.2f}'.format(a, b, c)

print(f'Primeiro format: {formato}')

# posso pegar por índices :

formato_2 = '{2}, {0}, {1}'.format(a, b, c)

print(f'Agora em outra ordem: {formato_2}')

# Dá para nomear um parâmetro, mas quando for chama-lo, tenho que chamar-lo pelo parâmetro nomeado
# exemplo:

string_2 = 'a = {0}, b = {1}, c= {nomeado:.2f}, outro nomeado = {nomeado2}'.format(a, b, nomeado=c, nomeado2 =a)

print(f'\nNovo format com parametro nomeado : {string_2}')

print(f'\nFinal\n')

#_____________________________________________________________________________________________________





