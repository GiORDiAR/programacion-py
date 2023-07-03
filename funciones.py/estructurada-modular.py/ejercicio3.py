# Realizar un programa de funciones que contengan 3 parámetros, el cual derive en una suma. Mostrar el resultado dos veces.
def suma(a, b, c):
    resultado = a + b + c
    return resultado

def procedimiento():
    # Ingresar los valores para los parámetros
    num1 = int(input("Ingresar primer número: "))
    num2 = int(input("Ingresar segundo número: "))
    num3 = int(input("Ingresar tercer número: "))

    # Llamar a la función suma() y obtener el resultado
    total_suma = suma(num1, num2, num3)

    # Mostrar el resultado dos veces
    print("La suma total es:", total_suma)
    print("La suma total es:", total_suma)
  
procedimiento()
#----------------------#