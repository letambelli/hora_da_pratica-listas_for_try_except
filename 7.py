lista = [1, 2, 3]
dividendo = 0
divisor = 0
media = 0

for elemento in lista:
        dividendo += elemento
        divisor +=1

try:
    media = dividendo/divisor
    print('Média:', media)
except ZeroDivisionError:
      print('A lista está vazia.')
