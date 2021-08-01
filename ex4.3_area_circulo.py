'''
Ejercicio 4.3: Solicitar al usuario el radio de un círculo y calcular su área.
Fórmula: π * r2
'''
import math

radio = int(input('Ingrese el radio del círculo: '))

#area = 3.1416 * radio ** 2
area = math.pi * radio ** 2
print('El area es igual a: ', area)

dos_decimales = round(area, 2)
print('El area es igual a: ', dos_decimales)
