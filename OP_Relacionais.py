"""
Operadores de comparação (relacionais)

OP      Significado         Exemplo (True)

>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'

Vai retornar um bool
"""
maior = 2 > 1 #True
maior_ou_igual = 2 >= 2 #True
menor = 1 < 2 #True
menor_ou_igual = 2 <= 2 #True
igual = 'a' == 'a' #True
diferente = 'a' != 'b' #True
print('Olha meu print aqui\n')
#__________________________________________________________________________________________
"""
Utilizando os operadores de comparação e condicional
Verifique com dois números, qual é o maior.

Colocando essas frases : {valor} é maior que {valor}
"""
primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor.isdigit() and segundo_valor.isdigit():
    primeiro_valor = int(primeiro_valor)
    segundo_valor = int(segundo_valor)
    if primeiro_valor > segundo_valor:
        print(f'{primeiro_valor} é maior que {segundo_valor}')
    elif primeiro_valor == segundo_valor:
        print(f'{primeiro_valor} e {segundo_valor}! Valores iguais.')
    else:
        print(f'{segundo_valor} é maior que {primeiro_valor}')
else:
    print('\nDigite números inteiros!')   
print('\nEnd\n')