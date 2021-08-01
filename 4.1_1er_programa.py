def sumar(a, b):
    suma = a + b
    return suma

numero_1 = int(input('Ingrese el primer número: '))
numero_2 = int(input('Ingrese el segundo número: '))

# resultado = sumar(numero_1 + numero_2) 
# 
# MAL!, los números en este caso van separados por una COMA por que son los parametros que pide la funcion, NO van sumados como esta línea.

resultado = sumar(numero_1, numero_2)

print(f'La suma de {numero_1} y {numero_2} es igual a {resultado}')
#print('La suma de {} y {} es igual a {}'.format(numero_1, numero_2, resultado))

# Prueba para checar git.