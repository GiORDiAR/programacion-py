# Realizar un programa en Python que conste de la conversión de centímetros a metros, milímetros y pulgadas. El mismo debe permitirle al usuario el ingreso del número a convertir en el tipo de dato que se considere correspondiente y con un mensaje que justifique cada conversión mostrándolo por pantalla. Pueden consultar en internet las equivalencias para la conversión a realizar. Los nombres de las variables y de las funciones a cargar quedan a criterio del estudiante que está en examen. 

def conversion_centimetros():
    centimetros = float(input("Ingrese la longitud en centímetros: "))

    # lo paso a metros
    metros = centimetros / 100
    print(f"{centimetros} centímetros equivale a {metros} metros.")

    # utilizo un bucle for para pasar a milímetros
    milimetros = 0
    for i in range(int(centimetros)):
        milimetros += 10
    print(f"{centimetros} centímetros equivale a {milimetros} milímetros.")

    # utilizo un bucle while para pasar a pulgadas
    pulgadas = 0
    while centimetros >= 2.54:
        pulgadas += 1
        centimetros -= 2.54
    print(f"{centimetros} centímetros equivale a {pulgadas} pulgadas.")

conversion_centimetros()
#----------------------#