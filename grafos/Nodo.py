class Nodo:
    def __init__(self, dato, costo, heuristica=None):
        self.__dato = dato
        self.__costo = costo
        self.__heuristica = heuristica
        self.__refDer = None
        self.__refIzq = None
    
    def getDato(self):
        """
        Devuelve el valor de la variable dato.
        :return: El valor del atributo dato.
        """
        return self.__dato
    
    def getDerecho(self):
        """
        Devuelve el hijo derecho del nodo.
        :return: El hijo derecho del nodo.
        """
        return self.__refDer
    
    def getIzquierdo(self):
        """
        Devuelve la referencia al nodo izquierdo.
        :return: La referencia al hijo izquierdo del nodo..
        """
        return self.__refIzq

    def setDato(self, nuevoDato):
        self.__dato = nuevoDato
    
    def setDerecho(self, nuevaRef):
        self.__refDer = nuevaRef

    def setIzquierdo(self, nuevaRef):
        self.__refIzq = nuevaRef
    
    def getCosto(self):
        """
        Devuelve el costo.
        :return: El costo.
        """
        return self.__costo

    def setCosto(self, nuevoCosto):
        self.__costo = nuevoCosto

    def setHeuristica(self, nuevaHeuristica):
        self.__heuristica = nuevaHeuristica
    
    def getHeuristica(self):
        return self.__heuristica
