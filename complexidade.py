"""
Constante = 'Variáveis' que não vão mudar, mostrar para os dev's que não pode mudar.

Utilizamos letras maiúsculas para coisas que não irão mudar no código.

EVITAR DE TER MUITAS CONDIÇÕES NO MESMO IF

"""


velocidade = 61 # velocidade atual do carro
local_carro = 99 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega, sendo 100 o local, 99 e 101 pegaria

"""
Eu quero saber se o carro passou da velocidade do radar.
"""
print('\nEtapa1\n')
if velocidade > RADAR_1:
    print('Passou da velocidade.')
else:
    print('Não passou da velocidade.')

#___________________________________________________________________________________________________________
velocidade = 51

print('\nEtapa2\n')
if velocidade > RADAR_1:
    print('Passou da velocidade.')
else:
    print('Não passou da velocidade.')

print('\nPara saber se o carro foi ou não mutado:')

# barra invertida para quebrar linha.
if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
    print('Carro multado em radar1')
else:
    print('Carro não foi multado.')

#___________________________________________________________________________________________________________

velocidade = 60


# Outro jeito seria colocando a expressão em uma variavel
print('\nPelo outro jeito, colocando as expressões na variável:\n')

vel_carro_pass_radar1 = velocidade > RADAR_1
carro_multado_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if vel_carro_pass_radar1 and carro_multado_radar1:
    print('O Carro foi multado no radar.')
else:
    print('O carro não foi multado.')

print("\n\n")