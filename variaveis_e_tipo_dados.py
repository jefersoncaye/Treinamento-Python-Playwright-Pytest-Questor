mensagem = 'Exemplo de uma Mensagem!'

inteiro = 25

decimal = 25.9

boleano = True

print(type(boleano))

# criando varias variaveis em sequencia
a, b, c = 1, 2, 3

print(a)

print(float(inteiro))
print(int(decimal)) # não arredonda, sempre corta
#decimal = str(decimal)
print(decimal)
print(type(decimal))

# erro ao tentar alterar para tipo de dado invalido
#print(int(mensagem))

resultado = inteiro + decimal
print(resultado)
print(type(resultado))