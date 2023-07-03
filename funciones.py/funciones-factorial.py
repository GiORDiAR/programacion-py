#Calcula el factorial de un número
def factorial(numero):
    resultado=1
    for i in range (1,numero+1):
        resultado=resultado*i 
        print("El número de iteración es:", i ,"por ende el resultado es:", resultado)  
    return resultado
factorial(6)

#este seria un ejemplo de factorial 3!=3x2x1
#----------------------#