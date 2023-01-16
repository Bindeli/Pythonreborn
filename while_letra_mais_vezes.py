"""
Qual letra irá aparecer mais vezes na frase ?
"""

frase = "O Python é uma linguagem de programação multiparadigma.Python foi criado por Guido Van Rossum"

# Método de string count = Retorna o número de vezes que o valor aparece na string

# print(frase.count('a'))
i = 0

qtd_apareceu_mais_vezes = 0
letra_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    if letra_atual == ' ':
        i += 1
        continue
    else:
        quant_letra_atual = frase.count(letra_atual)
        if qtd_apareceu_mais_vezes < quant_letra_atual:
            letra_mais_vezes = letra_atual  
            qtd_apareceu_mais_vezes = quant_letra_atual 
    i += 1

print(f'A letra que apareceu mais vezes foi : {letra_mais_vezes} = {qtd_apareceu_mais_vezes}')