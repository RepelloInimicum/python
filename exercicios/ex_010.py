# Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.


def valores():
	while True:
		try:
			return float(input('Quantos reais você possui? '))
		except ValueError:
			print(f'O valor digitado não é válido para essa operação.')

real = valores()

dolar = real / 5.15

print(f'{'-'*13}\nR$ {real:>10.2f}\n{'-'*13}\nU$ {dolar:>10.2f}\n{'-'*13}')