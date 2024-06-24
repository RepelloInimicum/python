# Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
# Formula de conversão: F = C * 9/5 + 32

while True:
	try:
		C = float(input('Temperatura em Celcius: '))
		F = C * 1.8 + 32
		print(f'{'Celcius':<12}{C:>5.1f}°C\n{'Fahrenheit':<12}{F:>5.1f}°F')
		break
	except ValueError:
		print('Tente novamente...')