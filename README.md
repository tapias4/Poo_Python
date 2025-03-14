# Poo_Python

- El paradigma de POO esta basado en una abstraccion del mundo real que nos va a permitir dearrollar programas de dorma mas cercana a como vemos el mundo, pensando en objetos que tenemos delante y en acciones que podemos hacer con ellos.

## Clase

- Una clase es un tipo de dato cuyas variabes se llaman objetos o instancias.
- Una clase es la definicion del concepto de la vida real y los objetos o instancias son el "propio" objeto del mundo real. 
- Las clases estan compuestas por dos elementos: atributos y metodos.

### Atributos 
- Informacion que lmacena la clase 

### Metodos 
- Operaciones que pueden realizar la clases. 

## Definicion de una clase en python 

```Python
class NombreClase:

    def _init_ (self, variable1, variable2):
        self.Atributo1 = Valor1
        self.Atributo2 = Valor2

def NombreMetodo(self):

    bloqueCodigo
```
   
### Componentes 

```class```: Palabra reservada en python para definir una clase. 

```NombreClase```: Nombre de la clase que quieres crear

```def```: Palabra reservada en python que se utiliza tanto para definir el constructor de la clase(Metodo que se usa la primera vez que usas una clase) como los diferentes metodos que tiene. 

```__init__```: Palabra reservaa en python paraa definir el metodo constructor de la clase. Es lo primero que se ejecuta cuando creas un objeto de una clase.

```self, VariableX```: Parametro del contructor de la clase. EL prametro self es obligatorio  despues puedes tener tantos parametros como quieras, la forma de añadir parametros es a misma que en las funciones.

```self.AtributoX```: forma de utilizacion y acceso a los atributos de la clase. 

```nombreMetodo```: Nombre del metodo de la clase. 

```(self)```: Parametro del metodo. EL prametro self es obligatorio  despues puedes tener tantos parametros como quieras, la forma de añadir parametros es a misma que en las funciones.

```bloqueCodigo```: Instrucciones que ejecutara el metodo.


- Cuando defines una clase debes tener en cuenta los siguientes puntos: 
  - Puedes definir tantos atributos como necesites.
  - Puedes definir tantos meetodos como ncesites.
  - Puedes definir tantos parametros en el constructor y en los metodos como necesites. 
  

## Compsicion

- consiste en la creacion de nuevas clases apartir de otras clases ya existentes que acuan como elementos compositores de la nueva.
- Las clases existentees sern atributos de la nueva clase, en POO la composicio significa que entre las dos clases existe una relacion del tipo "Tiene un". 
- Ejemplo:
   - una coordenada en dos dimenciones esta compuesta por dos valores, e valor en el eje de las X y el valor en el eje de las Y, eso podia ser una clase. Un cuadrado esta compuesto por 4 coordenadas que son los 4 vertices, eso podria ser ua clase que esta compuesta por 4 clases del objeto coordenada.  
   