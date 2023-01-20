"""
Introdução ao desempacotamento + tuplas (tuplas)

Quero criar variáveis que recebam os valores da lista
"""

lista_de_nomes = ['Lucas','Nil','André','Lemão']

nome_1, nome_2, nome_3, nome_4 = lista_de_nomes

print(f'Nomes desempacotados: {nome_1},{nome_2},{nome_3},{nome_4}')
print(f'Lista completa: {lista_de_nomes}')
# Para pegar somente o primeiro e segundo, tendo 4 valores

primeiro_n, segundo_n, *resto_nomes = lista_de_nomes

print(f'Primeiro nome: {primeiro_n}, Segundo nome: {segundo_n}, resto dos nomes: {resto_nomes}')

"""
Quando eu não quero utilizar o resto da variável, eu utilizo um *_ parece , underline
"""

_ , nome2, *_ = ['Maria','Helena','resto','resto'] # para pegar o segundo.

# _, _, nome3 = [a lista] pegar semente o terceiro

lista_e = ['Maria', 'Joao', 1 , 2, 3, 4,]

pri, seg, *_, ant_pen, ult = lista_e


#____________________________________________________________________________________________________

# Chamada de funções

string_d = 'ABCD'

lista_d = ['Lucas','Nil','André','Lemão']

tupla_d = 'Python','é','uma','linguagem','de','programação'

print('\n\nMaria', 'Joao', 1 , 2, 3, 4,)

print(*lista_e)
print(*string_d)
print(*tupla_d, sep='-')


