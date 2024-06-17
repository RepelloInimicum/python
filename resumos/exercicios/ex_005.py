# Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

while True:
	try:
		numero = int(input('Digite um valor: '))
		break
	except ValueError:
		print('Digite apenas números inteiros!')

antecessor = numero - 1
sucessor = numero + 1
print(f'Você digitou o número {numero}.\n')
print(f'\033[1;31m{antecessor:.<5}\033[m\033[1m{numero:.^5}\033[m\033[1;32m{sucessor:.>5}\033[m')