Que sorte que encontramos você, pensamos que você estava indo embora! Você poderia ficar um pouco mais nesta lição? É que Agus e Dani nos pediram ajuda para acompanhar a conta de suas estatísticas.

Por enquanto, para Agus já definimos essa função...


```python
def quantas_vezes_ultrapassou_objetivo(duracoes):
  vezes = 0
 
  for duracao in duracoes:
	if duracao < 3:
  	vezes += 1
    
  return vezes
```

...que é muito parecida com o que já havíamos definido, mas tem uma novidade: agora estamos contando **quantas vezes** o objetivo foi superado. E para isso precisamos de um `if`, com algumas novidades:

  * Por um lado, está dentro do `for`, tabulado, e não retorna nada;
  * por outro lado, não tem `else`: se a condição não for atendida, não faz _nada_.

Em outras palavras: a cada iteração, se a condição `duracao < 3` for verdadeira, o acumulador `vezes` será incrementado, caso contrário permanecerá o mesmo.

> Sabendo disso, vamos agora ajudar o Dani a definir `quantas_vezes_eu_treino_o_suficiente`, que retorna o número de vezes que ele treinou por mais de 30 minutos.

>
> ```python
> ム quantas_vezes_treino_o_suficiente([35, 40, 32, 60])
> 4  # todos os dias treino mais de 30 minutos
> ム quantas_vezes_treino_o_suficiente([15, 45, 90, 0])
> 2 # apenas dois dias treino mais de 30 minutos
> ```
