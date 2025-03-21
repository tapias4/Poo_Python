# Composicion 

"""una coordenada en dos dimenciones esta compuesta por dos valores, e valor en el eje de las X y el valor en el eje de las Y, eso podia ser una clase. Un cuadrado esta compuesto por 4 coordenadas que son los 4 vertices, eso podria ser ua clase que esta compuesta por 4 clases del objeto coordenada."""

# Clase cordenada 

class Coordenada:
    # Metodo constructor 
    def __init__(self, x, y):
        self.__X = x
        self.__Y = y

    # Metodo delectura y escritura de cada atributo    
    def getX(self):
        return self.__X
    
    def getY(self):
        return self.__Y
    
    def getX(self, x):
        self.__X = x
    
    def getX(self, y):
        self.__Y = y
    
    
    # Metodo para mostrar la coordenada 
    def mostrarCoordenada(self):
        print("(", self.__X, ",",  self.__Y,")")
 
    # Clase cuadro
    
class Cuadrado:

    # Metodo costructor
    def __init__(self,v1, v2, v3, v4):
        # atributos privados
        self.__V1 = v1
        self.__V2 = v2
        self.__V3 = v3
        self.__V4 = v4

    # metodos privados para mostrar los vertices  
    def __motrarCoordenadaV1(self):
        print("(", self.__V1.getX(), ",", self.__V1.getY(), ")")

    def __motrarCoordenadaV2(self):
        print("(", self.__V2.getX(), ",", self.__V2.getY(), ")")

    def __motrarCoordenada3(self):
        print("(", self.__V3.getX(), ",", self.__V3.getY(), ")")

    def __motrarCoordenadaV4(self):
        print("(", self.__V4.getX(), ",", self.__V4.getY(), ")")            

    # metodo para mostrar los vertices  
    def mostrarVertices(self):
        print("El cuadrado esta compuesto por los siguientes vertices: ")
        self.__mostrarCoordenadaV1()
        self.__mostrarCoordenadaV2()
        self.__mostrarCoordenadaV3()
        self.__mostrarCoordenadaV4()

    # Metodo principal
def main():
     # inpu 
    x1 = int(input("Dijite el valor de x: "))
    x2 = int(input("Dijite el valor de y: "))
    
    # processing
    c1 = Coordenada(x1,x2)
    c1.mostrarCoordenada()
    
    v1 = Coordenada(7,8)
    v2 = Coordenada(10,8)
    v3 = Coordenada(7,5)
    v4 = Coordenada(10,5)

    cuadrado1 = Cuadrado(v1, v2, v3, v4)
    cuadrado1.mostrarVertices()



    # que ocurre si el metodo get() lo hacemos privado: __getX()?
    coordenada = Coordenada(3,4)
    print("(", coordenada.getX(), ",", coordenada.getY(), ")") 




if __name__ == "__main__":
        main()