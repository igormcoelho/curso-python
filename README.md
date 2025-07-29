## Curso de Lógica de Programação e Python

Materiais gerais de Lógica de Programação e Python do [Prof. Igor Machado Coelho](https://igormcoelho.github.io), bem como suas respectivas aplicações em períodos recentes.

![last-commit](https://img.shields.io/github/last-commit/igormcoelho/curso-python)

Lista completa de módulos no repositório:

- A definir

### Objetivos e Metodologia do Curso:

1. O curso se destina ao ensino de aspectos fundamentais da programação de computadores e do pensamento computacional, utilizando para práticas a linguagem Python.
2. O curso tem um ensino incremental, no qual o aluno começa sem saber nada, nem dos conceitos e nem da sintaxe do Python,
e vai evoluindo gradualmente, conceito a conceito.
3. O curso é dividido em três avaliações, sendo que **até a primeira avaliação**, **não é aconselhado o uso de assistentes de programação**, pois eles tendem a utilizar conceitos mais avançados de programação
   - A partir da primeira avaliação, **já será permitido e aconselhado** o uso de assistentes de programação, pois o aluno já terá condições de acompanhar algumas boas sugestões desse tipo de plataforma de apoio
4. Todos os conceitos apresentados, dos mais simples aos mais complexos, exigirão domínio completo por parte dos alunos; ou seja, o aluno **só poderá utilizar aquilo que de fato ele sabe construir** a partir dos fundamentos da linguagem de programação
5. Importante: o curso não pode ter saltos longos! Cada conceito precisa ser exposto claramente, em seu tempo, e o aluno precisa se certificar que entendeu bem antes de avançar para o próximo. Praticar com exercícios é a melhor maneira.
Tipicamente em programação, ou você sabe a direção, ou você congela e não faz absolutamente nada! Isso é normal.
Do "nada" para "tudo", a distância não é tão longa quanto parece :)
6. Aulas Teóricas não podem ser dadas em laboratório, pois os alunos não prestam atenção... é um conteúdo perdido! Aulas em laboratório precisam ser exclusivamente práticas, todo o tempo. Problema x Solução, o tempo todo.

### Cronograma do Curso (por semana / conceitos básicos da linguagem):

Observações Importantes:

- Esse material é organizado para um curso de 60h semestrais, ou seja, aproximadamente 15 semanas.
- É esperado um tempo hábil para 12 semanas de conteúdos, além das avaliações (provas, reposições, provas finais, etc), sendo assim, o curso proposto é bastante enxuto, mas completo! 
   * foi cortado MUITO material para caber nesse curto espaço de tempo com alguma folga!!!
- Caso sintam que é necessário reforçar algum conteúdo, é possível que caiba no tempo das 60h, por isso é RECOMENDADO somente ir dos módulos 1 ao 10, sendo o 11 e 12 tópicos extras.
- Agradecimentos ao Prof. Yuri Frota, cujos materiais complementam diversos tópicos desse curso. No futuro, todos materiais do prof Yuri serão devidamente adaptados para as particularidades da lógica desse curso, restando apenas esse agradecimento.

I. Parte 1 - Pensamento computacional e sintaxe básica do Python (evitar assistentes de programação!)
   -  Objetivo: lógica de programação básica com Python

   1. Introdução: Lógica de Programação e a Linguagem Python
      - História Algoritmos e Compilador/Interpretador/IDE
      - **Conceitos novos:** *interpretador*, *entrada e saída*, *saída padrão*, *built-in `print()`*
      - **Conceitos novos:** *variável*, *constante*, *tipos de variáveis*, *tipos básicos `int`, `float`, `bool`, `str`*, *operador =*, *atribuição múltipla*, *built-ins de conversão de tipos*, *operadores +, -, \*, /, //, \*\* e %*, *`type()`*, *interpolação com fstring*, *built-in `id()`*, *entrada padrão*, *built-in `input()`*
      - Slides:
          * Aula Teórica 1: [Slides Yuri - Introdução](./slides_yuri/01-Introducao.pdf)
          * Final Aula Teórica 1 - Exercício para Casa: Instalar IDE Python ([Breve Introdução IDE Python (2025)](https://docs.google.com/presentation/d/1Qpy__44wEB0ISV-P02z7KBqkC94hk6nNnGcuhLBJnVA/edit?usp=sharing))
          * Aula Prática 1: [Slides Yuri - Organização](./slides_yuri/01P-Organizacao.pdf)
   2. Decisão
      - **Conceitos novos:** *indentação*, *`if`*, *operadores ==, `and`, `or`, `not`, >, <, >=, <=*, *`else`*, *`elif`*
      - Slides:
          * Aula Teórica 2: [Slides Yuri - Decisão](./slides_yuri/02-Decisao.pdf)
          * Aula Prática 2: [Slides Yuri - LAB Decisão](./slides_yuri/02P-LAB-Decisao.pdf)
   3. Repetição Condicional (pular Repetição Contável)
      - **Conceitos novos:** *`while`*, *escopo de variáveis*, *indentação (reforço)*, *operadores +=, -=, \*=, /=*
      - Slides:
          * Aula Teórica 3: [Slides Yuri - Repetição Condicional](./slides_yuri/03-Repeticao-Condicional.pdf)
          * Aula Prática 3: [Slides Yuri - LAB Repetição Condicional](./slides_yuri/03P-Repeticao-Condicional.pdf)
   4. Laços Aninhados
      - **Conceitos novos:** *`break`*, *`continue`*, *`pass`*, *escopo de variáveis (reforço)*, *indentação (reforço)*, *expressão condicional? (x=if-else)*
      - Slides:
          * Aula Teórica 4: Slides - Laços Aninhados (A FAZER!) - Não usar for!
          * Aula Prática 4: [Slides Yuri - LAB Laços Aninhados](./slides_yuri/04P-LAB-Lacos-Aninhados.pdf)

   - Revisão de Conteúdo
   - Listas de Exercícios
      * [Lista 01 Decisão Yuri](./listas-exercicios/Lista-01-Decisao-Yuri.pdf)
      * [Lista 02 Repetição Yuri](./listas-exercicios/Lista-02-Repeticao-Yuri.pdf)
   - Extra: aula prática de jogo da velha - [Yuri Completar Programação Python](http://profs.ic.uff.br/~yuri/python/velha.py) 
   - Primeira avaliação escrita: sem consulta e sem utilizar recursos de linguagem mais avançados (como listas e for-range/repetições contáveis)!

II. Vetores, Rotinas e Tipos Agregados (apoio parcial de assistentes de programação)
   -  Objetivo: vetores como listas, tipos compostos e funções

   5. Vetores, Listas, Ranges
      - **Conceitos novos:** *built-in `list()`*, *built-in `range()`*, *`for`*, *`in`*, *tipo de valor vs tipo de referência*,  *operador +*, *operador \**, *built-in `len()`*, *built-in `del`*, *slices*
      - Slides:
          * Aula Teórica 5: [Slides Yuri - Vetores](./slides_yuri/05-Vetores.pdf)
          * Aula Prática 5: [Slides Yuri - LAB Vetores](./slides_yuri/05P-Vetores.pdf)
          * Extra: adicionar material sobre *for* e remover menções a Dicionários (não faz parte do conteúdo!)
   6. Rotinas (Modularização I)
      - **Conceitos novos:** *`def`*, *rotinas*, *funções*, *procedimentos*, *`return`*, *parâmetros*, *argumentos*, *passagem por valor vs passagem por referência*, *pilha de execução*, *escopo de variáveis (reforço)*, *`global`*,  *argumentos posicionais vs nomeados*, *operador ponto (.) para acesso de funções built-ins* 
      - Exemplo de métodos do list, como `.split()`, `.append()`, `.sort()`, etc
      - Exemplo de métodos de strings, como `.split()`
      - Exemplo de métodos de Python, como `sqrt()`, `max()`, etc (porém, evitar *import* ainda!)
      - Não ensinar tipos agregados/heterogêneos ainda!
      - Slides:
          * Aula Teórica: [Cap. 7 - Rotinas (Modularização I)](https://docs.google.com/presentation/d/1ts0dM3DUxT94nJlX2B9zFgdOac_riwScsFPh89lsd40/edit?usp=sharing)
   7. Funções Recursivas e de Ordem Superior (Modularização II)
      - **Conceitos novos:** *rotinas (reforço)*, *pilha de execução (reforço)*, *estouro de pilha / stack overflow*, *recursão de cauda*, *caso base vs caso recursivo*
      - Exemplo com fibonacci e torres de hanoi (Desafio!)
      - Exemplo de Busca, inclusive, Busca Ordenada
      - Exemplo clássico: `x = list(map(int, s.split()))`
      - Slides:
          * Aula Teórica: [Cap. 8 - Funções Recursivas e de Ordem Superior](https://docs.google.com/presentation/d/1iFrVHO-atR6QjiWhnkxgnvjHOqY6v7KsRo-T2L1-quw/edit?usp=sharing)
   8. Ordenação e Agregados Heterogêneos (Modularização III)
         - **Conceitos novos:** *rotinas (reforço)*, *pilha de execução (reforço)*, *`class`*, *métodos dunder*, *`__init__`*, *`__str__`*
      - Slides:
          * A fazer!
          * Basear em [Slides UFF Concurso](./slides/Ordenacao-Bubble-Insertion-Shell-Comb.pdf)
          * Adicionar parte de agregados heterogêneos no início da aula!

   - Revisão de Conteúdo
   - Listas de Exercícios
      * [Lista 03 Vetores Yuri](./listas-exercicios/Lista-03-Vetores-Yuri.pdf)
      * [Lista 04 Rotinas Igor](./listas-exercicios/Lista-04-Rotinas-Igor.pdf)
      * Lista 05 - Ordenação e Agregados Heterogêneos (a fazer!)
   - Segunda avaliação escrita: sem consulta e sem utilizar recursos de linguagem mais avançados (como imports)!

III. Parte 3 (apoio total de assistentes de programação)

   9. Matrizes, *List Comprehension* e Pacotes/Importação (Modularização IV)
      - **Conceitos novos:** *rotinas (reforço)*, *pilha de execução (reforço)*, `import`
      - Slides:
          * Aula Teórica 10: [Slides Yuri - Matrizes](./slides_yuri/09-Matrizes.pdf)
          * Aula Prática 10: [Slides Yuri - LAB Matrizes](./slides_yuri/09P-Matrizes.pdf)
          * A fazer: slides de list comprehension e de importação de pacotes

   10. Escrita/Leitura de Arquivos Texto
      - Slides:
          * Aula Teórica 10: [Slides Yuri - Arquivos](./slides_yuri/10-Arquivos.pdf)
          * Aula Prática 10: [Slides Yuri - LAB Arquivos](./slides_yuri/10P-LAB-Arquivos.pdf)
          * A fazer: aumentar conteúdo nessa parte! Ideia: tratamento de exceções? É comum em arquivos...
          
   - Revisão de Conteúdo
   - Última avaliação ou Trabalho
        * Caso não tenha outra prova, juntar com partes anteriores!
            - Ideia: juntar Vetores com a Parte I e Matrizes e Arquivos com a Parte II.
        * Caso queira aumentar a Parte III, o tópico de Ordenação e Agregados Heterogêneos pode vir da Parte II.

IV. Parte 4 - Programação avançada em Python (Extra!)
   - Não é esperado que haja tempo hábil para ensinar isso em um curso regular de 60h semestrais
       * Mas fica como bônus para os alunos mais curiosos!

   11. Corrotinas, Geradores e Iteradores
      - **Conceitos novos:** *rotinas (reforço)*, *pilha de execução (reforço)*, `yield`, `next()`, ...
      - Slides:
         * A fazer!

   12. Dicionários
      - **Conceitos novos:** *rotinas (reforço)*, *pilha de execução (reforço)*, `dict`, ...
      - Slides:
         * A fazer!
         
V. Trabalho

   - O trabalho será feito em trio, onde cada aluno terá um papel de desenvolver uma parte do programa colaborativamente.
   - A entrega será individual por aluno com código e relatório (preencher um google forms), mas como parte de um grupo o código deverá ter as três partes funcionando colaborativamente.
   - É permitido o uso de assistentes de programação e os prompts utilizados deverão ser entregues juntamente com o relatório da atividade
   - Deverão ser anotados desafios durante o desenvolvimento do trabalho, tópicos de maior dificuldade e estratégias para resolvê-los
   - Alunos deverão participar da entrega intermediária para receber nota no trabalho, e após a entrega intermediária, teremos aulas para sanar eventuais dúvidas.
   - Um membro do grupo deverá unificar todos os três códigos e apresentar um outro relatório final, esse em formato texto (word), descrevendo os desafios de desenvolver o trabalho completos com suas três partes juntas, e poderá anexar prompts de análises e críticas do assistente de programação à versão final do trabalho.
   - IMPORTANTE: Não há problema em utilizar assistente de programação, desde que os relatórios demonstrem tal uso. Caso o desenvolvimento do trabalho não esteja plenamente justificado no relatório (ou com evidências de plágio), o trabalho terá nota zerada.

============

Materiais PDF-HTML:

- A organizar aqui!

***Observação:*** **alguns módulos só são oferecidos para cursos específicos.*

-------

## Cursos recentes

- 2025-1 UFF TCC00308 - [README](./slides/curso-2025-1/README.md)

-------

## Sobre gravações

Gravações disponibilizadas no YouTube e Classroom foram feitas com OBS (obrigado pelas dicas Mateus Nazário). Algumas dicas:

- https://medium.com/@igormcoelho/dicas-para-obs-no-linux-para-google-meet-8ac102972183

Utilizei o Okular para marcação do PDF (obrigado Matheus Nohra Haddad pelas dicas).

## Como esses slides foram feitos?

Estes slides foram feitos em `markdown` e `pandoc` (super fácil!) de acordo com o tutorial [ilectures-pandoc](https://github.com/igormcoelho/ilectures-pandoc).

Basicamente, é necessário instalar o pandoc e, opcionalmente, copiar alguns filtros úteis do tutorial (dois arquivos python). Então, é possível gerar, a partir do `markdown`, uma versão PDF LaTeX+Beamer, e outra web utilizando RevealJS. O tutorial explica tudo em detalhes.

O mais legal é que a edição do slide tem uma visualização em tempo real, com plugins disponíveis para editores populares como Atom e VSCode.
Uma demonstração foi colocada no site do ilectures: [https://github.com/igormcoelho/ilectures-pandoc#demonstrations](https://github.com/igormcoelho/ilectures-pandoc#demonstrations).


### Deps

Pandoc + LaTeX

`python3 -m pip install pandoc-source-exec`
`python3 -m pip install pandoc-latex-color`

[pandoc 2.10.1](https://github.com/jgm/pandoc/releases/tag/2.10.1)



### Licença CC-BY 4.0

Você pode: (Share) copiar e redistribuir esse material em qualquer formato; (Adapt) adaptar esse material, mesmo que para uso comercial.

Você deve: (Attribution) dar crédito apropriado, bem como um link para o original e a indicação das mudanças que você fez.

Veja licença original [CreativeCommons CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)

```
curso-estruturas-de-dados-i (c) by Igor M. Coelho

curso-estruturas-de-dados-i is licensed under a
Creative Commons Attribution 4.0 International License.

You should have received a copy of the license along with this
work. If not, see <http://creativecommons.org/licenses/by/4.0/>.
```


Copyleft 2020
