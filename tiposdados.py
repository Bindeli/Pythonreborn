"""
Python é uma linguagem de programação

str é as string's , ou conhecidos como textos

Strings = textos que estão dentro de aspas simples ou duplas 

"""

print('String1 com aspas simples')
print("String2 com aspas duplas")

variavel_string = 'variavel'

print(variavel_string)
#__________________________________________________________________________________________________________


# Caracteres de Escape - para pular um caracter
# exemplo : 

print("\nLucas \'Bindeli") # ele vai ignorar as aspas simples como um código e vai deixar como parte da string
# saída : Lucas 'Bindeli

# Utilizando o r no começo antes das aspas, ele vai mostrar também a barra
# Utilizado para Expressões regulares

print(r"Lucas \'Bindeli")

#__________________________________________________________________________________________________________

"""
Inteiros é qualquer número positivo ou negativo que não tenha ponto

Ex : 11 , 12, -1, -3, 0 
"""

print('\nInteiros: ')
print(11)   #int
print(-11)  #int
print(0)    #int

#__________________________________________________________________________________________________________
"""
Float números que possuem casa decimal ou ponto flutuante
São separados por ponto!! .

Vírgula é utilizado para outras coisas em python

Ex : 10.2, 11,2, -11,2, 0.0
"""
print('\nFloat: ')
print(11.5)
print(-12)
print(0.0)
#__________________________________________________________________________________________________________

"""
Função type para verificar o tipo do valor

type(dado)

vamos chamar de função por agora, mas na verdade é uma class.
"""
print('\n', 11, type(11))
print(10.5, type(10.5))
print(0, type(0))
print(0.0, type(0.0))

print('Utilizando type com a string "texto": ', type('texto\n'))
#__________________________________________________________________________________________________________
"""
Tipo de dado boolean

Utilizado ao questionar algo em um programa, só existem duas opções

True (sim) ou False (não)

Utilizados bastante com operadores lógicos
"""
print('')
print('Verificando se 10 == 10 : ', 10==10)
print('Verificando se 101 == 10 : ', 101==10)
#__________________________________________________________________________________________________________

"""
Conversão de tipos de dados, ou Coerção

Como STR, INT, FLOAT OU BOOL

Se eu for juntar dois valores distintos irá dar erro

Por exemplo 1 + '1' , estou tentando juntar um inteiro com uma string, eu deveria converter um desses
dois dados.

Só pode concatenar o mesmo tipo
"""

variavel_int = int('2') # transformei a string em um inteiro
print(f'Variavel {variavel_int} que antes era string se tornou do tipo : {type(variavel_int)}')

"""
int()  converte para inteiro
 
float() converte para float

str() converte para string

"""

print('Um bool vazio é considerado false. EX : bool(""), resultado :', bool(''))
print('Se tiver um espaço em branco ou algo, será true: bool(" "), resultado: ', bool(" "))



