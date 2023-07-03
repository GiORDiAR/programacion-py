# Realice un programa que lea dos números (dos parámetros), compare si son IGUALES, en ese caso, mostrar un mensaje que muestre TRUE. 
def comparar_num(num1, num2):
    if num1 == num2:
        return True
    else:
        return False

def procedimiento():
    num1 = int(input("Ingresar primer número: "))
    num2 = int(input("Ingresar segundo número: "))

    if comparar_num(num1, num2):
        print("TRUE")
    else:
        print("FALSE")

procedimiento()
#----------------------#