from Lista import *
#from Cola import *
from prioridad import *

# Esta clase crea una lista de listas, donde cada lista es un nodo con una cabeza y una cola..
class Grafo:
    arreglo = []

    def agregarVector(self, dato, costo, heuristica=None):
        """
        Agrega un nuevo vector(node)  al final de la lista.
        
        :param dato: El nombre del nodo
        :param costo: el costo del mismo
        """
        lista = Lista(dato, costo, heuristica)
        self.arreglo.append(lista)
        

    def mostrarVectores(self):
        """
        Imprime el contenido de cada lista en el array
        """
        for lista in self.arreglo:
            lista.recorrerLista()
            print("\n")
    
    def relacionar(self, vector1, vector2, costoV2, heuristicaV2=None):
        """
        Toma el vector1 y el vector2, así como tambien el costoV2 e inserta el vector2 y el costoV2 
        en la lista que tiene el vector1 como cabeza
        
        :param vector1: El primer vector(primer nodo)
        :param vector2: El vector(nodo) que se insertará en la lista.
        :param costoV2: El costo del borde
        """
        for lista in self.arreglo:
            if lista.NodoCabeza.getDato() == vector1:
                lista.insertarNodo(vector2, costoV2, heuristicaV2)


