# Realice un programa que contengan funciones de los tres tipos de triángulos. Los mismos deben estar acompañados de los mensajes respecto a la función decoradora.   Para mejorarlo pueden agregar los nombres de cada función según los triángulos.

def calcular_area_triangulo_equilatero(lado):
    area = (lado ** 2) * (3 ** 0.5) / 4
    return area

def calcular_perimetro_triangulo_equilatero(lado):
    perimetro = 3 * lado
    return perimetro

def calcular_area_triangulo_isosceles(base, lado):
    altura = (lado ** 2 - (base / 2) ** 2) ** 0.5
    area = (base * altura) / 2
    return area

def calcular_perimetro_triangulo_isosceles(base, lado):
    perimetro = base + 2 * lado
    return perimetro

def calcular_area_triangulo_escaleno(lado1, lado2, lado3):
    semiperimetro = (lado1 + lado2 + lado3) / 2
    area = (semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3)) ** 0.5
    return area

def calcular_perimetro_triangulo_escaleno(lado1, lado2, lado3):
    perimetro = lado1 + lado2 + lado3
    return perimetro

def mostrar_resultado(nombre_funcion, resultado):
    print(f"{nombre_funcion}: {resultado}")

lado1 = float(input("Ingrese el primer lado del triángulo: "))
lado2 = float(input("Ingrese el segundo lado del triángulo: "))
lado3 = float(input("Ingrese el tercer lado del triángulo: "))

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Los lados deben ser mayores que cero.")
else:
    if lado1 == lado2 == lado3:
        mostrar_resultado("Triángulo Equilátero - Área", calcular_area_triangulo_equilatero(lado1))
        mostrar_resultado("Triángulo Equilátero - Perímetro", calcular_perimetro_triangulo_equilatero(lado1))
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        mostrar_resultado("Triángulo Isósceles - Área", calcular_area_triangulo_isosceles(lado1, lado2))
        mostrar_resultado("Triángulo Isósceles - Perímetro", calcular_perimetro_triangulo_isosceles(lado1, lado2))
    else:
        mostrar_resultado("Triángulo Escaleno - Área", calcular_area_triangulo_escaleno(lado1, lado2, lado3))
        mostrar_resultado("Triángulo Escaleno - Perímetro", calcular_perimetro_triangulo_escaleno(lado1, lado2, lado3))
#----------------------#