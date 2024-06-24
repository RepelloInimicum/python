# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

while True:
	try:
		numero = float(input('Digite um valor qualquer: '))
		break
	except ValueError:
		print('O número digitado não é válido!')

verificador = numero % 1
if verificador == 0:
	numero = int(numero)

print(f'Você digitou o valor {numero}')
print(f'O dobro de {numero} é {numero * 2}')
print(f'O triplo de {numero} é {numero * 3}')
print(f'A raiz quadrada de {numero} é {numero ** .5}')