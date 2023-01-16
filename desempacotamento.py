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