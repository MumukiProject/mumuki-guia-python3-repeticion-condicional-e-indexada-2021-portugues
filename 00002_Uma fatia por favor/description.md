Outras operações que listas e strings têm em comum são os _slices_, que podemos traduzir como segmentos, seções, ou (de maneira mais literal e engraçada) fatias :bread: slices, que permite obtermos os elementos entre dois limites:

``` python
ム numeros = [10, 20, 30, 40, 50]
ム numeros[0:2]
[10, 20] # é a lista composta pelo 1º e 2º elementos;
             # ⚠️ vamos lembrar que índices em Python contam a partir de 0
ム numeros[2:4]
[30, 40] # é a lista delimitada pelo 3º e 4º elementos
ム numeros[0:4]
[10, 20, 30, 40] # é a lista delimitada
             # pelos elementos 1 a 4
ム numeros[:4]
[10, 20, 30, 40] # equivalente ao exemplo anterior;
             # se não definimos o limite inferior,
             # traz todos os elementos desde o início
ム numeros[3:]
[40, 50] # é a lista delimitada
             # para todos os elementos do 4º
             # se não definirmos o limite superior,
             # traz todos os elementos para o final
```


> Vamos usar o que aprendemos para extrair segmentos das strings! Já alimentamos no console uma variável do tipo string chamada `primeira_estrofe`; Aplicando o que você viu, é a sua vez:
>
> 1. Descubra quantos caracteres tem a `primeira_estrofe` 
> 2. Obtenha uma string com os primeiros 22 caracteres da `primeira_estrofe`

> 3. Obtenha uma string com os últimos 25 caracteres de `primeira_estrofe`
