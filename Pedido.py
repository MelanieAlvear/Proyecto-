from datetime import datetime
from Libro import Libro
from Revista import Revista
from Estudiante import Estudiante
from Docente import Docente

class Pedido(Libro, Revista, Estudiante, Docente):
    contador_pedido = 0

    def __init__(self, id_pedido=None, solicitante=None, lista_material=None, materia=None, fecha_prestamo=None, fecha_devolucion=None, id_docente=None, idES=None):
        self._id_pedido = id_pedido
        self._solicitante = solicitante
        self._lista_material = lista_material
        self._materia = materia
        self._fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion
        self._nombre_solicitante = None
        self._id_docente = id_docente
        self.idES = idES
        Pedido.contador_pedido += 1


    @property
    def id_pedido(self):
        return self._id_pedido

    @property
    def solicitante(self):
        return self._solicitante

    @property
    def lista_material(self):
        return self._lista_material

    @lista_material.setter
    def lista_material(self, nuevo_lista_material):
        self._lista_material = nuevo_lista_material

    @property
    def fecha_prestamo(self):
        return self._fecha_prestamo

    @fecha_prestamo.setter
    def fecha_prestamo(self, nuevo_fecha_prestamo):
        self._fecha_prestamo = nuevo_fecha_prestamo

    @property
    def fecha_devolucion(self):
        return self._fecha_devolucion

    @fecha_devolucion.setter
    def fecha_devolucion(self, nuevo_fecha_devolucion):
        self._fecha_devolucion = nuevo_fecha_devolucion

    @property
    def nombre_solicitante(self):
        return self._nombre_solicitante

    @nombre_solicitante.setter
    def nombre_solicitante(self,id_docente,idES):
        self._nombre_solicitante =id_docente, idES

    def pedir_material(self, material, id_docente=None, idES=None):
        self._lista_material = material
        self._fecha_prestamo = datetime.now()
        self._fecha_devolucion = None
        self._id_docente = id_docente
        self.idES = idES
        if self._solicitante:
            self._nombre_solicitante = self._solicitante.nombre
            print(f"Se ha realizado el préstamo del material {self._lista_material} a {self._nombre_solicitante}.")

    def devolver_material(self):
        if self._solicitante:
            self._fecha_devolucion = datetime.now()
            print(f"Se ha devuelto el material {self._lista_material} de {self._nombre_solicitante}.")
        else:
            print("No hay material para devolver o no se ha registrado un solicitante.")

# Ejemplo de uso:
# Para Revista y Estudiante
revista1 = Revista(id=301, codigo='S7V7N', titulo='SCIENCE', autor='Jhosh Pill', disponible=True, cantidad_disponible=12, tipo='Enviroment')
estudiante = Estudiante(cedula="0955403795", nombre="Melanie", apellido="Alvear", email="melaniealvear901@gmail.com",telefono="0985464272", direccion="Sauces4",  numero_libros=1, activo=True, carrera="Gestión de la información gerencial")

pedido1 = Pedido(solicitante=estudiante)

pedido1.pedir_material(revista1, idES=estudiante._idES)
print(f"Fecha de préstamo: {pedido1.fecha_prestamo}")

pedido1.devolver_material()
print(f"Fecha de devolución: {pedido1.fecha_devolucion}")

# Para Libro y Docente
libro1 = Libro(id=202, codigo="SVT137", titulo="El principito", autor="Antoine de Saint-Exupéry", disponible=True, cantidad_disponible=2, tipo_pasta="Dura")
docente = Docente(cedula="0943308221", nombre="Eileen", apellido="Gonzáles", email="gonzalezeileen213@gmail.com", telefono="0939179295", direccion="46 y Nicolás Agusto González",numero_libros=3, activo=True, carrera="Gestión de la información gerencial", id_docente=202, titulo_3er_nivel="no", titulo_4to_nivel="si")

pedido2 = Pedido(solicitante=docente)

pedido2.pedir_material(libro1, id_docente=docente.id_docente)
print(f"Fecha de préstamo: {pedido2.fecha_prestamo}")

pedido2.devolver_material()
print(f"Fecha de devolución: {pedido2.fecha_devolucion}")