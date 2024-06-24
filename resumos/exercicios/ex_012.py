# Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
while True:
	try:
		original = float(input('Digite o valor do produto: R$ '))
		break
	except ValueError:
		print('Valor inválido!')


print(f'{'Valor original:':<20}R${original:>10.2f}\n{'DESCONTO DE 5%:':<20}R${original*.05:>10.2f}\n{'Valor final:':<20}R${original*.95:>10.2f}')