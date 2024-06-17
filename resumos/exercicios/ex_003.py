# Exercício Python 003: Crie um programa que leia dois números e mostre a soma entre eles.

def obter_valores(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print(f'Opa! Valor inválido!')

x = obter_valores('Digite o primeiro valor: ')
y = obter_valores('Digite o segundo valor: ')

soma = x + y
print(f'{x:>10}\n+{y:>9}\n{'-'*10}\n{soma:>10}')