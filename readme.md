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