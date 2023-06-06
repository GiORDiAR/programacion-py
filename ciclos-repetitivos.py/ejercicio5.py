# Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.
num_positivos = []

for i in range(1, 16):
    num = int(input(f"Ingrese un número negativo {i}: "))
    
    if num < 0:
        num *= -1  # Multiplicamos por -1 para cambiar el signo del número
        num_positivos.append(num)

print("Números positivos:")
for num_positivo in num_positivos:
    print(num_positivo)

#----------------------#