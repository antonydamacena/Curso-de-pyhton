# ANOTAÇÕES SOBRE O CURSO!

## Dissecando variável:

### Para descobrir o tipo primitivo (str, bool, int, float) da variável, usamos:
`type()`

### Para dissecar a variável e saber se é número, letra, alfanumérico, se só contém espaços, etc., usamos `is` como por exemplo:
- `.isalpha()`: Verifica se todos os caracteres da string são letras do alfabeto.
- `.isnumeric()`: Verifica se todos os caracteres da string são numéricos.
- `.isalnum()`: Verifica se todos os caracteres da string são alfanuméricos (letras e números).
- `.isspace()`: Verifica se todos os caracteres da string são espaços em branco.
- `.isprintable()`: Verifica se todos os caracteres da string são imprimíveis.
- `.isdigit()`: Verifica se todos os caracteres da string são dígitos.
- `.isdecimal()`: Verifica se todos os caracteres da string são decimais.
- `.islower()`: Verifica se todos os caracteres da string estão em minúsculas.
- `.isupper()`: Verifica se todos os caracteres da string estão em maiúsculas.
- `.istitle()`: Verifica se a string está no formato de título (primeira letra de cada palavra em maiúscula).
- `.isidentifier()`: Verifica se a string é um identificador válido em Python.
- `.isascii()`: Verifica se todos os caracteres da string são ASCII.

Exempo:
`n= 45
print(f'a variável {n.isnumeric} é um numero?')`

## Operadores aritméticos:

- `+` : Adição
  - Exemplo: `a + b`
- `-` : Subtração
  - Exemplo: `a - b`
- `*` : Multiplicação
  - Exemplo: `a * b`
- `/` : Divisão
  - Exemplo: `a / b`
- `//` : Divisão inteira
  - Exemplo: `a // b`
- `%` : Módulo (resto da divisão)
  - Exemplo: `a % b`
- `**` : Exponenciação
  - Exemplo: `a ** b`

  ## Importando biblitecas 
  Para importarmos as bibliotecas usamos o comando `import`.

Como por exemplo:
`import math`

Nesse caso importaremos toda a biblioteca, porém se quisermos importar apenas uma função, neste caso usamos:
`from math import sqrt`

No caso mostrado acima estamos importando a função de raiz quadrada e se quisermos mais de uma, basta usar `,`.

Para mais informações sobre a biblioteca math [Clique aqui](https://docs.python.org/3/library/math.html) e para descobrir outras bibliotecas [Clique aqui](https://docs.python.org/3/library/index.html)

  ### Funções importantes da biblioteca math
- `raians` converte o anguo de grau em radiano
- `degrees` converte de radiano para graus
- `sin`descobre o seno de um radiano
- `cos`descobre o cosseno de um radiano
- `tan` descobre a tangente de um radiano
- `sqrt` descobre a raiz quadrada
- `ceil` arrendonda um numero para um valor maior mais proximo
- `floor`arrendonda um numero para um valor menor mais proximo
- `trunc`deixa apenas a parte inteira do numero
- `pow` ao invés de usar `**` para potencia pode usar essa função

> **Nota:**
> 
>Outra biblioteca bem comum seria a playsound para executar audio como um arquivo mp3. `playsond.playsoun('arquivo.mp3')`

