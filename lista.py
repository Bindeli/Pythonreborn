"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas

CRUD - Create - Read - Update - Delete
"""

string = 'ABDCE'

lista = list(string) # transforma cada elemento separando em uma lista
lista_1 = [] # uma lista vazia

# indices   0     1      2       3        4
lista_2 = [123, True, 'Lucas', 10.5, [1,2,3,4,5]]
# negativos -5    -4      -3     -2       -1

print(lista)
print(f'Elementos que podem aparecer na lista: {lista_2}')

# posso editar itens da lista

lista_2[2] = 'LucasBindeli'

print(f'Novo formato da lista: {lista_2}')

# Mutável pois podemos mudar seus valores
#______________________________________________________________________________________________________
# Método DEL - utilizado para apagar algo na lista com o índice, se eu não colocar indice, tudo será apago
# 
del lista_2[2]

print(f'Lista depois do DEL : {lista_2}')
#______________________________________________________________________________________________________
# Método append - adiciona um elemento que tá em parêntese como último elemento da lista
lista_2.append(50)
lista_2.append('teste')
print(f'Lista depois do append : {lista_2}')
#______________________________________________________________________________________________________
# Método pop - remove o último elemento da lista naquele momento
ultimo_valor_removido = lista_2.pop()
print(f'Lista depois do pop: {lista_2}, último elemento removido: {ultimo_valor_removido}')
lista_2.pop(1)
print(f'Removendo o elemento no indice 1: {lista_2}')
#______________________________________________________________________________________________________
# Método Clear - limpa toda a lista

# lista.clear()

#______________________________________________________________________________________________________
# Método Insert - adiciona um elemento no indice escolhido, primeiro o indice, depois o elemento

lista_2.insert(1, 100)
print(f'Lista depois do Insert (100,1) : {lista_2}')
#______________________________________________________________________________________________________
# Concatenando duas listas
# Posso utilizar o + ou extend

# Primeiro com o '+'
lista_3 = ['Elemento','Lista3']

lista_conc = lista_2 + lista_3

print(f'Lista concatenada com + : {lista_conc}')

# Extend mexe diretamente na lista a
lista_a = [1,2,3]
lista_b = [4,5,6]

# lista_c = lista_a.extend(lista_b) não posso jogar em uma variavel pois ele joga diretamente para lista a
lista_a.extend(lista_b)
# ou adicionar um elemento só lista_a.extend('a')
print(f'Junção de Lista com extend A e B : {lista_a}')


#______________________________________________________________________________________________________
"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)

método copy
"""
lista_x = ['Lucas', 'Bindeli']
lista_z = lista_x
# apontam para um mesmo valor na memória, se eu mudar um, o outro também vai mudar.

# Caso eu queira copiar e separar elas, utilizo o copy

lista_origem = ['Lucas','Nil','André','Lemao']
lista_copia = lista_origem.copy()

lista_origem[0] = 'Bindeli'

print(f'Lista origem mudada: {lista_origem}')
print(f'Lista copia: {lista_copia}')

#______________________________________________________________________________________________________
"""
For in - funciona listas
"""
lista_nomes = ['Lucas Bindeli', 'Ninilsan Ribeiro','André Junior','Lemao Angeli']

for nome in lista_nomes:
    print(nome, type(nome))

#______________________________________________________________________________________________________
"""
Exercício = Exiba os índices da lista

"""

print('\nExercicio : Exiba os indices da lista: ')

lista_ex = ['Lucas','Nil','André','Lemao']
i = 0
indices = range(len(lista_ex))

for indice in indices:
    print(f'{indice} : {lista_ex[indice]}')