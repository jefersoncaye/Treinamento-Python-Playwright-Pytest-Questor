num1, num2 = 10, 15.5

# soma

soma = num1 + num2
print(f'Soma = {soma}')

# subtração

subtracao = num1 - num2

print(f'Subtração = {subtracao}')

# multiplicação

multiplicacao = num1 * num2

print(f'Multiplicação: {multiplicacao}')

# divisão

divisao = num2 / num1

print(f'Divisão: {divisao}')

# Divisão Inteira

divisao_inteira = num2 // num1

print(f'Divisão Inteira: {divisao_inteira}')
"""
15.5/10
10    1
5.5
"""

# Resto de Divisão

resto_diviao = num2 % num1

print(f'Resto Divisão: {resto_diviao}')
"""
15.5/10
10    1
5.5
"""

# exponenciação

exponenciacao = num1 ** num2

print(f'Exponenciação: {exponenciacao}')

# Arredondamento

num3 = 18.6
print(f'Numero Arredondado: {round(num3)}')
num3 = 18.5
print(f'Numero Arredondado: {round(num3)}')

# Hierarquia Matematica

print(3 * 2 - 7)  # 3 * 2 = 6  | 6 - 7 = -1
print(3 * (2 - 7))  # 2 - 7 = -5   |  3 * -5 = -15
