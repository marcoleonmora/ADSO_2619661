"""
PROGRAMA 02: Numeros primos.
Determinar si un numero es primo
Ejecicios grupo ADO
"""

while True:
    # 1. leer el numero n
    print('----- NUMEROS PRIMOS ----')
    numero = int(input('Ingrese un entero mayor a 0: '))
    if numero == 0:
        break
    
    # 2. verificar si es primo
    resultado = 'SI es primo'

    for x in range(2, numero):
        if (numero % x) == 0:
            resultado = ' NO es primo'

    print('El numero', numero, resultado)

print('Terminado...')
