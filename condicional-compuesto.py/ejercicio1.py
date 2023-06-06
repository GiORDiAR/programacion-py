#Introducir los lados de un triángulo y visualizar por pantalla si dicho triángulo es equilátero, isósceles o escaleno:

lado1 = float(input("Introducir primer lado: "))
lado2 = float(input("Introducir segundo lado: "))
lado3 = float(input("Introducir tercer lado: "))

if lado1 == lado2 == lado3:
    print("El triangulo es equilatero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triangulo es isósceles.")
else:
    print("El triangulo es escaleno.")

#----------------------#