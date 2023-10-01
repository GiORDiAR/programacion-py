#Realizar un programa de funciones que contengan funciones con bucles y control de flujo fuera de la función decoradora. Al menos se deben tener dos condicionales o bucles.

def es_par(numero):
    return numero % 2 == 0

def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial = factorial * i
    return factorial

numero = int(input("Ingrese un número entero: "))

if es_par(numero):
    print(str(numero) + " es un número par.")
else:
    print(str(numero) + " es un número impar.")

if numero >= 0:
    factorial = calcular_factorial(numero)
    print("El factorial de " + str(numero) + " es " + str(factorial) + ".")
else:
    print("No se puede calcular el factorial de un número negativo.")
#----------------------#