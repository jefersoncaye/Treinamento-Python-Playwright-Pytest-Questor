carros = ['Mercedes', 'BMW', 'Ferrari', 'Porsche', "Bugatti"]

for carro in carros:
    print(carro)

for carro in carros:
    if carro == 'BMW':
        print(carro)


#usando enumerate no for
for indice, carro in enumerate(carros):
    print(f'Indice: {indice}, Carro: {carro}')


#range(start, stop, step)
#for indice in range(90, 10, -1):
#for indice in range(10, 91, 1):
#for indice in range(10, 91):
for indice in range(90):
    print(indice)

string = 'Hoje eu almocei lasanha'

for letra in string:
    print(letra)

for i in range(10):
    print(f'indice i = {i}')
    for j in range(20):
        print(f'indice j = {j}')