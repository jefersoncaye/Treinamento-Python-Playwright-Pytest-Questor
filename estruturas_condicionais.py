"""
Operadores Logicos

== Igual
!= Diferente
>= Maior ou Igual
<= Menor ou Igual
> Maior
< Menor
or OU
and E
"""

"""
nome = 'Jeferson'

if nome:
    print(f'A variavel nome não está vazia')
    print(f'conteudo da variavel: {nome}')

nome = ''

if nome:
    print(f'A variavel nome não está vazia')
    print(f'conteudo da variavel: {nome}')

nome = 'Jeferson'

if nome == 'jeferson':
    print('Nome é igual jeferson')

if nome == 'Jeferson':
    print('Nome é igual Jeferson')

if nome.lower() == 'jeferson':
    print('Nome é igual Jeferson')

if nome != 'José':
    print('Nome não é José')

numero = 10

if numero == 10:
    print(f'numero é igual 10')

if numero > 10:
    print(f'numero é maior que 10')

if numero >= 10:
    print(f'numero é maior ou igual a 10')

if numero < 10:
    print(f'numero é menor que 10')

if numero <= 10:
    print(f'numero é menor ou igual a 10')

boleano = True


if boleano is False:
    print('boleano é Falso')

if boleano:  # Equivalente a if boleano == True
    print('boleano é True')
"""

"""
IF ELSE e ELIF
"""

"""
numero = int(input('Digite um numero: '))

if numero == 1:
    print('Numero = 1')
elif numero == 2:
    print('Numero = 2')
elif numero >2:
    print('Numero maior que 2')
elif numero == 3: # Explicar a diferença entre esse caso ser um if e um elif
    print('Numero = 3')
else:
    print('Numero não é 1, não é 2 e tambem não é maior que 2')
"""

"""
OR e AND
"""

fruta = 'tomate'
numero = 25
objeto = 'Pratos'

if fruta == 'tomate' or numero == 40:
    print('Fruta é igual "tomate" OU numero é igual 40')

if fruta == 'tomate' and numero == 40:
    print('Fruta é igual "tomate" E numero é igual 40')

if (fruta == 'tomate' and numero == 40) or objeto == 'Prato': # sempre que utilizar and e or juntos optar por usar parenteses para deixar mais legivel
    print('Fruta é igual "tomate" E numero é igual 40 OU Objeto é igual "Prato"')


