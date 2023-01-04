print('Utilizada para exibir as coisas na tela e recebe argumento')

print(123)

print(12, 34) # dois argumentos, com a vírgula entre eles para separar

# sep  é um separador que vai separar com um dígito definitivo pelo dev

print(12, 53, sep='-') # vai separar os dois pelo traço 

print(50, 100, sep=".")

# no final de cada print, temos um quebra linha de padrão e ele não aparece, porém podemos utilizar o end

# \r\n -> CRLF
# \n  -> LF

# CRFL no canto inferior para windows , LF para mac

# end significa o final do print, como ele vai finalizar, 

print('')

print(1, 2, 100, sep='-', end='\r\n')
print(1, 2, 100, sep='-', end='\n')
print('Frase1.', end='') # aqui ele irá puxar o print abaixo, pois não tem o comando \r\n para saltar a linha
print('Frase2')

#  a mesma coisa para outro caracter, não precisa ser vazio

print('123.456.789', end='-')
print('10')

print('\nFinal do Código.\n')