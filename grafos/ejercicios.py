from grafo import *


def ejercicio1():
    print("ejecicio numero 1 ------------------------------------------")
    grafo = Grafo()
    grafo.agregarVector('A', 0)
    grafo.agregarVector('G1', 6)
    grafo.agregarVector('I1', 4)
    grafo.agregarVector('I2', 1)
    grafo.agregarVector('H1', 2)
    grafo.agregarVector('B1', 6)
    grafo.agregarVector('G2', 1)
    grafo.agregarVector('B2', 6)
    grafo.agregarVector('B3', 2)
    grafo.agregarVector('H2', 2)
    grafo.agregarVector('B4', 2)
    #A
    grafo.relacionar('A', 'G1', 6)
    grafo.relacionar('A', 'I1', 4)
    #G1
    grafo.relacionar('G1', 'I2', 1)
    grafo.relacionar('G1', 'H1', 2)
    #I1
    grafo.relacionar('I1', 'B1', 6)
    grafo.relacionar('I1', 'G2', 1)
    #I2
    grafo.relacionar('I2', 'B2', 6)
    #H1
    grafo.relacionar('H1', 'B3', 2)
    #G2
    grafo.relacionar('G2', 'H2', 2)
    #H2
    grafo.relacionar('H2', 'B4', 2)

    print("Grafo:")

    grafo.mostrarVectores()
    print("\n")
    print("Procedimiento")
    costoUniforme(grafo.arreglo, 'B')



#ejecutar ejericios aqui
ejercicio1()