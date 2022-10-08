from grafo import *
from Greedy import *

def grafoGreedy():
    print("------------------------- ejecicio Greedy -------------------------")
    grafo = Grafo()
    grafo.agregarVector('Arad', 366)
    grafo.agregarVector('Timisoara', 329)
    grafo.agregarVector('Sibiu1', 253)
    grafo.agregarVector('Sibiu2', 253)
    grafo.agregarVector('Zerind', 374)
    grafo.agregarVector('Oradea1', 380)
    grafo.agregarVector('Oradea2', 380)
    grafo.agregarVector('Lugoj', 244)
    grafo.agregarVector('Mehadia', 241)
    grafo.agregarVector('Dobreta', 242)
    grafo.agregarVector('Craiova1', 160)
    grafo.agregarVector('Craiova2', 160)
    grafo.agregarVector('Craiova3', 160)
    grafo.agregarVector('Fagaras1', 176)
    grafo.agregarVector('Fagaras2', 176)
    grafo.agregarVector('Rimnicu Vilcea1', 193)
    grafo.agregarVector('Rimnicu Vilcea2', 193)
    grafo.agregarVector('Pitesti1', 100)
    grafo.agregarVector('Pitesti2', 100)
    grafo.agregarVector('Pitesti3', 100)
    grafo.agregarVector('Pitesti4', 100)
    grafo.agregarVector('Pitesti5', 100)
    grafo.agregarVector('Bucharest1', 0)
    grafo.agregarVector('Bucharest2', 0)
    grafo.agregarVector('Bucharest3', 0)
    grafo.agregarVector('Bucharest4', 0)
    grafo.agregarVector('Bucharest5', 0)
    grafo.agregarVector('Bucharest6', 0)
    grafo.agregarVector('Bucharest7', 0)

    # Arad
    grafo.relacionar('Arad', 'Timisoara', 329)
    grafo.relacionar('Arad', 'Sibiu1', 253)
    grafo.relacionar('Arad', 'Zerind', 374)

    # Timisoara
    grafo.relacionar('Timisoara', 'Lugoj', 244)

    # Lugoj
    grafo.relacionar('Lugoj', 'Mehadia', 241)

    # Mehadia
    grafo.relacionar('Mehadia', 'Dobreta', 242)

    # Dobreta
    grafo.relacionar('Dobreta', 'Craiova1', 160)

    # Craiova1
    grafo.relacionar('Craiova1', 'Pitesti1', 100)

    # Pitesti1
    grafo.relacionar('Pitesti1', 'Bucharest1', 0)

    # Sibiu1
    grafo.relacionar('Sibiu1', 'Oradea1', 380)
    grafo.relacionar('Sibiu1', 'Fagaras1', 176)
    grafo.relacionar('Sibiu1', 'Rimnicu Vilcea', 193)

    # Rimnicu Vilcea1
    grafo.relacionar('Rimnicu Vilcea1', 'Craiova2', 160)
    grafo.relacionar('Rimnicu Vilcea1', 'Pitesti3', 100)

    # Craiova2
    grafo.relacionar('Craiova2', 'Pitesti2', 160)

    # Pitesti2
    grafo.relacionar('Pitesti2', 'Bucharest2', 0)

    # Fagaras1
    grafo.relacionar('Fagaras1', 'Bucharest4', 0)

    # Zerind
    grafo.relacionar('Zerind', 'Oradea1', 380)

    # Oradea2
    grafo.relacionar('Oradea2', 'Sibiu2', 253)

    # Sibiu2
    grafo.relacionar('Sibiu2', 'Rimnicu Vilcea2', 193)
    grafo.relacionar('Sibiu2', 'Fagaras2', 176)

    # Fagaras2
    grafo.relacionar('Fagaras2', 'Bucharest7', 0)

    # Rimnicu Vilcea2
    grafo.relacionar('Rimnicu Vilcea2', 'Craiova3', 160)
    grafo.relacionar('Rimnicu Vilcea2', 'Pitesti5', 100)

    # Craiova3
    grafo.relacionar('Craiova3', 'Pitesti4', 100)

    # Pitesti5
    grafo.relacionar('Pitesti5', 'Bucharest6', 0)

    # Pitesti4
    grafo.relacionar('Pitesti4', 'Bucharest5', 0)

    print("Grafo:")

    grafo.mostrarVectores()
    print("\n")
    print("Procedimiento")
    metodoGreedy(grafo.arreglo, "Bucharest")


grafoGreedy()
