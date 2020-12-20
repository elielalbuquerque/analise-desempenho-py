# Analise-desempenho-py
O trabalho faz parte do programa de pós-graduação em Ciência da Computação da Unisinos. Aqui você pode encontrar a implementação de um Sistema Especialista (SE), utilizando de algoritmos que façam pesquisa de string difusa, combinação de strings difusas é a técnica de encontrar strings que correspondam aproximadamente a um padrão (em vez de exatamente). Em outra palavra, a correspondência de string difusa é um tipo de pesquisa que encontrará correspondências mesmo quando os usuários digitarem palavras incorretamente ou inserirem apenas palavras parciais para a pesquisa. Também é conhecido como correspondência aproximada de strings. Com isto em mente, desenvolve-se no presente trabalho uma proposta de SE a fim de auxiliar o perfil turístico utilizando como ferramentas de desenvolvimento PyCharm Community Edition 2020.02, ambiente de desenvolvimento integrado usado em programação de computadores, especificamente para a linguagem Python. Aqui você encontrara uma abordagens de resolução do problema usando algoritmo de Levenshtein frequentemente utilizado para calcular a distância entre duas strings.

## Indice
- Pré-requisitos
- Instruções ao usuário
- Cenário
- Analise de desempenho
  - Definição das métricas de desempenho
  - Carga para teste de algoritmo 
  - Performance de métricas
  - Análise de algoritmo
  - Conclusões
- Autores

## Pré-requisitos
   - Python 3
   - Fuzzywuzzy
   - Python-Levenshtein
   - Numpy
   - Matplotlib

## Instruções ao usuário
A base de dados utilizada no projeto será em arquivo tipo JSON, um formato que armazena informações estruturadas e principalmente usado para transferir dados entre um servidor e um cliente. O arquivo e basicamente uma alternativa simples e mais leve ao XML (Extensive Markup Language), que tem funções similares. Desenvolvedores usam o JSON para trabalhar com AJAX (Asynchronous JavaScript and XML). Criamos um objeto Python para efetuar a validação dos dados consultados do usuário na interface HTML, para isso devemos utilizar a base em JSON e utilizar a biblioteca Fuzzywuzzy. A distância de Levenshtein é uma métrica para medir a distância entre duas sequencias de palavras. Em outras palavras, ele mede o número mínimo de edições que você precisa fazer para alterar uma sequência de uma palavra na outra. Essas edições podem ser inserções, exclusões ou substituições.  A principal característica do Pycharm e a separação do código e layout HTML. Possuı um webserver embutido (que pode ser integrado ao Apache de diversas formas) e é altamente integrável com outros módulos Python (até mesmo o flask). Ele funciona da seguinte maneira: ao invés de http://localhost/sub/index ser o arquivo index dentro do subdiretório sub; index() e uma função dentro da classe **App.py**. Para regenerar testes e novas análises, execute o arquivo validação.py. E para regenerar os gráficos, basta executar **gráficos.py**. É possível implementar a formula de Levensntein do zero usando uma função Python, posterior para usar basta chamar a função passando os parâmetros, exemplo: [Levensnteins.py] (https://github.com/elielalbuquerque/analise-desempenho-py/blob/main/Levensntein.py)

## Cenario
Com base numa string de dados informada pelo usuario numa aplicação Python, desejamos comparar a similaridade com informações armazenadas em uma base e trazer a informações que melhor representa com maior nível de acurácia.
  - Importar biblioteca FuzzyWuzzy, uma função de razão que calcula a razão de similaridade de distância de Levenshtein padrão entre duas sequências.

### Objetivo
Comparar o desempenho de uma implementação do algoritmo de Levenshtein com uma biblioteca Fuzzywuzzy para resolver o problema de comparação de similaridade de duas strings com maior nível de assertividade.
  
# Analise de desempenho
Nesta seção iremos avaliar o desempenho de nossas propostas de algoritmos para resolver o SE codificado aqui. 
Basicamente discutiremos sobre desempenho na comparação de strings propostas ao SE.

Mediremos o número mínimo de edições que você precisa fazer para alterar uma sequência de uma string na outra. A técnica utilizada para avaliação será a de simulação usando como critério a precisão para comparação.
Também é possível calcular a razão de similaridade com base na distância de Levenshtein. Isso pode ser feito usando a seguinte fórmula:
     
     (|a|+|b|)−leva,b(i,j)/|a|+|b)
     
Onde | a | e | b | são os comprimentos da sequência uma e sequência b respectivamente.

## Definição das métricas de desempenho
1. Quantidade de edições por inserções, exclusões ou substituições.
2. Percentual de acurácia.

### Carga para teste de algoritmo
- Testaremos cargas de trabalho para busca de palavras numa base de 29.870 palavras do dicionario Aurelio. 
As palavras pesquisadas usados como base estarão armazenados no formato json conforme arquivo [Lista-de-Palavras.json](Lista de Palavras)

### Performance de metricas
- Acuracia/Similaridade
- Distancia de Levensnteins

### Analise dos algoritmos
|

### Conclusões
Neste documento foi exemplificado como a correspondência por aproximada de strings e determinar o quão semelhante são. Os exemplos apresentados aqui podem ser simples, mas são suficientes para ilustrar como lidar com vários casos do que um computador pensa serem strings incompatíveis através da correspondência de string difusa para mapear correspondentes a pesquisa de um sistema de turismo para recomendação. No entanto, a utilidade desta técnica pode ser expandida, não há limites para usos da correspondência difusa. Este trabalho tem como objetivo demostrar os resultados de performance e acurácia comparando dois algoritmos distintos com o mesmo objetivo de comparar a similaridade entre palavras informadas com uma base de dados existentes.
