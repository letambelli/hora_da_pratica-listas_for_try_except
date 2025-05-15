numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0

for numero in numeros:
    if numero % 2 != 0:
        soma = soma + numero

print(f'A soma dos números ímpares de 1 a 10 é {soma}')