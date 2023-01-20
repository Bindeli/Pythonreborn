"""
split e join com list e str

split - divide uma string (list)

com essa função posso dividir uma string e criar uma lista com ela
no caso eu coloquei o espaço para dividir a string
a cada espaço entre uma palavra e outra, será feito um novo valor para a lista


join - une uma string

se eu quiser formar uma string dessa lista, posso utilizar a função 'join'
todos os elementos da lista serão juntados e separados pelo elemento que está entre aspas simples
que no caso do exemplo é a vírgula, ou pode ser também um espaço
"""

frase = 'Olha só que louco, bem interessante'

lista_da_frase = frase.split(',') 
# quando ele encontrar um ponto, ele irá pegar o valor lido até ali e separar

print(lista_da_frase)

frase_grande = 'Ola uma estrela perto do sol, como é possível?'

lista_frase_2 = frase_grande.split() # sem nada, o padrão é cada espaço

print(lista_frase_2)

#___________________________________________________________________________________________
"""
Strip - corta os espaços do começo e do fim da minha string

Algo assim :
  olha só que  |
coisa  |

viraria isso aqui

olha só que|
coisa|

Temos o strip que vai cortar ambos os espaços
rstrip  que vai cortar o espaço da direita
lstrip que vai cortar o espaço da esquerda

"""

frase_espaço = '   Olha só que   , coisa interessante          '

frase_end = frase_espaço.split(',')

lista_end = []
for ind, frase in enumerate(frase_end):
    lista_end.append(frase_end[ind].strip())

print(f'\nFrase antes da mudança do strip: {frase_espaço}')
print(f'Frase depois da mudança strip em uma lista: {lista_end}')


# o ideal é ter uma lista criada para receber essa correção

#___________________________________________________________________________________________
"""
JOIN - unir 

começa com uma string que eu indico qual é o separador que vou usar, se eu deixar nada, não terá nada

strings, tuplas e listas
"""

string_unida = ''.join('abc')
string_unida2 = '-'.join('123456789')
string_frases = '-'.join(lista_end)

print(f'JOIN EXEMPLO 1 = {string_unida}')
print(f'JOIN EXEMPLO 2 = {string_unida2}')
print(f'Join da lista com frase : {string_frases}')








