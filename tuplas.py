"""
Tipo Tupla - é uma lista imutável

Não pode alterar o valor, remover ou adicionar

"""

# Existe dois modos de criar tuplas

tupla = ('Lucas','Nil','André','Lemão')

tupla_1 = 'Lucas','Ninilsan','André','Lemão'

print(f'Tupla () : {tupla} ')
print(f'Tupla 1 : {tupla_1} ')

print(f'Vendo o valor no indice 1: {tupla[1]}')

#__________________________________________________________________________________________________________
# Posso converter em lista

tupla = list(tupla)

print(f'Estado atual da tupla: {tupla} seu tipo é {type(tupla)}')

tupla = tuple(tupla)

print(f'Estado atual da tupla: {tupla} seu tipo é {type(tupla)}')
