"""
PROGRAMA 01: Cuadrado de un numero
Ejecicios grupo ADO
"""

# ingresar numero
print('ELEVAR UN NUMERO AL CUADRADO')
strNum = input("Por favor, ingrese el numero..")
if strNum.isdigit():
    num = int(strNum)
    # elevar al cuadrado
    result = num * num
    # mostrar el resultado
    print('El cuadrado de', num, 'es', result) 
    print('El cuadrado de ' + str(num) + ' es ' + str(result))
    print()
    print('El cuadrado de {} es {}'.format(num, result))

else:
    print('No sea bruto, '+ strNum + ' no es un numero!')
