# Exercício Python #003 - Somando dois números
# Exercício Python 003: Crie um programa que leia dois números e mostre a soma entre eles.

# Lemos os dois números utilizando a função input, que irá armazenar os valores recebidos nas variáveis num1 e num2.

# Devido ao fato de a função input retornar dados do tipo string e como sabemos, o operador de adição (+) é utilizado para concatenar strings, precisamos converter os valores recebidos para inteiros, para que possamos realizar a operação de soma.

# A sintaxe da conersão de dados é a seguinte: A função int() recebe um argumento que será convertido para inteiro. No caso, o argumento é a função input().

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

# Exibimos o resultado da soma dos dois números.
print(f'A soma entre {num1} e {num2} é igual a {num1 + num2}.')

# Se quisermos usar o resultado futuramente, podemos armazená-lo em uma variável.

soma = num1 + num2
