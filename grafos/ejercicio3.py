from grafo import *

"""
En esta clase crean un gráfico con los nodos y bordes dados, y luego llama a la función costUniform en él.
"""

def ejercicio3():
    
    print("------------------------- ejecicio numero 3 -------------------------")
    
    grafo3 = Grafo()
    grafo3.agregarVector('A', 0)  
    grafo3.agregarVector('B', 4)
    grafo3.agregarVector('C', 5)    
    grafo3.agregarVector('D', 7)
    grafo3.agregarVector('E', 9)
    grafo3.agregarVector('F', 3)
    grafo3.agregarVector('G', 8) 
    grafo3.agregarVector('H', 5)
    grafo3.agregarVector('I1', 4)
    grafo3.agregarVector('I2', 1)
    grafo3.agregarVector('I3', 4)
    grafo3.agregarVector('J1', 4)
    grafo3.agregarVector('J2', 2)
    grafo3.agregarVector('K', 2)    
    grafo3.agregarVector('L', 5)
    grafo3.agregarVector('M', 7)
    
    
    #A
    grafo3.relacionar('A', 'B', 4)
    grafo3.relacionar('A', 'C', 5)

    #B
    grafo3.relacionar('B', 'D', 7)
    grafo3.relacionar('B', 'E', 9)
    
    #C
    grafo3.relacionar('C', 'F', 3)
    grafo3.relacionar('C', 'G', 8)
    
    #D
    grafo3.relacionar('D', 'H', 5)
    grafo3.relacionar('D', 'I1', 4)
    
    #E
    grafo3.relacionar('E', 'I2', 1)
    
    #F
    grafo3.relacionar('F', 'I3', 4)
    grafo3.relacionar('F', 'J1', 4)
    
    #G
    grafo3.relacionar('G', 'J2', 2)
    grafo3.relacionar('G', 'K', 2)
    
    #H
    grafo3.relacionar('H', 'L', 5)
    
    #L
    grafo3.relacionar('L', 'M', 7)

    print("Grafo:")

    grafo3.mostrarVectores()
    print("\n")
    print("Procedimiento")
    costoUniforme(grafo3.arreglo, 'I')
    
ejercicio3()