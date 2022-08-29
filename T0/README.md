# Tarea 0: Star Advanced 🚀🌌


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

<Descripción de lo que hace y que **_no_** hace la tarea que entregaron junto
con detalles de último minuto y consideraciones como por ejemplo cambiar algo
en cierta línea del código o comentar una función>

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Programación Orientada a Objetos (18pts) (22%%)
##### ✅ Menú de Inicio
##### ✅ Funcionalidades		
##### ✅ Puntajes
#### Flujo del Juego (30pts) (36%) 
##### ✅ Menú de Juego
##### 🟠 Tablero		
##### ✅ Bestias	
##### ✅ Guardado de partida		
#### Término del Juego 14pts (17%)
##### ✅ Fin del juego	
##### ❌✅🟠 Puntajes	
#### Genera: 15 pts (15%)
##### ✅ Menús
##### ✅ Parámetros
##### 🟠 PEP-8
#### Bonus: 3 décimas
##### ❌ 
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```Tarea_0.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```Tarea_0.py``` en ```T0```
2. ```partidas``` (carpeta) en ```T0``` la cual debe contiener los archivos de texto ```partidas.txt``` y ```puntajes.txt```
3. ```funciones.py``` en ```T0```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```Random```: ```random.randint / funciones.py``` (se debe importar)
2. ```math```: ```math.ceil / Tarea_0.py``` (se debe importar)

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```funciones.py```: Contiene a ```posicion()``` (permite jugar el tablero poniendo los numeros en las posiciones que escoja el jugador), ```bestias_en_tablero()``` (introduce las bestias exactas en el tablero), ```convertidor_columna_en_numero()``` (permite transformar las columnas (letras) en un valor (numerico) para utilizarlo como coordenada), ```cargar_partida()``` (permite imprimir de manera ordenadas las posibles partidas a cargar), ```cargar_ranking()``` (permite imprimir de manera ordenadas los 10 mejores puntajes guardados)


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Descripción/consideración 1 y justificación del por qué es válido/a> 
2. <Descripción/consideración 2 y justificación del por qué es válido/a>
3. ...

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>


-------



**EXTRA:** si van a explicar qué hace específicamente un método, no lo coloquen en el README mismo. Pueden hacerlo directamente comentando el método en su archivo. Por ejemplo:

```python
class Corrector:

    def __init__(self):
          pass

    # Este método coloca un 6 en las tareas que recibe
    def corregir(self, tarea):
        tarea.nota  = 6
        return tarea
```

Si quieren ser más formales, pueden usar alguna convención de documentación. Google tiene la suya, Python tiene otra y hay muchas más. La de Python es la [PEP287, conocida como reST](https://www.python.org/dev/peps/pep-0287/). Lo más básico es documentar así:

```python
def funcion(argumento):
    """
    Mi función hace X con el argumento
    """
    return argumento_modificado
```
Lo importante es que expliquen qué hace la función y que si saben que alguna parte puede quedar complicada de entender o tienen alguna función mágica usen los comentarios/documentación para que el ayudante entienda sus intenciones.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://stackoverflow.com/questions/46994453/how-to-count-specific-neighbours-in-a-nested-list-in-python-3>: este hace \<observa cierta posicion y cuenta la cantidad de "N" que se encuentran en las casillas adyacentes a esta> y está implementado en el archivo <funciones.py> en las líneas <76-77-78-79> y hace <le asiga un numero a la posicion [x][y] dependiendo de cuantas bestias tiene en las casillas adyacentes, lo utilice para crear la lista tablero_juego_admin con numeros y bestias>


## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/master/Tareas/Descuentos.md).
