import random
# para coisas aleatórias
import sys
nove_digitos = ''

# print(random.randint(0,9)) # quero um nome aleatório entre 0 e 9

for itens in range(9):
    nove_digitos += str(random.randint(0,9))

# print(nove_digitos)
# sys.exit()

contagem_regressiva = 10

resultado_dig_1 = 0

for digito in nove_digitos:
    resultado_dig_1 += int(digito) * contagem_regressiva
    contagem_regressiva -= 1
digito_1 = (resultado_dig_1*10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contagem_regressiva_2 = 11
resultado_dig_2 = 0

for digito in dez_digitos:
    resultado_dig_2 += int(digito) * contagem_regressiva_2
    contagem_regressiva_2 -= 1
digito_2 = (resultado_dig_2*10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_final = dez_digitos + str(digito_2)

# cpf_gerado = f'{novedigitos}{digito1}{digito2}'

print('CPF FINAL: ', cpf_final)


