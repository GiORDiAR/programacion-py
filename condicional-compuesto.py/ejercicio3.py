# Leer tres números, muestrar cuál es el mayor y determinar si es par o impar.
# Solicitar los tres números al usuario:
num1 = int(input("Ingresar el primer número: "))
num2 = int(input("Ingresar el segundo número: "))
num3 = int(input("Ingresar el tercer número: "))

# Obtener cuál es el número mayor:
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

print("El número mayor es:", mayor)

# Verificar si el número mayor es par o impar:
if (mayor // 2) * 2 == mayor:
    print("Y es un número par!", mayor)
else:
    print("Y es un número impar!", mayor)

#----------------------#