:octogonal_sign: Antes de continuar vamos fazer uma parada no caminho para ver <del>uma vaca :cow:</del> outro canto:

``` python
canto_da_vaca = """
Me diga você amigo
e responda com atenção
Qual é a mansa paciência
que povoa nossos campos
E na melancólica espera 
com abnegada paciência 
Nos dá alimento e abrigo
Fingindo indiferença
"""
```


Três aspas? É um erro de digitação? Não! Em Python podemos escrever textos com _várias linhas_ colocando-os entre três aspas duplas :sunglasses:. Embora isso funcione muito bem, tem um pequeno problema: quando queremos vê-lo no console, alguns `\n` bem peculiares aparecerão:

```python
ム canto_da_vaca
'\nMe diga você amigo\ne responda com atenção\nQual é a mansa paciência\nque povoa nossos campos\nE na melancólica espera \ncom abnegada paciência\nNos dá alimento e abrigo\nFingindo indiferença\n'
```


Este `\n`, chamado de _quebra de linha_, **representa** que ali, antes do próximo caractere, deve haver um enter `↵`. Perfeito, mas e se quisermos "escrever" o texto na tela, com enters verdadeiros ao invés desses `\n`? Vamos dar as boas-vindas ao procedimento `print`, que imprime os textos como queremos que eles fiquem:


```python
> print(canto_da_vaca)

Me diga você amigo
e responda com atenção
Qual é a mansa paciência
que povoa nossos campos
E na melancólica espera 
com abnegada paciência 
Nos dá alimento e abrigo
Fingindo indiferença

```

> E o que acontecerá se usarmos print com strings que não contenham quebras de linha? E se imprimirmos outros tipos de dados? Descubra tentando o seguinte e comparando os resultados:
>
> ```python
ム5
```
>
> ```python
ムprint(5)
```
>
> ```python
ム[1, 2, 3]
```
>
> ```python
ムprint([1, 2, 3])
```
>
> ```python
ム"à voz da aura"
```
>
> ```python
ムprint("à voz da aura")
```
