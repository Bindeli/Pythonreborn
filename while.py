"""
While - Repetição
Utilizando para realizar ações enquanto uma condição for verdadeira
Requisitos : Entender condições e operadores

continue - pula para o próximo laço
break - finaliza a repetição
"""

# Enquanto a condição for verdadeira, irá repetir o código
# contador = 0
# while contador < 2:
#     nome = input('Qual o seu nome ? ')
#     print(f'Olá {nome}!')
#     # contador irá receber ele e irá somar mais um para não travar o contador em somente um número
#     # fazendo que o código rode até determinado número da condição do while
#     contador += 1
#     print(f'Valor do contador: {contador}')
# print('')
#____________________________________________________________________________________________________
# Para exibir uma contagem com número até tanto valor
print('Exibindo uma contagem!')
g = 1
while g < 5:
    # caso eu queira pular o numero 3
    if g == 3:
        g = g + 1
        print('Pulei o número 3.')
    print(f'Número {g}!')
    # g recebe ele mesmo e mais um, para avançar até chegar na condição do while
    g = g + 1

#____________________________________________________________________________________________________
# continue e break
# continue é utilizado para pular para o próximo laço

print('\nUTILIZANDO O CONTINUE')
z = 0
while z <= 5:
    if z == 3:
        z = z + 1
        print('Irá pular.')
        # ele irá pular para o próximo laço, mas antes tenho que adicionar um valor para o contador
        continue
    print(f'Número atual de Z é: {z}')
    z = z + 1

#____________________________________________________________________________________________________
# já o break, irá parar toda repetição, o break irá forçar a saida do loop

c = 0
print('\nUTILIZANDO O BREAK')
while c <= 10:
    # caso eu queira parar no 4
    if c == 4:
        print('O break irá finalizar o laço agora.')
        break
    print(f'O número atual de C é {c}')
    c = c + 1

print()
#_______________________________________________________________________________________________
"""
Operadores de atribuição

contador += 1       mesmo que -> contador = contador + 1
contador -= 1       mesmo que -> contador = contador - 1
contador *= 1       mesmo que -> contador = contador * 1
contador /= 1       mesmo que -> contador = contador / 1
contador //= 1      mesmo que -> contador = contador // 1    
contador **= 1      mesmo que -> contador = contador ** 1
contador %= 1       mesmo que -> contador = contador % 1    
"""

# uma mini tabela
x = 0 # Coluna
y = 0 # linha

while x < 2:
    y = 0 # para reiniciar as linhas para ir para a próxima coluna
    while y < 2:
        print(f'X={x} e Y={y}')
        y += 1

    x += 1

#_______________________________________________________________________________________________

"""
Iterando strings com while
"""
#       
nome = 'Lucas Bindeli'  # Iteráveis

# Objetivo : A cada iteração, mostre um dígito da string
# Objetivo : nova_string += '*L*u*c*a*s* *B*i*n*d*e*l*i*'

print('\nPrimeiro Exemplo: ')
contador = 0
while contador < len(nome):
    print(nome[contador])
    contador += 1

print('\nSegundo Exemplo: ')

contador_2 = 0
novo_nome = ''
while contador_2 < len(nome):
    # novo_nome = novo_nome + "*" + nome[contador_2]
    novo_nome += f'*{nome[contador_2]}'
    print(novo_nome)
    contador_2 += 1

print('O final da nova string ficou assim : ', novo_nome)
#_______________________________________________________________________________________________

"""
While / Else 

Quando finalizar o While, o else será executado 
Caso um break seja ativado no While, o else não será executado.
"""
contador = 1

# um valor que você vai adicionar a cada laço
acumulador = 1

# o while será executado até a expressão se tornar falsa
while contador <= 3:
    print(f'Contador atual é {contador} e acumulador será de {acumulador}')
    # a cada laço, vai receber ele e o contador, só de exemplo, pode ser qualquer valor
    acumulador = acumulador + contador
    contador += 1
else:
    print('Agora é a vez do else logo após o while')

# caso eu crie uma condição e utilize o break neste laço, irá também rejeitar o else que está no laço while
# if algo, break, vai ignorar o else também
contadorbreak = 1
print('')
while contadorbreak < 5:

    if contadorbreak == 4:
        break

    print(f'Contador : {contadorbreak}')
    contadorbreak += 1
else:
    print('No break, o else, não será executado')
print('No contador 4 irá dar um break no código e irá pular o else')

#_______________________________________________________________________________________________

"""
Calculadora em Python

Pedir um primeiro e segundo número ao usuário
E pedir para selecionar um Operador
"""
print('\nCalculadora em Python')


while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite um segundo número : ')


    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
        operador = input('Selecione um Operador: \n1: [+]\n2: [-]\n3: [*]\n4: [/]\n5: [Sair]\nSelecione: ')
        if operador == '1':
            print(f'A soma de {num_1}+{num_2} = {num_1 + num_2}')
        elif operador == '2':
            print(f'A subtração de {num_1}-{num_2} = {num_1 - num_2}')
        elif operador == '3':
            print(f'A multiplicação de {num_1}*{num_2} = {num_1 * num_2}')
        elif operador == '4':
            print(f'A divisão de {num_1}/{num_2} = {num_1/num_2}')
        elif operador == '5':
            break
        else:
            print('Selecione um operador!!')
            continue
    except:
        print('Escreva um número inteiro!!')

    print('\n')

#_______________________________________________________________________________________________
















#_______________________________________________________________________________________________