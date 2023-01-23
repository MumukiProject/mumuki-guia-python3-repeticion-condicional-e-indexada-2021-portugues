E se agora quiséssemos juntar listas de strings, mas também indicando um _separador_? Por exemplo:

```python
ム juntar(" ", ["Nicki", "Nicole"])
"Nicki Nicole"
ム juntar(",", ["Esposito", "Lali"])
"Esposito,Lali"
ム juntar("", ["W", "O", "S"])
"WOS" # podemos continuar juntando sem separadores se passamos
  	# a lista vazia como argumento
```
> Vamos melhorar nossa função anterior! Modifique `juntar` para que também possamos receber um separador. O separador é o que está entre cada string.

