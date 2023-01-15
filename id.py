"""
Variável é algo que está na memória, e o Python busca pelo id do elemento.

"""

variavel_1 = 'Lucas'

# utilizamos id para verificar o id
print(id(variavel_1))

variavel_2 = 'Lucas'

print(id(variavel_2))


# Valores iguais terão o mesmo id, as duas variáveis apontam para o mesmo valor na memória

# se eu alterar o valor dela, será atribuído outro id

variavel_2 = 'LucasB'
print(id(variavel_2))