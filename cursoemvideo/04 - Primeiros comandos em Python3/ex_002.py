# Exercício Python #002 - Respondendo ao Usuário
# Exercício Python 002: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

# Lemos o nome utilizando uma função input que irá armazenar o valor recebido na variável nome.
nome = input('Digite o seu nome: ').strip().title()

# Exibimos o resultado formatado
print(f'Olá, {nome}. Seja muito bem-vindo!')

# Utilizamos o método strip() para remover espaços em branco no início e no final da string.
# Utilizamos o método title() para deixar a primeira letra de cada palavra em maiúscula.