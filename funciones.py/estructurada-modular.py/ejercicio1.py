# Muestre el mensaje “Hola Aula X (Indicar el número de aula a la que pertenecen), ¿Qué tal?” en tres veces intercambiados entre ellos otro mensajes a su elección.
def saludo(aula):
    print("Hola Aula", aula + ", ¿Qué tal?")

def cambiar_mensajes():
    msj1 = "¡Bienvenidos a la clase!"
    msj2 = "¡Hoy aprenderemos sobre funciones en Python!"
    msj3 = "La lección de hoy es funciones estructurada y modular."

    print(msj1)
    print(msj2)
    print(msj3)

def procedimiento():
    aula = input("Ingresar número de aula: ")
    aula = str(aula)

    for _ in range(3):
        saludo(aula)
        cambiar_mensajes()
        print()  # Entre cada iteración agrega una línea en blanco

procedimiento()
#----------------------#