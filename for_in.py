"""
For in Python
While é utilizando quando não sabemos o final
Já o For, é quando temos algo que sabemos que tem final
iteração string com for
Função range(start = 0, stop, step = 1)
"""
# palavra = 'texto'

# for letra in palavra:
#     print(letra)


"""
For + Range

range -> range(start = 0, stop = final, step = 1) -> valores como padrão
Também é um iteravel, os dois são independentes um do outro

"""

# numeros = range(10) # quando eu passo 1 valor só, estou colocando o valor do stop
# vai começar do 0 e ir até o 9

# print(list(numeros))

# numeros = range(5,10)
# # negativo numeros = range(0, -10, -1)

# for numero in numeros:
#     print(numero)

"""
O for pega seu iterável, ele pede para seu iterador qual é o próximo valor, e entrega nessa variável qual é o
próximo iterador, acaba quando ele recebe um erro chamada de stop iteration, informa para o for que não tem mais
valores e para.
"""

# Iterável -> str, range, etc
# Iterador -> quem sabe entregar um valor por vez
# next -> me entregue o próximo valor
# iter -> me entregue seu iterador

# métodos são ações que irá realizer no objeto, precisa de parênteses para executar a ação

# texto = 'LucasBindeli'.__iter__()

texto = iter('LucasBindeli') # irá retornar o endereço de memória do iterador

# método __iter__() me retorna um iterador

print(texto.__next__())
print(texto.__next__())
print(texto.__next__()) # se passar do limite, irá aparece um erro
print(next(texto))
print(next(texto))

texto_1 = 'Lucas'           # iterável - o cara que tem os elementos
iterador = iter(texto_1)    # iterator    

# O for faz basicamente isso :
while True:
    try:
        print(next(iterador))
    except StopIteration: #ele vai tratar só desse erro, outro não me importa
        break
    # Quando o Try perceber o erro sinalizado, ele vai jogar para o except
print('\nEnd\n')

"""
Mesma coisa : 

for letra in texto_1:
    print(letra)

"""
""""
O QUE EU APRENDI COM WHILE TAMBÉM FUNCIONA COM FOR DE SEU JEITO

"""
for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')
#___________________________________________________________________________________________

"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.

- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está
na palavra secreta.

    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;

    - Se a letra digitada não estiver
    na palavra secreta; exiba *.

Faça a contagem de tentativas do seu usuário.
"""
import os
print('\n\nJogo da Palavra Secreta!!!!')
palavra_secreta = 'palavra'
 
letras_acertadas = ''
chances = 10

while chances >= 0:
    letra_digitada = input('\nDigite uma letra: ')

    

    if len(letra_digitada) > 1 or len(letra_digitada) < 1:
        print('Digite somente uma letra!')
        continue

    if letra_digitada in palavra_secreta:  
        letras_acertadas += letra_digitada
    else:
        print('Você errou!')
        chances -= 1
        continue            

    nova_palavra = ''   
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            nova_palavra += letra
        else:
            nova_palavra += '*'
    

    if nova_palavra == palavra_secreta:
        print('Parabéns! Você acertou a palavra secreta!!')
        break
    else:
        print('A palavra está assim: ', nova_palavra)

print(f'Final : {nova_palavra}')
    





















