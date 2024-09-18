print("Programación POO")
# Definicion de clases
class Perro:
    #funciones dentro de la clase
    def morder(self):
        print("El perro me mordio")
    def datos_perro(self,nombre,edad):
        print(f" Nombre: {nombre} edad: {edad}")
# Zona creacion de objetos
pitbull=Perro()

# Zona de uso de objetos
pitbull.datos_perro("Bobby" ,4)
pitbull.morder()