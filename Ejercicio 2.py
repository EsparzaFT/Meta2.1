#Crear una clase persona y dos clases que hereden sus atributos, Fernando Esparza Tinoco, 17/03/22, 17/03/22

class Persona:
    def __init__(self, nombre, apellidos):
        self._nombre = nombre
        self._apellidos = apellidos

    #getters
    def get_nombre(self):
        return self._nombre

    def get_apeliidos(self):
        return self._apellidos

    #Setters
    def set_nombre(self,nombre):
        self._nombre = nombre

    def set_apellidos(self,apellidos):
        self._apellidos = apellidos

    def __str__(self):
        return 'El nombre de la persona es: {} y el apellido es: {}'.format(self._nombre,self._apellidos)

class Profesor(Persona):
    def __init__(self, nombre, apellidos, despacho):
        self._nombre = nombre
        self._apellidos = apellidos
        self._despacho = despacho

    #getters
    def get_despacho(self):
        return self._despacho

    # Setters
    def set_despacho(self, despacho):
        self._despacho = despacho

    def __str__(self):
        return 'El nombre del profesor es: {} y su apellido es: {}, {}'.format(self.get_nombre(),self.get_apeliidos(),self._despacho)

class Alumno(Persona):
    def __init__(self, nombre, apellidos, semestre):
        self._nombre = nombre
        self._apellidos = apellidos
        self._semestre = semestre

    #getters
    def get_semestre(self):
        return self._semestre

    #setters
    def set_semestre(self,semestre):
        self._semestre = semestre

    def __str__(self):
        return 'El nombre del alumno es: {} y su apellido es: {}, {}'.format(self.get_nombre(),self.get_apeliidos(),self._semestre)

persona = Persona("Alan","Espinoza Hernandez")
profesor = Profesor("Carlos","Ortiz Catlan","Despacho Tres B")
alumno = Alumno("Jun","Kim Ortiz","Semestre Siete")

print(persona)
print(profesor)
print(alumno)

print("\nSetters\n")

persona.set_nombre("Julio")
persona.set_apellidos("Perez Perez")
print(persona)

profesor.set_nombre("Josue")
profesor.set_apellidos("Rodriguez Aleman")
profesor.set_despacho("Despacho Dos C")
print(profesor)

alumno.set_nombre("Oscar")
alumno.set_apellidos("Vidal Hernandez")
alumno.set_semestre("Semestre Ocho")
print(alumno)