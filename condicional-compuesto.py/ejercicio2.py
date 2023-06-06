#Ejercicios estructura condicional compuesto (IF anidados). Realice un programa que le permita al usuario simular el pago ingresando el importe y la forma de pago:
#• Contado (1): se aplica un descuento del 10% al importe
#• Tarjeta (2): se aplica un interés de 10%
#• Débito (3): se aplica un descuento del 5%
#Mostrar el importe, el descuento o interés y el importe total.
# Solicitar el importe y la forma de pago del usuario:
importe = float(input("Introduce el importe a pagar: "))
forma_pago = int(input("Selecciona la forma de pago: \n1. Contado \n2. Tarjeta \n3. Débito \n"))

# Realizar el descuento o interés y el importe total
if forma_pago == 1:
    descuento_contado = importe * 0.1
    importe_total = importe - descuento_contado
    print("Forma de pago: Contado")
    print("Descuento por pago de contado: $", descuento_contado)
    print("Importe total a pagar: $", importe_total)
elif forma_pago == 2:
    interes = importe * 0.1
    importe_total = importe + interes
    print("Forma de pago: Tarjeta")
    print("Interés por pago con tarjeta: $", interes)
    print("Importe total a pagar: $", importe_total)
elif forma_pago == 3:
    descuento_debito = importe * 0.05
    importe_total = importe - descuento_debito
    print("Forma de pago: Débito")
    print("Descuento por pago con débito: $", descuento_debito)
    print("Importe total a pagar: $", importe_total)
else:
    print("Forma de pago inexistente! Por favor, elija una opción válida: 1, 2 o 3.")

#----------------------#