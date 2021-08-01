'''
Ejercicio 4.5: Calcular el área de un triángulo dadas la base y la altura


base = int(input('Digite la base: '))
altura = int(input('Digite la altura: '))

area = (base * altura) /2
print(area)
'''
# Vamos a intentar usar una función:

def area_triangulo(base, altura):
    area = base * altura / 2
    return area

base = int(input('Digite la base: '))
altura = int(input('Digite la altura: '))

area_total = area_triangulo(base, altura)
print(area_total)