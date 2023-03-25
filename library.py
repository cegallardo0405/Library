class Biblioteca:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.libros = []
        self.libros_prestados = []


    def añadir_libro(self, libro):
        self.libros.append(libro)

    def tengo_libro(self , nombre_lib):
        for libro in self.libros:
            if libro.nombre == nombre_lib:
                return libro
        return None



class Libro:

    def __init__(self,nombre):
        self.libro_tomado = False
        self.nombre = nombre

    def fue_tomado(self):
        self.libro_tomado = True

    def fue_devuelto(self):
        self.libro_tomado = False



class Usuario:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.libros_en_posesion = []


    def solicitar(self, nombre_lib, biblioteca):
        libro = biblioteca.tengo_libro(nombre_lib)
        if libro:
            if not libro.libro_tomado:
                libro.fue_tomado()
                self.libros_en_posesion.append(libro)
                biblioteca.libros_prestados.append(libro)
                biblioteca.libros.remove(libro)
                print(self.nombre," El libro ",libro.nombre, " se le ha prestado satisfactoriamente")
            else:
                print("El libro ",libro.nombre," no está disponible para prestar en este momento")
        else:
            print(self.nombre," no tenemos este libro por el momento")


    def regresar(self, nombre_lib, biblioteca):
        for libro in self.libros_en_posesion:
            if libro.nombre == nombre_lib:
                self.libros_en_posesion.remove(libro)
                biblioteca.libros.append(libro)
                biblioteca.libros_prestados.remove(libro)
                libro.fue_devuelto()
                print(self.nombre," ha devuelto el libro ",libro.nombre,)
                break
        else:
            print("No puede devolver el libro ",nombre_lib," porque no lo ha prestado")



biblioteca = Biblioteca("KCP")
print("Bienvenido a la Biblioteca ",biblioteca.nombre)
lib1 = Libro("100 años de soledad")
lib2 = Libro("El olvido que seremos")
lib3 = Libro("El principito")
lib4 = Libro("El lazarillo de tormes")
biblioteca.añadir_libro(lib1)
biblioteca.añadir_libro(lib2)
biblioteca.añadir_libro(lib3)
biblioteca.añadir_libro(lib4)
print("_________________________________________________________________________")
print("Actualmente tenemos los siguientes libros disponibles: ")
for libro in biblioteca.libros:
    print(libro.nombre)
user = Usuario(1323,"Alex")
user1 = Usuario(1323,"Alexa")
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
user.solicitar("100 años de soledad", biblioteca)
user.solicitar("El olvido que seremos", biblioteca)
user.solicitar("El principito", biblioteca)
user1.solicitar("El principito", biblioteca)
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("_________________________________________________________________________")
print("Ahora tenemos estos libros disponibles: ")
for libro in biblioteca.libros:
    print(libro.nombre)
print("*************************************************************************")
print("Estos son los libros que tenemos actualmente en prestamo: ")
for libro in biblioteca.libros_prestados:
    print(libro.nombre)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(user.nombre, " usted tiene prestado los siguientes libros: ")
for libro in user.libros_en_posesion:
    print(libro.nombre)
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
user.regresar("100 años de soledad", biblioteca)
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
print("_________________________________________________________________________")
print("Ahora tenemos disponibles estos libros:")
for libro in biblioteca.libros:
    print(libro.nombre)
print("*************************************************************************")
print("Ahora estos son los libros que tenemos actualmente en prestamo: ")
for libro in biblioteca.libros_prestados:
    print(libro.nombre)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(user.nombre, " ahora usted tiene prestado los siguientes libros: ")
for libro in user.libros_en_posesion:
    print(libro.nombre)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")



