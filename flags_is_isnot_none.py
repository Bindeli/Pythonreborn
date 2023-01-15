"""
Flag (Bandeira) - Marcar um local
Ficando uma bandeira em um local do código, e utilizamos o None para verificar se passou ou não

None = Não valor

is e is not = é ou não é (tipo, valor, identidade)

id = Identidade

As vezes eu quero saber se o interpretador passou em um local por um motivo qualquer.
Depende do algoritmo que você estiver criando.
Algoritmo = solução para que você criou para determino problema.

"""
condicao = True

passou_no_if = None # Não tem um valor específico

if condicao:
    passou_no_if = True
    print('Dentro do if')
else:
    print('Passou no Else, não fez nada.')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

#___________________________________________________________________________________________

print('\n\nExercícios: ')

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
print('Exercício 1:')
numero_ex1 = input('Digite um número para verificar se é par ou ímpar: ')

"""
if numero_ex1.isdigit():
    numero_ex1 = int(numero_ex1)
    if numero_ex1 % 2 == 0:
        print('Seu número é PAR')
    else:
        print('Seu número é Ímpar')
else:
    print('Digite um número inteiro')

print('\nCom o try e except:')
"""

try:
    numero_ex1 = int(numero_ex1)
    if numero_ex1 % 2 == 0:
        print('Seu número é PAR')
    else:
        print('Seu número é Ímpar')
except:
    print('Digite um número inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
print('\nExercício 2:')

hora_ex1 = input('Insira a hora atual: ')

"""
if hora_ex1.isdigit():
    hora_ex1 = int(hora_ex1)
    if hora_ex1 < 0 or hora_ex1 > 23:
        print('Escolha uma hora entre 0 à 23!')
    else:
        if hora_ex1 <= 11:
            print('BOM DIA!!!!')
        elif hora_ex1 <= 17:
            print('BOA TARDE!!!!')
        else:
            print('BOA NOITE!!!!!!')
else:
    print('Digite um valor inteiro!!')
"""

try:
    hora_ex1 = int(hora_ex1)
    if hora_ex1 < 0 or hora_ex1 > 23:
        print('Escolha uma hora entre 0 à 23!')
    else:
        if hora_ex1 <= 11:
            print('BOM DIA!!!!')
        elif hora_ex1 <= 17:
            print('BOA TARDE!!!!')
        else:
            print('BOA NOITE!!!!!!')
except:
    print('Digite um valor inteiro!!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
print('\nExercício 3:')

nome_ex = input('Escreva seu nome: ')

if len(nome_ex) > 1:
    if len(nome_ex) <= 4:
        print('Seu nome é curto!')
    elif len(nome_ex) <= 6:
        print('Seu nome tem tamanho normal!')
    else:
        print('Seu nome é muito grande!')
else:
    print('Digite alguma coisa!!')
print('\n')