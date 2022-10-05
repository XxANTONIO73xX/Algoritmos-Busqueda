from grafo import *

"""
En esta clase crean un gráfico con los nodos y bordes dados, y luego llama a la función costUniform en él.
"""

def ejercicio2():
    print("------------------------- ejecicio numero 2 -------------------------")
    grafo2 = Grafo()
    grafo2.agregarVector('S', 0)
    grafo2.agregarVector('G1', 10)
    grafo2.agregarVector('G2', 5)
    grafo2.agregarVector('G3', 5)
    grafo2.agregarVector('A', 1)
    grafo2.agregarVector('B', 5)
    grafo2.agregarVector('C', 15)
    
    #S
    grafo2.relacionar('S', 'A', 1)
    grafo2.relacionar('S', 'B', 5)
    grafo2.relacionar('S', 'C', 15)
    #A
    grafo2.relacionar('A', 'G1', 10)
    #B
    grafo2.relacionar('B', 'G2', 5)
    #C
    grafo2.relacionar('C', 'G3', 5)

    print("Grafo:")

    grafo2.mostrarVectores()
    print("\n")
    print("Procedimiento")
    costoUniforme(grafo2.arreglo, 'G')
    
ejercicio2()
