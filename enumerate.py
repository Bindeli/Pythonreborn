"""
enumerate - enumera iteráveis (índices)

Posso criar uma lista enumerada


"""
lista = ['Lucas','Ninilsan','André','Lemão']

lista_enumerada = enumerate(lista)

lista_mod = list(enumerate(lista))
#Ele vira uma tupla abaixo na hora de chamar (0, 'Lucas')

for valor in lista_enumerada:
    print(valor)

print('\n', lista_mod) # [(0, 'Lucas'), (1, 'Ninilsan'), (2, 'André'), (3, 'Lemão')]

# Caso eu queira que ele não comece do zero, e sim de um outro número, coloco a variavel vírgula e o valor

lista_av = list(enumerate(lista, 10))

print('\n',lista_av) #  [(10, 'Lucas'), (11, 'Ninilsan'), (12, 'André'), (13, 'Lemão')]

#
print('\nJeito primitivo:')
for indice,item in enumerate(lista):
    print(indice, item)

print('\nOu\n')

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

print('Utilizando o \t para ter um TAB')

for tupla_enumerada in enumerate(lista):
    print('FOR DA TUPLA:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')

print('\n')

