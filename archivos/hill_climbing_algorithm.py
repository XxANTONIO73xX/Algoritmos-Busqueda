import random
import time

'''
Función 1: el parámetro es el estado actual del diseño del tablero, y el numero de reinas en
en los ocho conflictos de diseño reina actuales se determina de acuerdo con el diseño.
'''
def getNumofConflict(status):
    num = 0
    for i in range(len(status)):
        for j in range(i + 1, len(status)):
            if status[i] == status[j]:
                num += 1
            offset = j - i
            if abs(status[i]-status[j]) == offset:
                num += 1
    return num

'''
Funcion 2: el parametro es el diseño actual del tablero, use el metodo hill climbing o escalada
para seleccionar el mejor diseño para el estado vecino y regrese.
'''

def hillClimbing(status):
    convert = {}
    length = len(status)
    for col in range(length):
        bestMove = status[col]
        for row in range(length):
            if status[col] == row:
                continue
            statusCopy = list(status)
            statusCopy[col] = row
            convert[(col, row)] = getNumofConflict(statusCopy)
    answers = [] #Mejor colecci[on sucesora
    conflictRow = getNumofConflict(status) #Registro actual de conflictos de reina

    # Recorre el diccionario que almacena todos los sucesores posibles para encontrar el mejor
    for key,value in iter(convert.items()):
        if value < conflictRow:
            conflictRow = value
    for key,value in iter(convert.items()):
        if value == conflictRow:
            answers.append(key)
    
    # Si el mejor elemento de conjunto sucesor es mayor que uno, seleccione uno al azar

    if len(answers) > 0:
        x = random.randint(0, len(answers) - 1)
        col = answers[x][0]
        row = answers[x][1]
        status[col] = row
    
    return status

'''
Funcion 3: encontrar una solucion en la que las ocho reinas satisfagan el numero de conflictos
a 0 y repita el conjunto posterior a cada paso hasta que no haya conflicto.
'''

def queens():
    status = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # En el estado inicial, todas las reinas estan en diagonal

    '''
    Cuando el numero de conflictos es mayor que 0, el mejor sucesor se resuelve ciclicamente hasta
    que se encuentren las ocho soculciones reina
    '''

    while getNumofConflict(status) > 0:
        status = hillClimbing(status)
        #time.sleep(5)
        print(status)
        print(getNumofConflict(status))
        
    for s in range(len(status)):
        status[s] += 1
    print("The answer is")
    print(status)
queens()