class Nodo:
    def __init__(self, dato, costo):
        self.__dato = dato
        self.__costo = costo
        self.__refDer = None
        self.__refIzq = None
    
    def getDato(self):
        return self.__dato
    
    def getDerecho(self):
        return self.__refDer
    
    def getIzquierdo(self):
        return self.__refIzq

    def setDato(self, nuevoDato):
        self.__dato = nuevoDato
    
    def setDerecho(self, nuevaRef):
        self.__refDer = nuevaRef

    def setIzquierdo(self, nuevaRef):
        self.__refIzq = nuevaRef
    
    def getCosto(self):
        return self.__costo

    def setCosto(self, nuevoCosto):
        self.__costo = nuevoCosto
