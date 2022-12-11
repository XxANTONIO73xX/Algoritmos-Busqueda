def arbolInput():
    #Insertar el arbol de desición
    arbol = {};
    nodos = [];
    nodoInicial = input("ingresa el nodo inicial: ")
    hijosLength = input("Dame el numero de hijos que tiene el nodo: ") 
    arbol[nodoInicial] = {"hijos":[]}
    nodos.append(nodoInicial)
    for j in range(int(hijosLength)):
        nodoHijo = input("ingresa nodo hijo: ")
        nodoHijoCosto = float(input("ingresa el costo del nodo hijo: ")) 
        arbol[nodoInicial]["hijos"].append({nodoHijo : nodoHijoCosto}) 
        arbol[nodoHijo] = {"hijos":[]}
        nodos.append(nodoHijo)

    tieneMasHijos = True
    while(tieneMasHijos):
        for key in arbol.copy():
            arbolLength = len(arbol[key]["hijos"]);
            if arbolLength == 0:
                print("Estas en el nodo ", key)
                hijosLength = input("Dame el numero de hijos que tiene el nodo "+key+" : ") 
                for j in range(int(hijosLength)):
                    nodoHijo = input("ingresa nodo hijo: ")
                    nodoHijoCosto = float(input("ingresa el costo del nodo hijo: ")) 
                    arbol[key]["hijos"].append({nodoHijo : nodoHijoCosto}) 
                    arbol[nodoHijo] = {"hijos":[]}
        res = input("Tiene mas hijos? (y/n) : ")
        if res == "n":
            tieneMasHijos = False
        return arbol;

arbol = {'A': {'hijos': [{'G1': 6.0}, {'I1': 4.0}]}, 
'G1': {'hijos': [{'I2': 1.0}, {'H1': 2.0}]}, 
'I1': {'hijos': [{'B1': 6.0}, {'G2': 1.0}]}, 
'I2': {'hijos': [{'B2': 6.0}]}, 
'H1': {'hijos': [{'B3': 2.0}]}, 
'B1': {'hijos': []}, 
'G2': {'hijos': [{'H2': 2.0}]}, 
'B2': {'hijos': []}, 
'B3': {'hijos': []}, 
'H2': {'hijos': [{'B4': 2.0}]}, 
'B4': {'hijos': []}}

#for key in arbol:
#    print(key)
#    for child in arbol[key]['hijos']:
#        print(child)
#        for value in child:
#            print(child[value])


#procedimiento = []
#for key in arbol:
#    print(key)
#


dict = {'A':'a', 'A':'b', 'A':'n'}
print(dict)

array = [{'A':{'hijos': [{'G':2.0}, {'F':3.0}]}}, {'A':{'hijos': [{'G':4.0}, {'F':6.0}]}}]
print(array)