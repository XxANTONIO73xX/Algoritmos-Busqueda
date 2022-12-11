from Lista import *

class Aasterisco(Lista):
    def __init__(self, dato, costo, heuristica):
        Lista.__init__(self, dato, costo, heuristica)
        self.tamanio = 1
    
    def insertar(self, dato, costo, heuristica):
        respuesta = self.insertarNodo(dato, costo, heuristica)
        if respuesta != False:
            self.tamanio += 1
    
    def eliminar(self):
        dato = self.eliminarNodoCabeza()
        if dato:
            self.tamanio -= 1
            return dato
        else:
            return False
    
    def ordenar(self):
        """
        Ordena una lista enlazada intercambiando los nodos de posicion
        :return: La lista ordenada.
        """
        #print("----sin ordenar----")
        #self.recorrerLista()
        fin = None
        while fin != self.NodoCabeza:
            r = p = self.NodoCabeza
            while p.getDerecho() != fin:
                q = p.getDerecho()
                if p.getCosto() > q.getCosto():
                    p.setDerecho(q.getDerecho())
                    q.setDerecho(p)
                    if p != self.NodoCabeza:
                        r.setDerecho(q)
                    else:
                        self.NodoCabeza = q
                    aux = p
                    p = q
                    q = aux
                r = p
                p = p.getDerecho()
            fin = p
        print("\n")
        #print("----ordenado-----")
        self.recorrerLista()
        #print("\n")
        return self;
    

def bucarLista(arreglo, nodoPadre):
    for lista in arreglo:
        if lista.NodoCabeza.getDato() == nodoPadre.getDato():
            return lista

def metodoAsterisco(arreglo, meta):
    nodoAux = arreglo[0].NodoCabeza
    