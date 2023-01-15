"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

variavel_1 = "ABC"

print(f'{variavel_1}')
print(f'{variavel_1: >10}.') #dois pontos, espaço(que é o dígito), direção/quantidade
print(f'{variavel_1:#<10}.')

print(f'{1000.56548:.2f}')
print(f'{-1000.56548:-.2f}') # ele tem que ser um número negativo
print(f'{1000.56548:+.2f}')

print(f'{1000.56548:0=+10.2f}')
print(f'{1000.56548:0>+10.2f}')
print(f'{1000.56548:0<+10.2f}') 

print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'O hexadecimal de 1500 é {1500:X}')
