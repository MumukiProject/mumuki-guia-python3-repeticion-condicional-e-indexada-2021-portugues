Os segmentos `[:]` e o operador de indexação `[]` não seriam tão úteis se não pudéssemos contar de trás para frente também! :arrow_left: É por isso que Python permite usar:

 * índices positivos: começam em `0` e contam os elementos da primeira até a última posição;
 * índices negativos: começam em `-1` e contam os elementos da última posição até a primeira.

Por exemplo, isso permitirá entender a string `"olá mundo"` de duas maneiras diferentes...


<table class="table table-bordered">
<thead>
  <tr>
	<th></th>
	<th>h</th>
	<th>o</th>
	<th>l</th>
	<th>a</th>
	<th></th>
	<th>m</th>
	<th>u</th>
	<th>n</th>
	<th>d</th>
	<th>o</th>
  </tr>
</thead>
<tbody>
  <tr>
	<td>➡️</td>
	<td>0</td>
	<td>1</td>
	<td>2</td>
	<td>3</td>
	<td>4</td>
	<td>5</td>
	<td>6</td>
	<td>7</td>
	<td>8</td>
	<td>9</td>
  </tr>
  <tr>
	<td>⬅️</td>
	<td>-10</td>
	<td>-9</td>
	<td>-8</td>
	<td>-7</td>
	<td>-6</td>
	<td>-5</td>
	<td>-4</td>
	<td>-3</td>
	<td>-2</td>
	<td>-1</td>
  </tr>
</tbody>
</table>


... e realizar operações como as seguintes:

```python
ム "olá mundo"[:3] # os primeiros 3 caracteres, como já conhecemos
"olá"
ム "olá mundo"[:-1] # todos os caracteres exceto o último
"olá mund"
ム "olá mundo"[-5:] # os últimos 5 caracteres
"mundo"
ム "olá mundo"[0] # primeiro caractere, como já conhecemos.
"o"
ム "olá mundo"[-1] # último caractere
"o"            	 
ム "olá mundo"[-2] # penúltimo caractere
"d"
```

> Vamos colocar em prática tudo o que vimos! Defina:
>
> * uma função `sem_extremos` que utilize uma lista e retorne outra igual, mas sem o primeiro e o último elemento;
> * uma função `extremos` que faça exatamente o oposto, ou seja, utilize uma lista e retorne outra com apenas o primeiro e o último elemento.

>
> ```python
> ム sem_extremos([4, 5, 10, 2, 3])
> [5, 10, 2]
> ム extremos([4, 5, 10, 2, 3])
> [4, 3]
> ```
