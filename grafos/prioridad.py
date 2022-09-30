from Lista import *

class Prioridad(Lista):
    def __init__(self, dato, costo):
        Lista.__init__(self, dato, costo)
        self.tamanio = 1

    def insertar(self, dato, costo):
        respuesta = self.insertarNodo(dato, costo)
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
        self.recorrerLista()
        print("\n")
        return self;
    

def buscarLista(arreglo, nodoPadre):
    for lista in arreglo:
        if lista.NodoCabeza.getDato() == nodoPadre.getDato():
            return lista


def costoUniforme(arreglo, meta):
    #empieza por el nodo raiz
    nodoAux = arreglo[0].NodoCabeza
    #se agrega a la lista con caracteristica de prioridad
    listaPrioridad = Prioridad(nodoAux.getDato(), nodoAux.getCosto())
    #el bucle se acciona mientras que el nodo sea diferente a vacio
    while nodoAux != None:
        #se valida si el nodo actual es igual al nodo raiz
        if nodoAux == arreglo[0].NodoCabeza:
            hijo = nodoAux.getDerecho()
            #se agregan los hijos a la lista de prioridades
            while hijo != None:
                #se suma el costo de los nodos hijos con el nodo padre
                sumaCostes = hijo.getCosto() + nodoAux.getCosto()
                #se agrega el hijo a la lista de prioridades
                listaPrioridad.insertar(hijo.getDato(), sumaCostes)
                #pasa al siguiente hijo
                hijo = hijo.getDerecho()
            #elimina el nodo padre
            listaPrioridad.eliminar()
            #ordena la lista de menor a mayor siendo el NodoCabeza el nodo con costo menor
            listaPrioridad = listaPrioridad.ordenar()
            #se busca la lista donde viene el proximo nodo padre e hijos
            listaBuscada = buscarLista(arreglo, listaPrioridad.NodoCabeza)
            #suma el costo de la lista buscada y el nodo padre
            sumaCostes = listaBuscada.NodoCabeza.getCosto() + nodoAux.getCosto()
            #Se modifica el costo del nodoCabeza de la lista buscada
            listaBuscada.NodoCabeza.setCosto(sumaCostes)
            #El siguiente nodo sera el nodo Cabeza de la lista buscada
            nodoAux = listaBuscada.NodoCabeza
            continue
        # Se valida si el dato del nodo es la meta buscada
        dato = str(nodoAux.getDato())
        if dato.startswith(meta):
            print("\n")
            print("Meta encontrada en ", nodoAux.getDato())
            break;
        else:
            #El hijo del nodo actual seran los nodos siguientes de la lista
            hijo = nodoAux.getDerecho()
            #se agregan los hijos a la lista de prioridades
            while hijo != None:
                #se suma el costo de los nodos hijos con el nodo padre
                sumaCostes = hijo.getCosto() + nodoAux.getCosto()
                #se agrega el hijo a la lista de prioridades
                listaPrioridad.insertar(hijo.getDato(), sumaCostes)
                #pasa al siguiente hijo
                hijo = hijo.getDerecho()
            #elimina el nodo padre
            listaPrioridad.eliminar()
            #ordena la lista de menor a mayor siendo el NodoCabeza el nodo con costo menor
            listaPrioridad = listaPrioridad.ordenar()
            #se busca la lista donde viene el proximo nodo padre e hijos
            listaBuscada = buscarLista(arreglo, listaPrioridad.NodoCabeza)
            #suma el costo de la lista buscada y el nodo padre
            sumaCostes = listaBuscada.NodoCabeza.getCosto() + nodoAux.getCosto()
            #Se modifica el costo del nodoCabeza de la lista buscada
            listaBuscada.NodoCabeza.setCosto(sumaCostes)
            #El siguiente nodo sera el nodo Cabeza de la lista buscada
            nodoAux = listaBuscada.NodoCabeza
#test
#listaPrioridad = Prioridad("A", 4.0)
#listaPrioridad.insertar("B", 2.0)
#listaPrioridad.recorrerLista()
#print("--------------Ordenado----------------------")
#listaPrioridad.ordenar()
#print("\n")
#print(listaPrioridad.NodoCabeza.getDato())