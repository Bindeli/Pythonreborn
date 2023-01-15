"""
https://docs.python.org/pt-br/3/library/stdtypes.html

Imutáveis que vimos : str, int, float, bool.


"""

string = 'Lucas Bindeli'
# não poderia fazer string[3] = A, para mudar o valor 
# teria que fazer igual a opção abaixo

outra_string = f'{string[:3]}ABC{string[4:]}'

print(f'Primeira string : {string}')
print(f'Segunda string modificada: {outra_string}')



