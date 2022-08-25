_Mas o `for` não é apenas sobre números! Por exemplo, também poderíamos usá-lo para acumular um resultado booleano._ :open_mouth:

Agus quer saber se em algum de seus últimos tempos de natação :person_swimming: ele ultrapassou sua meta pessoal de 3 minutos:

```python
ム alguma_vez_ultrapassou_meta([3.2, 3.4, 3.01, 3.08])
False # todas os seus tempos foram de mais de 3 minutos
ム alguma_vez_ultrapassou_meta([3.1, 3.2, 2.9, 3.1])
True  # um de seus tempos (2.9) foi menor que 3 minutos
```

E para isso definiu a seguinte função:

```python
def alguma_vez_ultrapassou_meta(duracoes):
  ultrapassou = False # a principio, não ultrapassou o tempo de 3 minutos
 
  for duracao in duracoes:
	ultrapassou = ultrapassou or duracao < 3 # mas se alguma delas é menor que 3 minutos,
                                	# então sim vai ter ultrapassado
 
  return ultrapassou
```

Como podemos ver, aqui a variável local que estamos usando de _acumulador_ é booleana, e em cada _iteração_ (ou seja, cada vez que visitamos uma `duracao`) vamos atualizar o valor, para saber se esta `duracao` ou qualquer das anteriores foi menor que 3.


> Agora é a sua vez! Dani também não quer perder o treino diário de futebol :soccer: e ele precisa de uma função `todos_os_dias_um_pouco` que utilize uma lista de quantos minutos ele treinou por dia, e retorne se seu treino diário sempre foi maior que 30 minutos:
>
>
> ```python
> ム todos_os_dias_um_pouco([35, 40, 32, 60])
> True  # todos os dias praticou mais de 30 minutos
> ム todos_os_dias_um_pouco([15, 45, 90, 0])
> False # um dia praticou apenas 15 minutos, e o outro não praticou nada
>```
>
> Novamente, deixamos você com o molde da função para servir como ponto de partida.

