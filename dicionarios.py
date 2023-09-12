dicionario = {
    'nome': 'Pedro',
    'idade': 28,
    'altura': 1.78
}

print(dicionario.keys()) # Print Apenas das Chaves do Dicionario
print(dicionario.values()) # Print Apenas dos Valores do Dicionario

# Adicionar item ao Dicionario

dicionario['sobrenome'] = 'Silva'

print(dicionario)

# Removendo item do Dicionario
dicionario = {
    'nome': 'Pedro',
    'idade': 28,
    'altura': 1.78,
    'sobrenome': 'Silva'
}
# pop()
dicionario = {
    'nome': 'Pedro',
    'idade': 28,
    'altura': 1.78,
    'sobrenome': 'Silva'
}
item_removido = dicionario.pop('sobrenome')
print(item_removido)
print(dicionario)

# del
dicionario = {
    'nome': 'Pedro',
    'idade': 28,
    'altura': 1.78,
    'sobrenome': 'Silva'
}
del dicionario['altura']
print(dicionario)

# clear()
dicionario = {
    'nome': 'Pedro',
    'idade': 28,
    'altura': 1.78,
    'sobrenome': 'Silva'
}
dicionario.clear()

print(dicionario)

# Alterando item do Dicionario

dicionario = {
    'nome': 'Pedro',
    'idade': 28,
    'altura': 1.78,
    'sobrenome': 'Silva'
}

dicionario['nome'] = 'Marcelo'
print(dicionario)

dicionario = {
    'nome': 'Pedro',
    'idade': 28,
    'altura': 1.78,
    'sobrenome': 'Silva'
}

# Iterando em um dicionario
print(dicionario.items())

for chave, valor in dicionario.items():
    print(f'Chave: {chave}, Valor: {valor}')