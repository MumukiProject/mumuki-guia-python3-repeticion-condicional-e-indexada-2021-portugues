As coisas ficam ainda mais interessantes quando relembramos tudo o que já vimos. Por exemplo, esta função `somatório`...

```python
def somatorio(numeros):
  soma = 0
 
  for numero in numeros:
	soma += numero
    
  return soma
```

...calcula a soma de todos os elementos de uma lista de números...

```python
ム somatorio([10, 5, 20])
35 # porque é 10 + 5 + 20
ム somatorio([])
0 # porque o somatório de uma lista vazia é 0.

```

...ou inclusive de uma categoria de variação:

```python
ム somatorio(range(1, 6))
15 # porque é 1 + 2 + 3 + 4 + 5
```

> Vamos ver se está entendido: complete a definição da função `produtorio` que, como `somatorio`, utiliza uma sequência de números, mas em vez de somar todos, ela os multiplica:
>
> ```python
> produtorio([10, 2, 3])
> 60 # porque é 10 * 2 * 3
> produtorio([3, 3, 2, 4])
> 72 # porque é 3 * 3 * 2 * 4
> produtorio([8])
> 8 # porque o produtório de um número é esse mesmo número.
> produtorio([])
> 1 # porque o produtório de uma lista vazia é 1.
> ```
>
