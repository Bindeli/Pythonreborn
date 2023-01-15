"""
Operadores Lógicos

and -  or  - not

and - todas as condições precisam ser verdadeiras, se um for falso, o resultado é falso.

Também existe o tipo None, que é usado para representar um não valor, quase que falso.

True and True = True
True and False = False
False and False = False
"""

entrada = input('[E]ntrar ou [S]air? R:').lower()

usuario = 'lucas'
senha = 'senha'

if entrada == 'e':
    print('Você entrou no sistema!\n')
    usuario_digitado = input('Digite o usuário: ') 
    senha_digitada = input('Digite a senha: ')
    if senha_digitada == senha and usuario_digitado == usuario:
        print('\nVocê entrou no sistema com sucesso!\n')
    else:
        print('\nUsuário incorreto ou senha incorreta\n')
elif entrada == 's':
    print('Você saiu do sistema.')
else:
    print('Escolha uma opção válida!')

print(True and False and True)

print('\n\n')

#___________________________________________________________________________________________________________

"""
or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.

TRUE or False or False = true

True or True = True
True or False = True
False or False = False

"""

print('Operador OR [True or False or False]:', end='')
print(True or False or False)

num1 = 2
num2 = 6
num3 = 42
num4 = 6

if num1 > num3 or num3 > 4:
    print('Uma das expressões utilizando OR é verdadeira')
else:
    print('As duas expressões utilizando OR são falsas')
#___________________________________________________________________________________________________________
"""
NOT

Usado para inverter expressões

not True = False
not False = True

"""
print(f'\nUtilizando o Not')
print('not True: ', end='')
print(not True)
print('not False', end='')
print(not False)

# podemos verificar também se o conteúdo está vazia

#___________________________________________________________________________________________________________
"""
Operadores IN e NOT IN

Para verificar se um valor está ou não presente em algo, como uma letra está em uma string

0 1 2 3 4
L U C A S

"""
print('\nPraticando IN e NOT IN')
nome = 'lucas'
print(f'Verificando se l está presente no nome com IN: ', end='')
print('l' in nome)
print(f'Verificando se c não está presente no nome com NOT IN: ', end='')
print('c' not in nome)

print(f'Irá dar false, pois a letra "c" está presente na variável.')

print('\n')