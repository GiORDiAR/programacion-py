# Introducir un número del 1 al 12 y diga el nombre del mes correspondiente.
# Solicitar un número entre el 1 al 12:
num = int(input("Introduzca un número del 1 al 12: "))

# Verificar a que mes corresponde:
if num == 1:
    mes = "Enero"
elif num == 2:
    mes = "Febrero"
elif num == 3:
    mes = "Marzo"
elif num == 4:
    mes = "Abril"
elif num == 5:
    mes = "Mayo"
elif num == 6:
    mes = "Junio"
elif num == 7:
    mes = "Julio"
elif num == 8:
    mes = "Agosto"
elif num == 9:
    mes = "Septiembre"
elif num == 10:
    mes = "Octubre"
elif num == 11:
    mes = "Noviembre"
elif num == 12:
    mes = "Diciembre"
else:
    mes = "parámetro no encontrado! El número debe ser del 1 al 12."

# Mostrar a que mes corresponde:
print("El número", num, "corresponde al mes de:", mes)

#----------------------#