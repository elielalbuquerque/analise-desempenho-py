# Analise-desempenho-py
O trabalho faz parte do programa de pós-graduação em Ciência da Computação da Unisinos. Aqui você pode encontrar a implementação de um Sistema Especialista (SE), utilizando de algoritmos que façam pesquisa de string difusa, combinação de strings difusas é a técnica de encontrar strings que correspondam aproximadamente a um padrão (em vez de exatamente). Em outra palavra, a correspondência de string difusa é um tipo de pesquisa que encontrará correspondências mesmo quando os usuários digitarem palavras incorretamente ou inserirem apenas palavras parciais para a pesquisa. Também é conhecido como correspondência aproximada de strings. Com isto em mente, desenvolve-se no presente trabalho uma proposta de SE a fim de auxiliar o perfil turístico utilizando como ferramentas de desenvolvimento PyCharm Community Edition 2020.02, ambiente de desenvolvimento integrado usado em programação de computadores, especificamente para a linguagem Python. Aqui você encontrara uma abordagens de resolução do problema usando algotimo de Levenshtein frequentemente utilizado para calcular a distância entre duas strings.

## Indice
- Pré-requisitos
- Instruções ao usuario
- Cenario
- Analise de desempenho
  - Definição das métricas de desempenho
  - Carga para teste de algoritmo 
  - Performance de metricas
  - Análise de algoritmo
  - Conclusões
- Autores

## Pré-requisitos
   - Python 3
   - Fuzzywuzzy
   - Python-Levenshtein
   - Numpy
   - Matplotlib

## Instruções ao usuario
A base de dados utilizada no projeto será em arquivo tipo JSON, um formato que armazena informações estruturadas e principalmente usado para transferir dados entre um servidor e um cliente. O arquivo e basicamente uma alternativa simples e mais leve ao XML (Extensive Markup Language), que tem funções similares. Desenvolvedores usam o JSON para trabalhar com AJAX (Asynchronous JavaScript and XML). Criamos um objeto Python para efetuar a validação dos dados consultados do usuário na interface HTML, para isso devemos utilizar a base em JSON e utilizar a biblioteca Fuzzywuzzy. A distância de Levenshtein é uma métrica para medir a distância entre duas sequencias de palavras. Em outras palavras, ele mede o número mínimo de edições que você precisa fazer para alterar uma sequência de uma palavra na outra. Essas edições podem ser inserções, exclusões ou substituições.  A principal característica do Pycharm e a separação do código e layout HTML. Possuı um webserver embutido (que pode ser integrado ao Apache de diversas formas) e é altamente integrável com outros módulos Python (até mesmo o flask). Ele funciona da seguinte maneira: ao invés de http://localhost/sub/index ser o arquivo index dentro do subdiretório sub; index() e uma função dentro da classe **App.py**. Para regenerar testes e novas análises, execute o arquivo validação.py. E para regenerar os gráficos, basta executar **gráficos.py**. É possivel implementar a formula de Levensntein do zero usando uma função Python, posterior para usar basta chamar a função passando os parametros, exemplo: [Levensnteins.py] (https://github.com/elielalbuquerque/analise-desempenho-py/blob/main/Levensntein.py)

## Cenario
Com base numa string de dados informada pelo usuario numa aplicação Python, desejamos comparar a similaridade com informações armazenadas em uma base e trazer a informaões que melhor representa com maior nivel de acurácia.
  - Opção 1: Implementar algoritmo de Levenshtein na linguagem Puthon que frequentemente é utilizado para calcular a distância entre duas strings determinando a similaridade enter as palavras.
  - Opção 2: Importar biblioteca FuzzyWuzzy, assim como o pacote Levenshtein, uma função de razão que calcula a razão de similaridade de distância de Levenshtein padrão entre duas sequências.

### Objetivo
Comparar o desempenho de uma implementação do algoritmo de Levenshtein com uma biblioteca Fuzzywuzzy para resolver o problema de comparação de similaridade de duas string com maior nivel de acertividade.
  
# Analise de desempenho
Nesta seção iremos avaliar o desempenho de nossas propostas de algoritmos para resolver o o SE codificado aqui. Basicamente discutiremos sobre desempenho na comparação de strings propostas ao SE.

Mediremos o número mínimo de edições que você precisa fazer para alterar uma sequência de uma string na outra. A tecnica utilizada para avaliação será a de simulação usando como criterio a precisão para comparação.
Também é possível calcular a razão de similaridade com base na distância de Levenshtein. Isso pode ser feito usando a seguinte fórmula:
     
     (|a|+|b|)−leva,b(i,j)/|a|+|b)
     
Onde | a | e | b | são os comprimentos da sequência uma e sequência b respectivamente.

## Definição das métricas de desempenho
1. Quantidade de edições por inserções, exclusões ou substituições.
2. Percentual de acuracia.

### Carga para teste de algoritmo
- Testaremos cargas de trabalho com string de 5, 10, 20 caracteres para busca numa base de 100 palavras. 
Os arquivos usados no arquivo estarão armazenados no formato json conforme arquivo [base_dados.json] (Base de dados)

### Performance de metricas
- Testaremos uma acuracia minima de 95%
- Análise dos dados

### Analise do algoritmos


### Conclusões
Neste documento foi exeplificado como a correspondência por aproximada de strings e determinar o quão semelhantes são. Os exemplos apresentados aqui podem ser simples, mas são suficientes para ilustrar como lidar com vários casos do que um computador pensa serem strings incompatíveis atraves da correspondência de string difusa para mapear correspondentes a pesquisa de um sistema de turismo para recomendação. No entanto, a utilidade desta técnica pode ser expandida, não há limites para usos da correspondência difusa. Este trabalho tem como objetivo demostrar os resultados de performance e acuracia comparando dois algoritmos distintos com o mesmo objetivo de comparar a semilaridade entre palavras informadas com uma base de dados existentes.
