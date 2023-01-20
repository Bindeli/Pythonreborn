"""

entrada = input('Digite o cpf : )
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)

tudo que não for números de 0 a 9, será substituido por '', que no caso será nada
eu coloco entre aspas que, ficará no lugar dos dígitos que não foram de 0 a 9

"""


"""

import sys

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

finaliza o python
"""