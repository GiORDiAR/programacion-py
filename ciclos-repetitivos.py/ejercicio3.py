# Ingresar las edades y el sexo de 15 personas y determinar cuántas son mujeres, cuántos varones, cuántos mayores de edad y cuántos menores de edad.
num_mujeres = 0
num_varones = 0
num_mayores_edad = 0
num_menores_edad = 0

for i in range(1, 16):
    print(f"Persona {i}:")
    edad = int(input("Ingrese la edad: "))
    sexo = input("Ingrese el sexo (M o F): ")

    if sexo.upper() == "F":
        num_mujeres += 1
    elif sexo.upper() == "M":
        num_varones += 1

    if edad >= 18:
        num_mayores_edad += 1
    else:
        num_menores_edad += 1

print("Resultados:")
print(f"Total de mujeres: {num_mujeres}")
print(f"Total de varones: {num_varones}")
print(f"Total de mayores de edad: {num_mayores_edad}")
print(f"Total de menores de edad: {num_menores_edad}")

#----------------------#