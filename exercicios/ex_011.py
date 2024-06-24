# Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

while True:
	try:
		largura = float(input('Digite a largura da parede em metros: '))
		altura = float(input('Digite a altura da parede em metros: '))
		break
	except ValueError:
		print('Valor inválido!')

area = largura * altura
litro_tinta = 2

tinta_necessaria = area / litro_tinta

print(f'{'Largura:':<10}{largura:>8}m\n{'Altura:':<10}{altura:>8}m\n{'Área:':<10}{area:>8}m²')
print(f'{tinta_necessaria:.2f} litros de tinta')