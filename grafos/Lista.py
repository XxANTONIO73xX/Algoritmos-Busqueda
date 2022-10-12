from Nodo import *

class Lista: 
    NodoCabeza = None
    NodoCola = None

    def __init__(self, dato, costo, heuristica=None):
        self.NodoCabeza = Nodo(dato, costo, heuristica)
    
    def insertarNodo(self, dato, costo, heuristica=None): 
        """
        Si la lista está vacía, crea un nuevo nodo y lo sobreescribe 
        como el nodo principal. De lo contrario, crea un nuevo nodo, 
        va al final de la lista y establece el nuevo nodo como el 
        nodo derecho del último nodo.
        
        """
        if self.listaVacia():
            self.NodoCabeza = Nodo(dato, costo, heuristica)
        else:
            nuevoNodo = Nodo(dato, costo, heuristica)
            nodoFin = self.irAlFinal()
            nodoFin.setDerecho(nuevoNodo)
    
    def insertarNodoCabeza(self, dato, costo, heuristica=None):
        """
        Crea un nuevo nodo y, si la lista está vacía, establece el nuevo nodo como el nodo principal.
        De lo contrario, establece el puntero derecho del nuevo nodo en el nodo principal actual y 
        luego establece el nuevo nodo como el nodo principal.
        
        """
        nuevoNodo = Nodo(dato, costo, heuristica)
        if self.listaVacia():
            self.NodoCabeza = nuevoNodo
        else: 
            nuevoNodo.setDerecho(self.NodoCabeza)
            self.NodoCabeza = nuevoNodo
            return True
    
    def eliminarNodoCabeza(self):
        """
        Elimina el primer nodo de la lista y devuelve los datos de ese nodo.
        :return: Los datos del nodo que se está elimnando.
        """
        if self.listaVacia():
            return False
        else:
            dato = self.NodoCabeza.getDato()
            self.NodoCabeza = self.NodoCabeza.getDerecho()
            return dato
    
    def irAlFinal(self):
        """
        Retorna el ultimo nodo en la lista
        """
        nodoGuia = self.NodoCabeza
        while True:
            if nodoGuia.getDerecho() != None:
                nodoGuia = nodoGuia.getDerecho()
            else:
                return nodoGuia
    
    def eliminarNodo(self, dato):
        """
        Si la lista está vacía, retorna False. 
        
        Si el nodocabeza es el nodo a eliminar, pone el nodo cabeza en el siguiente nodo.
        
        De lo contrario, busca el nodo que se eliminará y, si lo encuentra, establecerá el 
        siguiente puntero del nodo anterior en el siguiente puntero del nodo que se eliminará 
        
        Por ultimo, si el nodo a eliminar es el nodo de cola, establece el nodo de cola en 
        el nodo anterior
        
        """
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
        """
        Si el nodo caebza es vacio (none), la lista está vacía
        :return: un valor booleano.
        """
        if self.NodoCabeza == None:
            return True
        else:
            return False

    def recorrerLista(self):
        """
        Si la lista estea vacía retrona el false y el nodo auxilio será igual al nodo cabeza,
        mientras que 9imprime la lista.
        :return: El valor de la varaible nodoAux.
        """
        if self.listaVacia():
            return False
        nodoAux = self.NodoCabeza
        while nodoAux != None:
            print(nodoAux.getDato(), nodoAux.getCosto(), " => ", end="")
            nodoAux = nodoAux.getDerecho()
    
    def buscarNodo(self, dato):
        """
        Devuelve el nodo con los datos que se quiere buscar, o False si no existe
        
        :return: El nodo que contiene los datos.
        """
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