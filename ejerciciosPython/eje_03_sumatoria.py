"""
algoritmo que calcule la sumatoria de los números enteros
pares comprendidos entre 1 y 100.
El Programa deberá mostrar los números.
eje_03_sumatoria
"""
print("""sumatoria de los números
enteros pares comprendidos
entre 1 y 100""")

suma = 0


for x in range(1, 101):
    if (x % 2) == 0:
        suma += x
        print(x, end = ', ')

print()
print('la sumatoria es ', suma)
