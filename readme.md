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

## Manipulação de texto:

### Fatiamento:

 para fatiarmos uma frase vamos usar de exemplo a frase "Curso em Video"  tem 12 letras e 2 espaços, ele irá ocupar 14 espaços na memoria, para selcionarmos uma palavra especifica usamos os '[]' Exemplo:

 ` frase= 'Curso em Video'
 print (frase[9])`
 
 A onde nos retornará a letra 'v'. pois se contarmos de 0 à 9 com os espaços a letra 'v' ocupará o 9° espaço. 
 
 E se usamos o comando:
 `print(frase[:6]) ` nos retornará a frase curso pois os primeiros ':' representam o inicio e os segundos o final.
 > **Lembrando que:**
 > 
 > O python nunca conta o ultimo número Ex:
 >
 >| Letra  | C | U | R | S | O |
> |--------|---|---|---|---|---|
> | Contagem | 1| 2 | 3 | 4 | 5 |
 >
 >Se você digita até o numero 5 ele irá printar apenas "curs" pois o utimo numero sempre tem que ser +1.
 
 E voce também pode usar `::2` Neste exemplo vc mostra que ele começará do inicio, terminará no final e sera fatiado de 2 em 2 resutando em `croe ie yhn`

 ### Analise de texto e manipulação:

- `print(len(frase))` - Conta quantas letras a variável `frase` tem.

- `print(frase.count('a'))` - Conta quantas vezes a letra 'a' aparece na variável `frase`.

- `print(frase.find('Curso'))` - Encontra a posição da primeira ocorrência da substring 'Curso' na variável `frase`.

- `print(frase.replace('Python', 'Android'))` - Substitui todas as ocorrências da substring 'Python' por 'Android' na variável `frase`.

- `print(frase.upper())` - Converte todos os caracteres da variável `frase` para maiúsculas.
- `print(frase.lower())` - Converte todos os caracteres da variável `frase` para minúsculas.
- `print(frase.strip())` - Remove espaços em branco no início e no final da variável `frase`.
- `print(frase.rstrip())` - Remove todos os espaços em branco da direita da variável `frase`.
- `print(frase.lstrip())`- Remove todos os espaços em branco da esquerda da variável `frase`.
- `print(frase.split())` - Divide a variável `frase` em uma lista de substrings com base em espaços em branco.
- `print(' '.join(lista))` - Junta uma lista de substrings `lista` em uma única string, usando um espaço como delimitador.
- `print('curso' in frase)` - Diz se a palavra/letra existe na variavel frase.
- `print(frase.capitalize())` -  deixa a frase no formato capitalizado (a inicial da maiúscula)

>**OBS:**
>Uma substring é uma sequência de caracteres que aparece dentro de outra string. Por exemplo, na string "programação", as substrings podem ser "pro", "grama", "ação", etc.

## Condições:

Para as codições usamos if (se) e else (senão) como por exemplo :

```
N= input('Qual foi sua nota?')

if n >= 6:
print('PARABÉN!')

else:
print('ESTUDE MAIS!') 

```
Neste Exemplo de sua nota for igual ou superior a 6 ele irá te parabenizar e se for abaixo de 6 irá te mandar estudar.

porem nesses casos mais simpes não é nessesario usar tantas linhas ou a função 'else' veja um exeplo:

```
N= input('Qual foi sua nota?')

print('Parabens' if N >=6, else 'Estude mais')
         
                       OU
print('parabens' if N >=6)      
print('Estude mais')          
```
Em ambos os casos ele irá mostrar  parabens de sua nota for igual ou superior a 6 e ira mostrar estude mais se for inferior a 6.


