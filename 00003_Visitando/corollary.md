¡Acaban de pasar varias cosas! Primero, han entrado en escena los _rangos_, que son otro tipo de dato de Python que representa una secuencia de números, que puede ser: 

* continua, como en `range(1, 10)`, que no es nada más y nada menos que la secuencia de los números del `1` al `9` (sí, el último no entra :exclamation:)
* con saltos, como en `range(0, 10, 3)`, que son los números del `0` al `9` dando saltos de a 3: `0`, `3`, `6`, `9`

Por otro lado, acabamos de ver también que el `for ... in` nos permite "visitar" a cada elemento de una lista, string o rango de números, y hacer algo con éste. Para ello, esta estructura tiene tres partes:

 1. `in` nos permite especificar qué secuencia de elementos vamos a recorrer;
 2. `for` nos permite elegir un nombre con el que nos referiremos a cada elemento de la secuencia;
 3. y después del `:` tendremos una o más acciones que ejecutaremos al visitar cada elemento. :warning: ¡Cuidado! Tienen que estar tabuladas respecto de la línea del `for` 


En este caso, en `imprimir_cada_elemento` elegimos: 

 1. recorrer cada elemento del parámetro `elementos`:
 2. llamar a cada uno de esos elementos `elemento`;
 3. imprimir cada uno de esos elementos usando `print`.


Muy interesante, pero no parece que hayamos hecho nada muy útil :confused:. ¿Podremos hacer cosas más que sólo mostrar elementos? 



Acaba de acontecer várias coisas! Primeiro, entraram em cena as _variações_, que são outro tipo de dado de Python e representa uma sequência de números, que pode ser: 

* contínua, como `range(1, 10)`, que não é nada mais, nada menos que a sequência dos números  `1` ao `9` (se, o último não entra :exclamation:)
* aternado , como `range(0, 10, 3)`, que são os números de `0` ao `9` alternando cada 3 números: `0`, `3`, `6`, `9`

Por outro lado, acabamos de ver também que o `for ... in` permite "visitar cada elemento de uma lista, string ou variação de números, e fazer alguma coisa com eles. Para isso, esta estrutura possui três partes:

 1. `in` permite especificar qual a sequência de elementos que vamos recorrer;
 2. `for`  permite escolher um nome com o qual nos referimos a cada elemento da sequência;
 3. e depois do `:` teremos uma ou mais ações que executaremos ao visitar cada elemento. :warning: Cuidado! Eles devem ser tabulados em relação à linha `for`


Nesse caso, em `imprimir_cada_elemento` escolhemos: 

 1. percorrer cada elemento do parâmetro `elementos`:
 2. chamar a cada um desses elementos `elemento`;
 3. imprimir cada um desses elementos usando `print`.


Muito interessante, mas não parece que fizemos alguma coisa útil :confused:. Poderemos fazer mais coisas do que só mostrar elementos?
