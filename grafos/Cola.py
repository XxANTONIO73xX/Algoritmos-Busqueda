from Lista import *

# Esta clase implementa una cola como una lista enlazada
class Cola(Lista):
    def __init__(self, dato):
        Lista.__init__(self, dato)
        self.tamanio = 1

    def insertar(self, dato):
        """
        Inserta un nodo en el árbol..
        
        :param dato: Los datos a insertar en el árbol.
        :return: El nodo que se insertó.
        """
        respuesta = self.insertarNodo(dato)
        if respuesta != False:
            self.tamanio = self.tamanio + 1
            return respuesta;
    
    def quitar(self):
        """
        Elimina el primer elemento de la lista y lo devuelve.
        :return: Los datos del nodo que se eliminó.
        """
        dato = self.eliminarNodoCabeza()
        if dato:
            self.tamanio = self.tamanio - 1
            return dato
        else:
            return False;
    