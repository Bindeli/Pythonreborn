"""
Variáveis são usadas para salvar algo na memoria do computador

é indicado que inicie variáveis com letras minúsculas, pode usar números e underline _

Utilizamos o sinal de igual = para atribuir um valor à variável.

Exemplo : numero = 8

primeiro_numero = 10 (snake_case)
"""

nome_completo = 'Lucas'

print(nome_completo)

#_________________________________________________________________________________________________
"""
Posso colocar qualquer tipo de dado na variavel, como int, float, bool, string.

numero_inteiro = 10
numero_float = 10.5
palavra = 'programar'
resultado = True
"""
print('')
soma_resultado = 10 + 7

print(soma_resultado)
#_________________________________________________________________________________________________
"""
Variáveis não são usadas para abreviar código, são utilizadas para tornar-lo mais legível.

Permitindo ao dev, não precisar repetir o mesmo valor várias e várias vezes

exemplo:
"""
# invés de ficar escrevendo print(int('10'), type(int('10))), vou jogar o valor em uma variável

valor_no_print = int(10)

print(valor_no_print, type(valor_no_print))

#_________________________________________________________________________________________________
nome = 'Lucas'
idade = 25
maior_de_idade = idade >= 18
print('Nome:',nome, 'Idade:', idade)
print('É maior de idade ? ', maior_de_idade)

#_________________________________________________________________________________________________

print('')
"""
Exercicio , montar as variáveis para as perguntas abaixo

nome, sobrenome, idade, ano de nascimento, é maior de idade? , altura em metros 
"""
nome = 'Lucas'
sobrenome = 'Bindeli'
idade = 25
ano_nascimento = 2022 - 25
maior_de_idade = idade >= 25
altura_metros = 1.70


print('Nome: ' , nome)
print('Sobrenome :' , sobrenome)
print('Idade :' , idade)
print('Ano de nascimento : ' , ano_nascimento)
print('É maior de idade?' , maior_de_idade)
print('Altura em metros :' , altura_metros)