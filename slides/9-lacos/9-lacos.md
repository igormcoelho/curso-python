---
author: Igor Machado Coelho
title: Programação I
subtitle: Repetição Condicional
date: 14/04/2025
transition: linear
fontsize: 10
header-includes:
- <link rel="stylesheet" type="text/css" href="general.css">
- <link rel="stylesheet" type="text/css" href="reveal-beamer.css">
pandoc-latex-fontsize:
  - classes: [cpp, listing]
    size: footnotesize
---


# Repetição Condicional

-----------

## Comando While

Executa o bloco de instruções enquanto a condição for verdadeira

::::::::::::: {.columns}

::::: {.column width=55%}

Portugol

```.cpp
enquanto CONDIÇÃO
faça
   INSTRUÇÃO 1;
   INSTRUÇÃO 2;
   ...
   INSTRUÇÃO N;
...
```

:::::

. . .

::::: {.column width=45%}

Python

```.py
while CONDIÇÃO:
   INSTRUÇÃO 1;
   INSTRUÇÃO 2;
   ...
   INSTRUÇÃO N;
...
```

:::::

:::::::::::::

. . . 

- A condição é uma expressão booleana que pode fazer uso de
quaisquer operadores
- O bloco de instruções é delimitado por indentação
- Deve haver algum processo dentro do bloco de comandos que
torne a condição falsa para que a repetição seja encerrada
- **Pergunta:** Qual fluxograma representa esses códigos?

-------

## Exemplos com While 


```.py
numero = 1
while numero <= 100:
   print(numero)
   numero = numero + 1
```

. . .

```.py
n = int(input("Digite um número:"))
numero = 1
while numero <= n:
   print(numero)
   numero = numero + 1
```

. . .

```.py
a = 5
while a == a:
   a =  a + 1
print(a)     
``` 
 

-------

## Mais exemplos com While

::::::::::::: {.columns}

::::: {.column width=55%}

```.py
num = 100
pares = 0
while num <= 200:
   if num % 2 == 0
       pares = pares + 1
   num = num + 1
print(pares)
```

:::::

. . .

::::: {.column width=45%}

```.py
num = 100
pares = 0
continua = True

while continua:
   if num % 2 == 0:
      pares = pares + 1
   num = num + 1
   if num > 200:
      continua = False
print(pares)
```

:::::

:::::::::::::


-------

## Padrão while(True) / break

Em algumas situações, é útil ter um laço infinito:

```.py
while True:
   # faça algo útil!
```

Mas como escapar desse laço infinito?

. . . 

```.py
num = 100
contador_pares = 0
while True:
   if num % 2 == 0:
      contador_pares = contador_pares + 1
   num = num + 1
   if num > 200:
      break
print(contador_pares)
```

-------

## Padrão while(True) / break / continue

Em algumas situações, é útil ter um laço infinito:

```.py
num = 99
contador_pares = 0
while True:
    num = num + 1
    if num > 200:
        break
    if num % 2 != 0:
        continue  # o que isso faz?
    contador_pares = contador_pares + 1
print(contador_pares)
```

**Pergunta:** Por que começamos com 99?


-------

## Padrão for-range em repetições contáveis

A repetição contável, ou laço tipo `for-range`, é muito utilizado em python.
Esse conceito será melhor explicado no futuro, porém apresentamos brevemente a estrutura de um for-range básico (simplemente, uma variavel e um intervalo de continuação/incremento):

::::::::::::: {.columns}

::::: {.column width=55%}

```.py
numero = 1
while numero <= 100:
   print(numero)
   numero = numero + 1
```

:::::

. . .

::::: {.column width=45%}

```.py
for numero in range(1, 101):
   print(numero)
```

:::::

:::::::::::::

A estrutura é bastante compacta e muito utilizada na prática!
Porém, ela mascara alguns comportamentos internos do python que serão melhor discutidos no futuro.

**Dica:** Busque utilizar e praticar o laço do tipo `while`, pois ele permite construir *qualquer tipo* de repetição, não apenas contáveis como `for`.

**Pergunta:** O que acontece com `break` e `continue` em um laço `for`? Pratique!

-------

## Laços Aninhados

Seguir com material do prof Yuri

-----

## Reprodução do material

Esses slides foram escritos utilizando pandoc, segundo o tutorial ilectures:

- https://igormcoelho.github.io/ilectures-pandoc/

Exceto expressamente mencionado (com as devidas ressalvas ao material cedido por colegas), a licença será Creative Commons.

**Licença:** CC-BY 4.0 2025

Igor Machado Coelho

-------

## This Slide Is Intentionally Blank (for goomit-mpx)
