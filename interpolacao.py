print('\n')
"""
Interpolação básica de strings , colocar % na frente da string

s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789) são números formados de letras de A a F até 0 à 9

x - para ficar em minúsculo
X - para ficar em maiúsculo
"""

nome = 'Lucas'
preco = 10.50

# resultado esperado = 'Lucas, o preço total foi de R$ 10.50

variavel = '%s, o preço é RS%.2f' % (nome, preco)
print(variavel)

print('O hexadecimal de %d é %x' % (10, 10)) 

print('Caso eu queira que apareça mais algo além do hexadecimal, eu coloco o caracter e depois quantidade.')

print('O Hexadecimal de %d é %05x' % (15,15))

print('O hexadecimal entrará como uma unidade da quantidade que você escolher.')

#estou passando para ele que o valor que eu quero é 15 no %d, e passando para o hexadecimal que quero 15 no x

#___________________________________________________________________________________________________________

