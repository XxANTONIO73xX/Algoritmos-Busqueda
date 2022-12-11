from Nodo import *

class Lista: 
    NodoCabeza = None
    NodoCola = None

    def __init__(self, dato, costo):
        self.NodoCabeza = Nodo(dato, costo)
    
    def insertarNodo(self, dato, costo): 
        if self.listaVacia():
            self.NodoCabeza = Nodo(dato, costo)
        else:
            nuevoNodo = Nodo(dato, costo)
            nodoFin = self.irAlFinal()
            nodoFin.setDerecho(nuevoNodo)
    
    def insertarNodoCabeza(self, dato, costo):
        nuevoNodo = Nodo(dato, costo)
        if self.listaVacia():
            self.NodoCabeza = nuevoNodo
        else: 
            nuevoNodo.setDerecho(self.NodoCabeza)
            self.NodoCabeza = nuevoNodo
            return True
    
    def eliminarNodoCabeza(self):
        if self.listaVacia():
            return False
        else:
            dato = self.NodoCabeza.getDato()
            self.NodoCabeza = self.NodoCabeza.getDerecho()
            return dato
    
    def irAlFinal(self):
        nodoGuia = self.NodoCabeza
        while True:
            if nodoGuia.getDerecho() != None:
                nodoGuia = nodoGuia.getDerecho()
            else:
                return nodoGuia
    
    def eliminarNodo(self, dato):
        if self.listaVacia():
            return False
        else: 
            #1. Verificar que el Nodo Cabeza es el dato a Buscar
            if self.NodoCabeza.getDato() == dato:
                self.NodoCabeza = self.NodoCabeza.getDerecho()
                return True
            else:
                #2. Buscar el Nodo a Eliminar
                nodoAux = self.NodoCabeza
                nodoAnterior = None
                while nodoAux.getDato() != dato:
                    nodoAnterior = nodoAux
                    nodoAux = nodoAux.getDerecho()
                    if nodoAux == None:
                        return False
                nodoAnterior.setDerecho(nodoAux.getDerecho())
                if nodoAux == self.NodoCola:
                    self.NodoCola = nodoAnterior
                return True;
    
    def listaVacia(self):
        if self.NodoCabeza == None:
            return True
        else:
            return False

    def recorrerLista(self):
        if self.listaVacia():
            return False
        nodoAux = self.NodoCabeza
        while nodoAux != None:
            print(nodoAux.getDato(), nodoAux.getCosto(), " => ", end="")
            nodoAux = nodoAux.getDerecho()
    
    def buscarNodo(self, dato):
        nodoGuia = self.NodoCabeza
        while True:
            if nodoGuia.getDerecho() != None:
                if nodoGuia.getDato() == dato:
                    print(nodoGuia)
                    return nodoGuia;
                else:
                    nodoGuia = nodoGuia.getDerecho()
            else:
                if nodoGuia.getDato() == dato:
                    return nodoGuia;
                return False