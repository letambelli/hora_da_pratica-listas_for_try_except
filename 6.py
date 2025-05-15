lista = ['Ana', 23, 'Gabriel', 22, 'Ana', 25]
soma = 0

for elemento in lista:
    try:
        soma += elemento
    except TypeError:
        None

print(f'A soma total é igual a {soma}')