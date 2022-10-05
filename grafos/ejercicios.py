from grafo import *

"""
En esta clase crean un gráfico con los nodos y bordes dados, y luego llama a la función costUniform en él.
"""

def ejercicio1():
    print("------------------------- ejecicio numero 1 -------------------------")
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