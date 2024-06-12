# Curso Python #04 - Primeiros comandos em Python3

"""
Agora chegou a hora de aprender os comandos básicos do Python e fazer os primeiros programas em Linguagem Python.

Nesta aula, vamos aprender a utilizar as instruções print() e input() para realizar interação com o usuário. Além disso, vamos ver o conceito fundamental de variável e como elas se comportam num programa em Python.

Teremos exercícios resolvidos em Python, com desafios de programação, onde você terá que criar programas em Python de acordo com enunciados propostos durante a aula.


Aprenda os primeiros comandos em Python3, como usar print, variáveis e input para interagir com o usuário. Crie scripts para executar tarefas básicas, como exibir mensagens e realizar cálculos simples.

Momentos-chave:
Aprender a interagir com o computador por comandos básicos de Python, como mostrar mensagens e realizar operações simples, é essencial para iniciantes em programação. Utilizar aspas para delimitar mensagens e não utilizá-las para números é uma prática fundamental. Explorando a importância dos operadores em Python e a necessidade de compreendê-los para avançar na programação. Destaque para a próxima aula sobre operadores e a base que estão sendo construídas. Explicando a utilização de aspas como delimitadores de mensagens em Python, seja com aspas simples ou duplas, e a distinção entre mensagens e números na linguagem de programação. Demonstrando a diferença na utilização de aspas para mensagens e a ausência delas para números, exemplificando a importância de compreender a distinção na programação.

Ao utilizar o operador de soma em Python, é importante notar que ele pode juntar mensagens em vez de somar números, sendo necessária atenção ao uso de aspas. O vídeo também aborda a configuração do ambiente Idle no Windows para facilitar a prática de programação. A importância de utilizar aspas ao trabalhar com mensagens e números no Python para evitar erros de interpretação. Configuração do ambiente Idle no Windows para facilitar a prática de programação, tornando mais acessível o uso do Python de forma interativa.

No Python, variáveis são objetos que podem receber valores, representados pelo sinal de igual. A interatividade com o usuário pode ser implementada utilizando a função input. A importância de compreender que variáveis no Python são objetos que podem armazenar valores específicos. Utilização do sinal de igual para atribuir valores às variáveis e a distinção entre igualdade e atribuição no Python. Implementação da interatividade com o usuário através da função input para coletar informações como nome, idade e peso.

O vídeo demonstra como criar scripts em Python no modo interativo e como salvar e executar scripts separados, mostrando a transição entre os modos. A importância de testar e programar no modo interativo e de criar scripts para execução posterior é destacada. A importância do modo interativo para testar e experimentar comandos em Python antes de criar scripts separados. Demonstração de como salvar e executar scripts separados no IDLE, permitindo a execução de comandos sem interação direta.

O vídeo apresenta desafios de programação em Python, incentivando os espectadores a praticarem e aprimorarem suas habilidades. Os desafios são progressivos e visam tornar a programação mais divertida e acessível. O primeiro desafio consiste em criar um script Python para exibir uma mensagem de boas-vindas personalizada. Os espectadores são encorajados a tentar resolver o desafio e compartilhar suas soluções. O segundo desafio envolve a formatação de uma mensagem com a data de nascimento de uma pessoa. Os espectadores são incentivados a praticar e a colaborar nos comentários. O terceiro desafio aborda a soma de dois números em Python, destacando a importância de aprender novas funções e buscar soluções. Os desafios são apresentados como etapas de aprendizado progressivo.

O instrutor destaca a importância do apoio dos espectadores para a continuidade e aprimoramento do curso de Python, enfatizando a qualidade e diferenciais do conteúdo oferecido. Ele ressalta a necessidade de suporte financeiro para manter a estrutura e a produção do curso. O curso de Python oferece diversas metas, desde aulas e desafios até soluções e cursos avançados, prometendo um conteúdo completo e diferenciado. O instrutor destaca a qualidade do curso, com didática, animações e gamificação, ressaltando a diferença em relação a outros tutoriais disponíveis gratuitamente. O apoio financeiro dos espectadores é essencial para manter a qualidade e a continuidade do curso, devido aos custos envolvidos na produção e estrutura do conteúdo.
"""

# Conjuntos de caracteres são delimitados por aspas simples ou duplas (depende do contexto).
# Todos os comandos em Python são funções. Funções utilizam parênteses para indicar os parâmetros para executar suas ações
print('Olá, Mundo!')

