# Realice un programa que contenga una función que se llame “sumayresta”, que la misma contenga dos variables locales nombradas suma y resta, respectivamente. Recuerda: en estos ejercicios trabajamos argumentos para este ejercicio sería dos.
def sumayresta(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

def procedimiento():
    num1 = float(input("Ingresar primer número: "))
    num2 = float(input("Ingresar segundo número: "))

    resultado_suma, resultado_resta = sumayresta(num1, num2)

    print("La suma es:", resultado_suma)
    print("La resta es:", resultado_resta)

procedimiento()
#----------------------#