lista = [10, 1, 2, 3, 8, 'Olá', 2.89, True, 5, [8, 'Boa Tarde']]
# Indices   0,  1, 2, 3, 4,  5   , 6   , 7   , 8, 9[0, 1         ]

"""print(lista)

# Acessando posições em uma lista

print(lista[5])
print(lista[9][1]) # acessando a lista dentro de outra lista

# contar elementos de uma lista
print(len(lista))

# acessar o ultimo elemento da lista
print(lista[-1])
print(lista[-5])

# acessar parte de uma lista
print(lista[0:5]) # acessa o elemento do indice 0 até o indice 4
"""

"""
Metodos:
append - adiciona o item ao final da lista;
insert - insere um item na lista na posição indicada
del - remove um item da lista baseado na posição indicada;
pop - remove o ultimo item da lista ou o indice passado
remove - remove da lista_compras o último item, mas não o exclui.
clear - limpa a lista
"""
lista = [10, 1, 2, 3, 8, 'Olá', 2.89, True, 5, [8, 'Boa Tarde']]
print(lista)

# Append
lista.append('Boa Noite')
print(lista)

# Insert
lista = [10, 1, 2, 3, 8, 'Olá', 2.89, True, 5, [8, 'Boa Tarde']]
lista.insert(1, 'Boa Tarde')
print(lista)

# del
lista = [10, 1, 2, 3, 8, 'Olá', 2.89, True, 5, [8, 'Boa Tarde']]
del lista[1]
print(lista)

# pop
lista = [10, 1, 2, 3, 8, 'Olá', 2.89, True, 5, [8, 'Boa Tarde']]
lista.pop()
print(lista)
elemento_removido = lista.pop(0) # o pop retona o elemento que foi removido, diferende do del
print(lista)
print(elemento_removido)

# remove
lista = [10, 1, 2, 3, 8, 'Olá', 2.89, True, 5, [8, 'Boa Tarde']]
lista.remove('Olá')
print(lista)

# clear
lista = [10, 1, 2, 3, 8, 'Olá', 2.89, True, 5, [8, 'Boa Tarde']]
lista.clear()
print(lista)