# Neste exemplo, print() é a função e 'Olá, Mundo' é o argumento da função, ou seja, a ação que a função deve realizar. O print exibe na tela o texto especificado.

# A sintaxe, portanto é: O nome da função, parêntese de abertura, abertura de aspa (simples ou dupla), caracteres desejados para formar a palavra, frase e etc, podendo também ser nenhum caractere, aspa de fechamento que sinaliza o fim da cadeia de caracteres e o parêntese de fechamento, que conclui a função

# Se omitirmos um dos parêntes, uma das aspas ou ambas e etc, o Python retorna um erro de sintaxe, ou seja, é um erro por ferir uma regra para construção das sentenças. "SyntaxError: invalid syntax"

print(7 + 4)  # Obtemos o resultado 11
print('7' + '4')  # Obtemos o resultado '74'

# Dados numéricos (sem aspas) são diferentes de caracteres numéricos entre aspas. Por exemplo, 7 + 4 é diferente de '7' + '4'
# Com isso concluímos que o operador + quando utilizado com conjuntos de caracteres delimitados por aspas tem a função de unir os dados
# Quando o operador + é utilizado com dados numéricos ele funciona como o operador matemático de soma

# O operador + não funciona com dados de tipos diferentes.
# print('Olá' + 5) retornaria um erro TypeError, que indica que estamos utilizando um dado de um tipo não válido para executar determinada ação. Neste caso estamos somando uma palavra com um número.

# Dados diferentes podem ser unidos utilizando a vírgula como separador
print('Olá', 5)  # Obtemos 'Olá 5'

# Nota: Por questão de legibilidade utilizamos um espaço após a vírgula para separar os argumentos, mas ele não é realmente necessário e não interfere na exibição. O espaço exibido no resultado é causado pelo argumento opcional da função print sep que por padrão é um espaço. Argumentos opcionais ficam ocultos, pois possuem um valor padrão.

# Se quisermos reutilizar algum dado em nosso programa, devemos guardar este valor em uma variável. Toda variável é um objeto!
# Nossas variáveis devem receber um nome. Por questões de boas práticas, existem regras para nomear variáveis, como utilizar letras minúsculas, dar nomes autoexplicativos e etc

# Uma variável passa a existir a partir do momento que é criada e tem um valor atribuído. A sintaxe da criação de uma variável é nome da variável, um operador de atribuição = e o valor desejado.

nome = 'Guanabara'
idade = 25
peso = 75.8

# O sinal de igual pode ser lido como "recebe" para deixar sua função intuitiva.

# Podemos mostrar o valor guardado em uma variável, chamando seu nome.
print(nome, idade, peso)  # Obtemos Guanabara 25 75.8

# Nota: Neste exemplo temos três valores de tipos diferentes, portanto não podemos utilizar o operador +

# Variáveis, como o nome sugere, são entidades dinâmicas. Isso significa que podemos atualizar seus valores. Uma das formas de fazer isso é adicionando interatividade com o usuário, combinando a criação da variável com uma função especial chamada input que significa ler um valor

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
peso = input('Digite o seu peso: ')

# A função input possui um argumento chamado mensagem de prompt, que é a mensagem que será exibida para o usuário. Ao executar o programa, o usuário irá digitar no teclado o valor que deseja atribuir para aquela variável.

# Após isso podemos manipular este valor da forma que desejarmos.
print(f'Olá, {nome}. Você tem {idade} anos e pesa {peso}Kg.')

# Desafio 01 - Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas conforme o valor digitado.
nome = input('Digite o seu nome para visualizar a mensagem: ')
print(f'Olá, {nome}! Seja bem-vindo.')

# Desafio 02 - Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.
dia = input('Digite o dia do seu nascimento: ')
mês = input('Digite o mês do seu nascimento: ')
ano = input('Digite o ano do seu nascimento: ')
print(f'Sua data de nascimento é: {dia}/{mês}/{ano}')

# Desafio 03 - Crie um script Python que leia dois números e tente mostrar a soma entre eles.
primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
print(f'Vamos somar! {primeiro} + {segundo} = {primeiro + segundo}')

# O valor padrão retornado pela função input, independente de ser digitado um caractere alfabético ou numérico será um dado do tipo string (str). Para receber o valor do input e conseguir somar e não concatenar, devemos converter o caractere para o tipo inteiro (int) se possível (Caso seja digitado um caractere alfabético um erro será exibido). A função int() é a responsável pela conversão