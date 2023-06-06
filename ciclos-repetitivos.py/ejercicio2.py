# Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100, cuál es el número máximo y cuál es el número mínimo.
# Inicializar las variables:
num_mayores = 0
num_menores = 0
maximo = float('-inf')
minimo = float('inf')

# Leer 10 números:
for i in range(10):
    num = int(input("Ingrese un número: "))

    # Verificar si es mayor o menor a 100
    if num > 100:
        num_mayores += 1
    elif num < 100:
        num_menores += 1
    
    # Actualizar máximo y mínimo
    if num > maximo:
        maximo = num
    
    if num < minimo:
        minimo = num

# Imprimir resultados
print("Cantidad de números mayores a 100:", num_mayores)
print("Cantidad de números menores a 100:", num_menores)
print("Número máximo:", maximo)
print("Número mínimo:", minimo)

#----------------------#