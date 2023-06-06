# Leer 10 números y mostrar solamente los números positivos, y su sumatoria:
suma_positivos = 0

for i in range(1, 11):
    num = int(input(f"Ingrese el número {i}: "))
    
    if num > 0:
        print(num)
        suma_positivos += num

print("Sumatoria de números positivos:", suma_positivos)

#----------------------#