# Realice un programa que contenga una función que se llame “conversion”, que la misma contenga tres parámetros. Se pide convertir los segundos ingresados en horas, minutos y segundos.
def conversion(seg):
    hs = seg // 3600
    min = (seg % 3600) // 60
    seg = (seg % 3600) % 60

    return hs, min, seg

seg_totales = int(input("Ingrese la cantidad total de segundos: "))

hs, min, seg = conversion(seg_totales)

print("Horas:", hs, "Minutos:", min, "Segundos:", seg)
#----------------------#