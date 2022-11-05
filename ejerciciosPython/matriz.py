"""
Problema 24. Recorridos en matrices Dada la matriz 7x7.
Poblarla con números generados al azar, entre 10 y 99.
"""
import random


# Crear la matriz
matriz = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
    ]

# poblarla
for x in range(len(matriz)):
    #recorrer elementos de una fila
    for y in range(len(matriz)):
        #generar numero al azar entre 10 y 99.
        matriz[x][y] = random.randrange(10, 99)
            

#mostrarla
for x in range(len(matriz)):
    print(matriz[x])


#MOSTRAR DIAGONAL PRINCIPAL
print()
print('----- DIAGONAL PRINCIPAL --------')
long = len(matriz)
for x in range(long):
    print('    ' * x, end="")
    print(matriz[x][x], end=", ")
    print()

    
#MOSTRAR DIAGONAL INVERSA
print()
print('----- DIAGONAL INVERSA --------')
for f in range(long):
    c = long- 1 - f
    print('    ' * c, end='')
    print(matriz[f][c], end=",")
    print()


#MOSTRAR SUPERIOR DERECHO
print()
print('----- MATRIZ SUPERIOR DERECHA --------')
for f in range(long):
    print('    ' * f, end='')
    for c in range(f, long):
        print(matriz[f][c], end=", ")
    print()


#MOSTRAR SUPERIOR IZQUIERDO
print()
print('----- MATRIZ SUPERIOR IZQUIERDA --------')
for f in range(long):
    for c in range(long - f):
        print(matriz[f][c], end=", ")
    print()


#MOSTRAR INFERIOR DERECHA
print()
print('----- MATRIZ INFERIOR DERECHA --------')
for f in range(long):
    print('    ' * (long- f-1), end= '')
    for c in range(long - f-1, long):
        print(matriz[f][c], end=", ")
    print()


#MOSTRAR INFERIOR IZQUIERDA
print()
print('----- MATRIZ INFERIOR IZQUIERDA --------')
for f in range(long):
    for c in range(f+1):
        print(matriz[f][c], end=", ")
    print()
    


    
