#leer 4 números y decir cuántos son pares y cuantos impares y devolver la sumatoria de los pares.

# Inicializar contadores y variables
num_pares = 0    # contador par
num_impares = 0  # contador impar
total_pares = 0  # acumulador

# Leer 4 números:
for i in range(4):
    num = int(input("Introduzca un número: "))
    
    # Verificar si el número es par o impar:
    if (num // 2) * 2 == num:
        num_pares += 1  
        total_pares += num 
    else:
        num_impares += 1 

# Mostrar los resultados:
print("Los números pares son:", num_pares)
print("Los números impares son:", num_impares)
print("La sumatoria de todos los números pares es:", total_pares)

#----------------------#

