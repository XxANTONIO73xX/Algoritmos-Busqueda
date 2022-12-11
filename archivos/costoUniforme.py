class NodoPadre:
    def __init__(self, name, nodosHijos):
        self.name = name
        self.nodosHijos = nodosHijos


def buscar(nodosList, nodoSearch):
    for i in nodosList:
        if i.name == nodoSearch:
            return i;


def insertarArbol():
    nodos = [];
    hayMasNodos = True
    while(hayMasNodos):
        name = input("ingresa el nombre del nodo: ")
        hijosLength = input("Dame el numero de hijos que tiene el nodo: ")
        nodosHijos = {}
        for j in range(int(hijosLength)):
            nodoHijo = input("ingresa nodo hijo: ")
            nodoHijoCosto = float(input("ingresa el costo del nodo hijo: "))
            nodosHijos[nodoHijo] = nodoHijoCosto
        nodoPadre = NodoPadre(name, nodosHijos);
        nodos.append(nodoPadre)
        res = input("hay mas nodos? (y/n) : ")
        if res == 'n':
            break
    return nodos;

nodos = [
    NodoPadre('A', {'G1':6.0, 'I1':4.0}),
    NodoPadre('G1', {'I2':1.0, 'H1':2.0}),
    NodoPadre('I2', {'B2':6.0}),
    NodoPadre('B2', {}),
    NodoPadre('H1', {'B3':2.0}),
    NodoPadre('B3', {}),
    NodoPadre('I1', {'B1':6.0, 'G2':1.0}),
    NodoPadre('B1', {}),
    NodoPadre('G2', {'H2':2.0}),
    NodoPadre('H2', {'B4':2.0}),
    NodoPadre('B4', {})
]
nodoInicial = input("Dime cual es el nodo inicial: ")
meta = input("Dime cual es la meta: ")

#nodoEncontrado = buscar(nodos, nodoInicial)
#print(nodoEncontrado.name, nodoEncontrado.nodosHijos, "Valor de G1  " + str(nodoEncontrado.nodosHijos['G1']))

procedimiento = {}
procedimiento[nodoInicial] = 0.0

continuar = True
while(True):
    for nodo, costo in procedimiento.items():
        if nodo.startswith(meta):
            print("meta encontrada en: "+i)
            break;
        else:
            nodoBuscado = buscar(nodos, nodo);
            for hijo in nodoBuscado.nodosHijos:
                procedimiento[hijo] = nodoBuscado.nodosHijos[hijo] + costo




for nodo in nodos:
    for hijo in nodo.nodosHijos:
        if hijo.startswith(meta):
            print("Meta encontrada")
            
