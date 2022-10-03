from Lista import *
#from Cola import *
from prioridad import *

class Grafo:
    arreglo = []

    def agregarVector(self, dato, costo):
        lista = Lista(dato, costo)
        self.arreglo.append(lista)
        

    def mostrarVectores(self):
        for lista in self.arreglo:
            lista.recorrerLista()
            print("\n")
    
    def relacionar(self, vector1, vector2, costoV2):
        for lista in self.arreglo:
            if lista.NodoCabeza.getDato() == vector1:
                lista.insertarNodo(vector2, costoV2)


