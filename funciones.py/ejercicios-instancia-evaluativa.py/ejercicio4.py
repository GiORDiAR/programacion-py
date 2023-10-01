# Escribir una función que convierta un número decimal en los otros dos sistemas: Binario y Hexadecimal. Mostrar mensajes pertenecientes a cada función.
def dec_a_bin(decimal):
    binario = bin(decimal)
    return binario

def dec_a_hexa(decimal):
    hexadecimal = hex(decimal)
    return hexadecimal

def procedimiento():
    decimal = int(input("Ingresar número decimal: "))

    binario = dec_a_bin(decimal)
    print("El número en binario es:", binario)

    hexadecimal = dec_a_hexa(decimal)
    print("El número en hexadecimal es:", hexadecimal)

procedimiento()
#----------------------#