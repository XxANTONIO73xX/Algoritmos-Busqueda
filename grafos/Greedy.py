from Lista import *

class Greedy(Lista):
    def __init__(self, dato, costo):
        Lista.__init__(self, dato, costo)
        self.tamanio = 1
    
    def insertar(self, dato, costo):
        respuesta = self.insertarNodo(dato, costo)
        if respuesta != False:
            self.tamanio += 1
    
    def elminar(self):
        dato = self.eliminarNodoCabeza()
        if dato:
            self.tamanio -= 1
            return dato
        else:
            return False
    

def bucarLista(arreglo, nodoPadre):
    for lista in arreglo:
        if lista.NodoCabeza.getDato() == nodoPadre.getDato():
            return lista
    

def desplegarHijos(nodo, arreglo):
    lista = bucarLista(arreglo, nodo)
    hijo =  lista.NodoCabeza.getDerecho()
    while hijo != None:
        print("Desplegando hijos:")
        print(hijo.getDato(), hijo.getCosto(), " => ", end="")
        hijo = hijo.getDerecho()


def metodoGreedy(arreglo, meta):
    nodoAux = arreglo[0].NodoCabeza
    listaGreedy = Greedy(nodoAux.getDato(), nodoAux.getCosto())
    print("Nodo raiz: ", nodoAux.getDato())
    while nodoAux != None:
        if nodoAux == arreglo[0].NodoCabeza:
            desplegarHijos(nodoAux, arreglo)
            hijo = nodoAux.getDerecho()
            hijoMenorCosto = hijo
            while hijo != None:
                if hijoMenorCosto.getCosto() > hijo.getDerecho().getCosto():
                    hijoMenorCosto = hijo.getDerecho()
                hijo = hijo.getDerecho()
            print("Nodo seleccionado: ", hijoMenorCosto)
            listaGreedy.insertar(hijoMenorCosto.getDato(), hijoMenorCosto.getCosto())
            nodoAux = hijoMenorCosto
        dato = str(nodoAux.getDato)
        if dato.startswith(meta):
            print("\n")
            print("Meta encontrada en ", nodoAux.getDato())
            break;
        else:
            listaBuscado = bucarLista(arreglo, nodoAux)
            desplegarHijos(listaBuscado, arreglo)
            hijo = nodoAux.getDerecho()
            hijoMenorCosto = hijo
            while hijo != None:
                if hijoMenorCosto.getCosto() > hijo.getDerecho().getCosto():
                    hijoMenorCosto = hijo.getDerecho()
                hijo = hijo.getDerecho()
            print("Nodo seleccionado: ", hijoMenorCosto)
            listaGreedy.insertar(hijoMenorCosto.getDato(), hijoMenorCosto.getCosto())
            nodoAux = hijoMenorCosto
    print("Respuesta: ")
    listaGreedy.recorrerLista()