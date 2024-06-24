# Exercício Python 002: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input('Digite o seu nome: ')
mensagem = f'Olá \033[1;31m{nome}\033[m. Seja bem-vindo! É um prazer te conhecer.'
print(mensagem)