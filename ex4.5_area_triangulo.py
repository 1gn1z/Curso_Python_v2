'''
Ejercicio 4.5: Calcular el área de un triángulo dadas la base y la altura
'''

base = float(input('Digite la base: '))
altura = float(input('Digite la altura: '))

area = (base * altura) /2
print(area)

# Vamos a intentar usar una función:

def area_triangulo(base, altura):
    area = base * altura / 2
    return area

base = float(input('Digite la base: '))
altura = float(input('Digite la altura: '))

area_total = area_triangulo(base, altura)
print(f'El área del triángulo es igual a {area_total}')