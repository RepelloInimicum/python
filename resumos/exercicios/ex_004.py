# Exercício Python #004 - Dissecando uma Variável

def mensagem():
	print(f'Valor do tipo {type(algo).__name__}')


algo = input('Digite qualquer coisa... ')

try:
	if '.' in algo:
		algo = float(algo)
		mensagem()
	else:
		algo = int(algo)
		mensagem()
except ValueError:
		mensagem()