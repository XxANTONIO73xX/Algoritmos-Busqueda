from Lista import *
"""
Está clase hereda de la clase lista.
Contiene las funciones de insertar, eliminar y ordendar
"""
class Prioridad(Lista):
    def __init__(self, dato, costo):
        Lista.__init__(self, dato, costo)
        self.tamanio = 1

    def insertar(self, dato, costo):
        """
        La función insertar() toma dos argumentos, dato y costo, 
        y devuelve el valor de la función insertarNodo() si no es False
        
        """
        respuesta = self.insertarNodo(dato, costo)
        if respuesta != False:
            self.tamanio += 1
    
    def eliminar(self):
        """
        Elimina el primer nodo de la lista y devuelve los datos de ese nodo
        :return: Los datos del nodo que se eliminó.
        """
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
    

def buscarLista(arreglo, nodoPadre):
    """
    Devuelve la lista del array que tiene el mismo nodo principal que el nodo pasado como parámetro.
    
    :return: La lista que contiene el nodo que es el padre del nodo que se busca.
    """
    for lista in arreglo:
        if lista.NodoCabeza.getDato() == nodoPadre.getDato():
            return lista


def costoUniforme(arreglo, meta):
    """
    Esta función realiza la búsqueda de costo uniforme.
    
    :param arreglo: es un array de listas
    :param meta: el nodo meta
    """
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
            #El siguiente nodo sera el nodo Cabeza de la lista prioridad
            nodoAux = listaPrioridad.NodoCabeza
            continue
        # Se valida si el dato del nodo es la meta buscada
        dato = str(nodoAux.getDato())
        if dato.startswith(meta):
            print("\n")
            print("Meta encontrada en ", nodoAux.getDato())
            break;
        else:
            #se buscan el nodo en el arbol para desplegar a sus hijos
            listaBuscada = buscarLista(arreglo, nodoAux)
            #El hijo del nodo actual seran los nodos siguientes de la lista
            hijo = listaBuscada.NodoCabeza.getDerecho()
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
            #El siguiente nodo sera el nodo Cabeza de la lista prioridad
            nodoAux = listaPrioridad.NodoCabeza
#test
#listaPrioridad = Prioridad("A", 4.0)
#listaPrioridad.insertar("B", 2.0)
#listaPrioridad.recorrerLista()
#print("--------------Ordenado----------------------")
#listaPrioridad.ordenar()
#print("\n")
#print(listaPrioridad.NodoCabeza.getDato())