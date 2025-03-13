# Clase Persona

class Persona:
    # Metodo Constructor
    def __init__(self, nombre, apellidos, edad):
        self.Nombre = nombre
        self.Apellidos = apellidos
        self.Edad = edad


    # Metodo para mostrar los datos de una persona 
    def MostrarPersona(self):
        print("Nombre: " + self.Nombre)
        print("Apellidos: " + self.Apellidos)
        print("Edad: " + str(self.Edad))



# Metodo principal 
def main():
    p1 = Persona("Diego", "Tapias", 17)
    p1.MostrarPersona()
    p2 = Persona("Juan", "Delgado", 18)
    p2.MostrarPersona()
    p1.Edad = 18
    p1.MostrarPersona()
    p1 = p2
    p1.MostrarPersona()
    p2.MostrarPersona()

if __name__ == "__main__":
    main() 