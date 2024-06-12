# Exercício Python #001 - Deixando tudo pronto

"""Nesse vídeo, mostraremos como criar um projeto Python no PyCharm e deixar tudo preparado para receber os exercícios da série, que vão utilizar o mesmo projeto.
"""

# Desafio 0001 - Aula 4 - Crie um programa que escreva "Olá, Mundo!" na tela.

# Exibindo a mensagem diretamente com uma instrução, print
print('Olá, Mundo!')

# Exibindo o valor de uma variável com a instrução print, utilizando a variável como argumento
mensagem = 'Olá, Mundo!'
print(mensagem)

# Atualizamos a variável criada anteriormente, agora seu valor será fornecido pelo usuário e exibido na tela
mensagem = input('Digite a mensagem que deseja exibir: ')

# Neste exemplo utilizamos as duas variantes de aspas na mesma sentença, respeitando a sintaxe. As aspas simples estão envolvendo as aspas duplas, indicando que as aspas duplas se referem a uma citação e as simples fazem parte da sintaxe de uma cadeia de carcteres
print(f'A mensagem digitada foi: "{mensagem}"')