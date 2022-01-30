'''
Libreria CNYT
Operaciones con Vectores y Matrices
Andrea Durán Vivas
'''

import Libcplx as lc

#verificar que el tamaño de los vectores sean iguales
def verificacion (v,w):
    '''Función que verifica si dos vectores son del mismo tamaño
       (list, list) --> bool'''
    fila1 = len(v)
    fila2 = len(w)

    return fila1 == fila2


#Suma de vectores
def sumavec (v, w):
    '''Función que retorna la suma entre dos vectores
       (list, list) --> list'''
    if verificacion(v, w) == True:
        lon = len(v)
        res = [(0,0) for i in range(lon)]
        j = 0

        while j < lon:
            res[j] = lc.sumacplx(v[j], w[j])
            j += 1

        return res

    return 'Inconsistente: El tamaño de las matrices o los vectores no es igual'

def restavec (v, w):
    '''Función que retorna la resta entre dos vectores
       (list, list) --> list'''
    if verificacion(v, w) == True:
        lon = len(v)
        res = [(0,0) for i in range(lon)]
        j = 0

        while j < lon:
            res[j] = lc.restacplx(v[j], w[j])
            j += 1

        return res

    return 'Inconsistente: El tamaño de las matrices o los vectores no es igual'


#Inverso aditivo de un vector
def inverso (v):
    '''Función que retorna el inverso aditivo de un vector
       (list) --> list'''
    lon = len(v)
    res = [(0, 0) for i in range(lon)]
    j = 0
    while j < lon:
        res[j] = lc.multiplicacioncplx((-1, 0), v[j])
        j += 1
    return res


#Multiplicacion de un escalar por un vector complejo
def multiplicacionEscalar (num, v):
    '''Función que retorna la multiplicación entre un número complejo
       y un vector
       (tuple, list) --> list'''
    lon = len(v)
    res = [(0, 0) for i in range(lon)]
    j = 0
    while j < lon:
        res[j] = lc.multiplicacioncplx(num, v[j])
        j += 1
    return res


#Adicion de matrices complejas
def sumaMatrices (v, w):
    '''Función que retorna la suma entre dos matrices
           (list 2D, list 2D) --> list 2D'''
    if verificacion(v, w) == True and verificacion(v[0], w[0]) == True:
        filas = len(v)
        j = 0
        res = [[] for i in range(filas)]

        while j < filas:
            res[j] = sumavec(v[j], w[j])
            j += 1

        return res

    return 'Inconsistente: El tamaño de las matrices o los vectores no es igual'


#Resta de matrices complejas
def restaMatrices (v, w):
    '''Función que retorna la suma entre dos matrices
           (list 2D, list 2D) --> list 2D'''
    if verificacion(v, w) == True and verificacion(v[0], w[0]) == True:
        filas = len(v)
        j = 0
        res = [[] for i in range(filas)]

        while j < filas:
            res[j] = restavec(v[j], w[j])
            j += 1

        return res

    return 'Inconsistente: El tamaño de las matrices o los vectores no es igual'


#Inverso aditivo de una matriz compleja
def inversoMatrices (v):
    '''Función que retorna el inverso aditivo de una matriz
       (list 2D) --> list 2D'''
    filas = len(v)
    j = 0
    res = [[] for i in range(filas)]

    while j < filas:
        res[j] = inverso(v[j])
        j += 1

    return res


#Multiplicación de un escalar por una matriz compleja
def multEscalarMatrices(num, v):
    '''Función que retorna la multiplicaion entre un número complejo y
       una matriz
       (tuple, list 2D) --> list 2D'''
    filas = len(v)
    j = 0
    res = [[] for i in range(filas)]

    while j < filas:
        res[j] = multiplicacionEscalar(num, v[j])
        j += 1

    return res

#Transpuesta de una matriz/vector
def transpuesta (v):
    '''Función que retorna la transpuesta de un vector o una matriz
        (list) --> list'''
    res = []

    for k in range(len(v[0])):
        res.append([])
        for j in range(len(v)):
            res[k].append(v[j][k])

    return res


#Conjugado de una matriz/vector
def conjugadoMatVec(v):
    '''Función que retorna el conjugado de un vector o una matriz
       (list) --> list'''
    filas = [(0, 0)] * len(v[0])
    res = [filas] * len(v)

    for j in range(len(v)):
        filas = [(0, 0)] * len(v[0])
        res[j] = filas

        for k in range(len(v[0])):
            res[j][k] = lc.conjugado(v[j][k])

    return res


#Adjunta (daga) de una matriz/vector
def adjunta(v):
    '''Función que retorna la adjunta de un vector o una matriz
        (list) --> list'''

    return transpuesta(conjugadoMatVec(v))

if __name__ == '__main__':
    print(sumavec([(0,3), (0,0), (2,8)], [(1,1), (2,1), (0,1)]))
    #[(0,3), (0,0), (2,8)] + [(1,1), (2,1), (0,1)] = [(1,4), (2,1), (2,9)]
    print(restavec([(0, 3), (0, 0), (2, 8)], [(1, 1), (2, 1), (0, 1)]))
    #[(-1, 2), (-2, -1), (2, 7)]
    print(inverso([(0,3), (0,0), (2,8)]))
    #[(0, -3), (0, 0), (-2, -8)]
    print(multiplicacionEscalar((1,2), [(0,3), (0,0), (2,8)]))
    #[(-6, 3), (0, 0), (-14, 12)]
    print(sumaMatrices([[(0,2), (0,1)], [(1,2), (2,4)]], [[(1,0), (1,1)], [(8,0), (0,0)]]))
    #[[(1, 2), (1, 2)], [(9, 2), (2, 4)]]
    print(restaMatrices([[(0, 2), (0, 1)], [(1, 2), (2, 4)]], [[(1, 0), (1, 1)], [(8, 0), (0, 0)]]))
    #[[(-1, 2), (-1, 0)], [(-7, 2), (2, 4)]]
    print(inversoMatrices([[(0,2), (0,1)], [(1,2), (2,4)]]))
    #[[(0, -2), (0, -1)], [(-1, -2), (-2, -4)]]
    print(multEscalarMatrices((1,2), [[(0,3), (0,0), (2,8)], [(0,3), (0,0), (2,8)]]))
    #[[(-6, 3), (0, 0), (-14, 12)], [(-6, 3), (0, 0), (-14, 12)]]
    print(transpuesta([[(0,2), (0,1)], [(1,2), (2,4)]]))
    #[[(0, 2), (1, 2)], [(0, 1), (2, 4)]]
    print(conjugadoMatVec([[(0,2), (0,1)], [(1,2), (2,4)]]))
    #[[(0, -2), (0, -1)], [(1, -2), (2, -4)]]
    print(adjunta([[(0,2), (0,1)], [(1,2), (2,4)]]))
    #[[(0, -2), (1, -2)], [(0, -1), (2, -4)]]
    print(transpuesta([[(0,2), (0,1)], [(1,2), (2,4)]]))