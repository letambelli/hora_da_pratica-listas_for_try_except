numero = int(input('Digite um número para saber sua tabuada: '))
n = 0

print()

for n in range(0, 11):
    print(f'{numero} x {n} = {numero*n}')
    n += 1