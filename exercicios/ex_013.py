# Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

while True:
	try:
		salário = float(input('Digite o valor do salário: R$ '))
		break
	except ValueError:
		print(f'Valor não é válido para essa operação!')

print(f'{'Salário atual:':<20}R${salário:>10.2f}\n{'Aumento de 15%:':<20}R${salário*.15:>10.2f}\n{'Novo salário:':<20}R${salário*1.15:>10.2f}')