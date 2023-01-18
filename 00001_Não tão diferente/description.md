Nas lições anteriores vimos várias funções (e alguns operadores!) que operam com números, outras com booleanos e assim por diante.

Mas você já deve ter notado que existem duas operações em particular que são bastante _peculiares_: `len` e `in`. Por quê? Vamos ver os seguintes exemplos:


``` python
ム len("não temos pertences, só bagagem")
31
ム "em" in "uma única alma dividida em duas"
True
ム len([4, 8, 15, 16, 23, 42])
6
ム 34 in [1, 1, 2, 3, 5, 8, 13, 21, 34]
True
```

`len` e `in` funcionam tanto com listas como com strings!

> É uma coincidência? Haverá mais operações em comum entre esses dois tipos de dados? Vamos descobrir tentando o seguinte:
>
> ``` python
ム"Da árvore" + "uma folha caiu"
```
>
> ``` python
ム"Sem bússola e sem rádio"[4]
```
>
> ``` python
ム[1, 4] + [4, 5]
```
>
> ``` python
ム["o", "caroço", "cantou"][2]
```

