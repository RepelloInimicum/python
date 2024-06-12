# Curso Python #06 - Tipos Primitivos e Saída de Dados

"""Nessa aula, vamos aprender como funcionam os tipos primitivos no Python e as peculiaridades do int() float() bool() e str(). Além disso, veremos como fazer as primeiras operações com a função print() do Python.

Neste vídeo, o instrutor explica os tipos primitivos em Python, como inteiros, números de ponto flutuante, valores booleanos e strings. Ele demonstra como converter tipos e utilizar diferentes formas de exibir os resultados na tela.

Momentos-chave:
É importante entender os tipos primitivos na linguagem de programação Python, pois são fundamentais para o desenvolvimento de programas. Com o avanço do curso, mais tipos primitivos serão abordados conforme a necessidade. A importância dos tipos primitivos na programação e a promessa de abordar mais tipos ao longo do curso. Explicação sobre a utilização de aspas simples e duplas no Python, destacando a recomendação da comunidade para priorizar as aspas simples pela simplicidade do código.

O vídeo aborda a utilização de variáveis, comandos de input e print em Python, destacando a importância dos tipos primitivos como inteiros, reais, lógicos e strings. A importância da correta conversão de valores para tipos primitivos em Python para garantir o funcionamento adequado do código. Explicação dos quatro tipos primitivos básicos em Python: inteiros, reais, lógicos e strings, com exemplos de cada um.

O vídeo aborda a diferença entre valores inteiros e flutuantes, destacando a importância de representar corretamente os valores lógicos com maiúsculas. Além disso, explora a sintaxe moderna para imprimir na tela em Python. Explicação sobre a representação de valores inteiros e flutuantes, enfatizando a importância da correta diferenciação. Destaque para a importância de representar valores lógicos com letras maiúsculas e a sintaxe moderna para imprimir na tela em Python.

O vídeo explica como instalar o PyCharm e configurar o ambiente para aulas anteriores. Demonstrando a execução de comandos e a soma de valores de forma interativa. Demonstração da instalação do PyCharm e configuração do ambiente para aulas anteriores. Execução interativa de comandos e demonstração da soma de valores de forma prática. Explicação sobre a especificação do tipo primitivo de variáveis e a ordem de execução de comandos.

O vídeo aborda a utilização de formatos de strings em Python, destacando a sintaxe nova e antiga, mostrando a conversão de tipos primitivos e exemplificando a verificação de valores alfanuméricos. Demonstração da sintaxe nova e antiga de strings em Python, com foco na utilização de vírgulas e formatação de valores. Explicação sobre a conversão de tipos primitivos, mostrando como valores numéricos e strings são tratados em Python. Exemplificação da verificação de valores alfanuméricos, mostrando como identificar se um valor é alfabético, numérico ou alfanumérico.

O vídeo aborda a resolução de desafios de programação, incentivando a prática e a criatividade na resolução de exercícios utilizando tipos primitivos. Além disso, destaca a importância do apoio dos espectadores para manter a qualidade do conteúdo produzido. A importância da prática e criatividade na resolução de desafios de programação utilizando tipos primitivos. Incentivo para os espectadores apoiarem o canal para manter a qualidade do conteúdo produzido e ajudar toda a comunidade.
"""

# Neste exemplo, utilizamos dois inputs para receber um valor digitado pelo teclado. Os valores são guardados em variáveis para serem utilizados posteriormente
n1 = input('Digite um número: ')
n2 = input('Digite mais um número: ')

# Uma variável intermediária é criada e armazena o valor de uma operação.
s = n1 + n2

# Ao exibir o resultado, um erro semântico é apresentado. Ou seja, o programa executa a tarefa, porém o resultado não é o esperado O intuito da operação era somar dois valores numéricos, mas o resultado não é esse.
print(f'A soma vale {s}')

# Isso ocorreu, pois os dados recebido por um input, por padrão são do tipo string, mesmo que um número seja digitado. O operador +, quando utilizado em operações envolvendo dados do tipo string age como um concatenador, ou seja, ele une os caracteres. Mesmo que números sejam digitados, ele não age como seu irmão matemático.

# Para solucionar isso e utilizar os dados do input como números e poder realizar operações matemáticas, é necessário antes converter os tipos de dados. Em nosso exemplo, isso pode ser feito utilizando a função int() com o input como argumento. Assim os dados salvos nas variáveis serão do tipo inteiro (A conversão só ocorre se a string digitada for numérica)

# A versão atualizada do programa seria:
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print(f'A soma entre {n1} e {n2} é {n1 + n2}')

# Os quatro dados primitivos são int (números inteiros), float (números com parte decimal), bool (valores lógicos que representam verdadeiro/True ou falso/False, algo ou zero/vazio) e str (string, que são cadeias de caracteres entre aspas, podendo ser inclusive zero caracteres)

# f-strings são o método mais moderno para combinar strings e variáveis. Utilizamos um f antes da abertura das aspas para indicar uma f string e dentro da string, utilizamos chaves para posicionar as variáveis

# Quando não temos certeza do tipo de dado que estamos trabalhando, podemos utilizar a função type(). Em combinação com a função print, podemos visualizar o tipo de dado fornecido
print(type(n1))

# <class 'int'> é exibido

# Dados do tipo string possuem métodos de verificação
dado_str = input('Digite algo: ')
print(dado_str.upper())

# O método upper() converte todos os caracteres da string para maiúsculo. Existem outros métodos que podem ser utilizados, como lower() que converte para minúsculo, title() que converte para o formato de título (primeira letra de cada palavra em maiúscula) e capitalize() que converte a primeira letra da string para maiúscula.

# Podemos indicar o tipo de uma variável ao criá-la, utilizando a sintaxe var:tipo = valor. Isso é chamado de tipagem explícita. Em Python, a tipagem é dinâmica, ou seja, o tipo de dado é definido no momento em que a variável é criada. A tipagem explícita é utilizada para indicar o tipo de dado que a variável irá armazenar, porém, não é necessário, pois o Python é capaz de inferir o tipo de dado a partir do valor atribuído. Essa tipagem explícita não converte o valor atribuído, apenas indica o tipo de dado que a variável irá armazenar. Se o valor atribuído não for compatível com o tipo indicado, um erro será gerado.