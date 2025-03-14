# Composicion 

"""una coordenada en dos dimenciones esta compuesta por dos valores, e valor en el eje de las X y el valor en el eje de las Y, eso podia ser una clase. Un cuadrado esta compuesto por 4 coordenadas que son los 4 vertices, eso podria ser ua clase que esta compuesta por 4 clases del objeto coordenada."""

# Clase cordenada 

class Coordenada:

    # Metodo constructor 
    def __init__(self, x, y):
        self.X = x
        self.Y = y
        
    # Metodo para mostrar la coordenada 
    def mostrarCoordenada(self):
        print("(", self.X, ",",  self.Y,")")
 
    # Clase cuadro
    
class Cuadrado:

    # Metodo costructor
    def __init__(self,v1,v2,v3,v4):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3
        self.V4 = v4

    # metodo para mostrar los vertices  
    def mostrarVertices(self):
        print("El cuadrado esta compuesto por los siguientes vertices: ")
        self.V1.mostrarCoordena(7,8)
        self.V2.mostrarCoordena(10,8)
        self.V3.mostrarCoordena(7,5)
        self.V4.mostrarCoordena(10,5)

# Metodo principal
def main():
    # input
    x1 = int(input("Dijite el valor de x: "))
    x2 = int(input("Dijite el valor de y: "))
    
    # processing
    c1 = Coordenada(x1, x2)
    c1.mostrarCoordenada()

    if __name__ == "__main__":
        main()