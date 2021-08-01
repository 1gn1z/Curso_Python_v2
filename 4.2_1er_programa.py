# Igual que el primer programa pero para que sume números reales (decimales)

def sumar(num1, num2):
    suma = num1 + num2
    return suma

numero_1 = float(input('Ingrese el primer número: '))
numero_2 = float(input('Ingrese el segundo número: '))

resultado = sumar(numero_1, numero_2)

print(f'La suma de {numero_1} y {numero_2} es igual a {resultado}')
