# cambiar pesos a dólares, y que sea el usuario quién decida qué tipo de cambio quiere, si de dólares a pesos o viceversa:

cambio=float(input("Valor por cada dolar: "))
pesos=int(input("Ingrese cantidad de pesos: "))

dolares=pesos / cambio

if dolares==0:
    print("Me quedo en pesos.")
elif dolares>1:
    print("Cambio a dolares.")
else:
    print("No cambio nada.")

#----------------------#