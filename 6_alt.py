lista = ['Ana', 23, 'Gabriel', 22, 'Ana', 25]
soma = 0

for elemento in lista:
    try:
        soma += elemento
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

print(f'A soma total é igual a {soma}')