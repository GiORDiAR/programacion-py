# Pedir un número del 1 al 7 y decir el día de la semana correspondiente.
# Solicitar al usuario un número entre el 1 al 7:
num = int(input("Introduce un número del 1 al 7: "))

# Verificar a que día de la semana corresponde:
if num == 1:
    dia = "Lunes"
elif num == 2:
    dia = "Martes"
elif num == 3:
    dia = "Miércoles"
elif num == 4:
    dia = "Jueves"
elif num == 5:
    dia = "Viernes"
elif num == 6:
    dia = "Sábado"
elif num == 7:
    dia = "Domingo"
else:
    dia = "parámetro no encontrado! Introduzca por favor un número del 1 al 7"

# Mostrar a que día de la semana corresponde:
print("El número", num, "corresponde al día:", dia, "de la semana.")

#----------------------#