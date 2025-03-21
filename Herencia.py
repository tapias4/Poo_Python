# Clase Persona

class Persona:
    
    # método constructor
    def __init__(self):
        self.__Nombre = ""
        self.__Apellidos = ""
        self.__Edad = 0

    def getNombre(self):
        return self.__Nombre
    
    def setNombre(self, nombre):
        self.__Nombre = nombre

    def getApellidos(self):
        return self.__Apellidos
    
    def setApellidos(self, apellidos):
        self.__Apellidos = apellidos

    def getEdad(self):
        return self.__Edad
    
    def setEdad(self, edad):
        self.__Edad = edad

    # método para mostrar los datos de una persona
    def MostrarPersona(self):
        print("Nombre: " + self.__Nombre)
        print("Apellidos: " + self.__Apellidos)
        print("Edad: " + str(self.__Edad))

class Alumno(Persona):
    def __init__(self):
        self.__Curso = ""
        self.__Asignaturas = ""
    
    def getCurso(self):
        return self.__Curso
    
    def setCurso(self, curso):
        self.__Curso = curso

    def getAsignaturas(self):
        return self.__Asignaturas
    
    def setAsignaturas(self, asignaturas):
        self.__Asignaturas = asignaturas

    def mostrarAlumno(self):
        print("Alumno")
        print("\tNombre: ", self.getNombre())
        print("\tApellidos: ", self.getApellidos())
        print("\tEdad: ", self.getEdad())
        print("\tCurso: ", self.__Curso)
        print("\tMatrículas: ", self.__Asignaturas)

class Profesor(Persona):
    def __init__(self):
        self.__Antiguedad = ""
        self.__Tutorias = ""
        self.__Telefono = ""
    
    def getAntiguedad(self):
        return self.__Antiguedad
    
    def setAntiguedad(self, antiguedad):
        self.__Antiguedad = antiguedad
    
    def getTutorias(self):
        return self.__Tutorias
    
    def setTutorias(self, tutorias):
        self.__Tutorias = tutorias
        

    def getTelefono(self):
        return self.__Telefono    
    def setTelefono(self, telefono):
        self.__Telefono = telefono

    def mostrarProfesor(self):
        print("Profesor")
        print("\tNombre: ", self.getNombre())
        print("\tApellidos: ", self.getApellidos())
        print("\tEdad: ", self.getEdad())
        print("\tAntiguedad: ", self.__Antiguedad)
        print("\tTutorias: ", self.__Tutorias)
        print("\tTelefono: ", self.__Telefono)


# metodo principal
def main():
    alumno = Alumno()
    alumno.setNombre("Diego Fernando")
    alumno.setApellidos("Tapias Diaz")
    alumno.setEdad(17)
    alumno.setCurso("Bachillerato")
    alumno.setAsignaturas(["Matemáticas", "Tecnología", "Inglés"])
    alumno.mostrarAlumno()

    profesor = Profesor()
    profesor.setNombre("Néstor Jesus")
    profesor.setApellidos("Páez Sarmiento")
    profesor.setEdad(60)
    profesor.setAntiguedad("3 años")
    profesor.setTutorias(["Matemáticas de 12:30 a 2:30", "Sandwuchadas 3:40 a 4:40", "Inglés de 5:00 a 6:45"])
    profesor.setTelefono("3105852023")
    profesor.mostrarProfesor()


if __name__ == "__main__":
    main()