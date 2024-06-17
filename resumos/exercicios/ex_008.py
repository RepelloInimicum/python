# Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Valor em metros: '))

quilometros = metros / 1000
hectometros = metros / 100
decametros = metros / 10
decimetros = metros * 10
centimetros = metros * 100
milimetros = metros * 1000

print(f'{"Quilômetros":<15}{quilometros:>5.3g}km')
print(f'{"Hectômetros":<15}{hectometros:>5.3g}hm')
print(f'{"Decâmetros":<15}{decametros:>5.3g}dam')
print(f'{"Metros":<15}{metros:>5.0f}m')
print(f'{"Decímetros":<15}{decimetros:>5.0f}dm')
print(f'{"Centímetros":<15}{centimetros:>5.0f}cm')
print(f'{"Milímetros":<15}{milimetros:>5.0f}mm')

# :.3g formata o número para exibir até três dígitos significativos, removendo zeros desnecessários à direita.