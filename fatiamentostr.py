"""
Fatiamento de strings 

Strings são iteráveis, os indices começam desde o zero

 012345678
 Olá mundo
-987654321

Fatiamento [inicio:fim:passo] [::] passo seria os pulos
Obs.: a função len retorna a qtd 
de caracteres da str
"""
print('\n')
variavel = 'Lucas Bindeli' # o espaço também tem indice
print(f'Variável : {variavel}')
print(f'No indice 6 teremos : {variavel[6]}')
print(f'Começando do indice 2 e indo até o final : {variavel[6:]}')
print(f'Começando do indice 2 e indo até o indice 8: {variavel[6:8]}') 
# vai até o 7, o valor do indice 8 não aparece

print(f'Com a função len, contamos a quantidade de valores teremos: {len(variavel)}')
print('Teremos 13 caracteres e o indice vai de 0 até 12.')
print(variavel[0:len(variavel)])
print(variavel[0:len(variavel):2])

# invertendo colocando negativo no passo

print(f'Invertendo com passo negativo : {variavel[::-1]}')
print('\n')

#___________________________________________________________________________________________

"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
print('\n\n')

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if not nome or not idade:
    print("Desculpe, você deixou campos vazios.")
else:
    print(f'Seu nome é : {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome {nome} contém espaço!')
    else:
        print(f'Seu nome {nome} não contém espaço')
    print(f'Seu nome contém {len(nome)}')   
    print(f'A Primeira letra de seu nome é {nome[0]}') 
    print(f'A última letra de seu nome é {nome[-1]}')



print('\nFim\n')