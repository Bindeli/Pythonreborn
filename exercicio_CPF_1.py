"""
Calculo do primeiro dígito do CPF

CPF: 746.824.890-70

Colete a soma dos 9 primeiros dígitos do CPF multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 

70+36+48+56+12+20+32+27+0 = 301

Multiplicar o resultado anterior por 10

301 * 10 = 3010

Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7

Se o resultado anterior for maior que 9:
    resultado é 0

contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
cpf_inicio = '74682489070'
cpf_edit = cpf_inicio[:-2]
soma_resultado = 0
indice = 10
digito = 0


for valores in cpf_edit:
    soma_resultado += int(valores) * indice
    indice -= 1
valor = (soma_resultado * 10) % 11

if valor > 9:
    digito = 0
else:
    digito = valor

print('O Valor do digito é : ', digito)

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""

indice_2 = 11
cpf_edit += str(digito)
soma_resultado_2 = 0
digito_2 = 0
for valores in cpf_edit:
    soma_resultado_2 += int(valores) * indice_2
    indice_2 -= 1
valor_2 = (soma_resultado_2 * 10)/11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_total = cpf_edit + str(digito_2)

if cpf_inicio == cpf_total:
    print(f'CPF é válido!!! {cpf_total}\n')
else:
    print(f'CPF digitado é inválido.')