# Creamos la clase Lavadora
class Lavadora:

    def __init__(self):
        pass

    # Tiene un método publico lavar que referencia a otros métodos
    def lavar(self, temperatura='fría', marca='ariel', proceso='programa 4°', velocidad='120rpm'):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon(marca)
        self._lavar(proceso)
        self._centrifugar(velocidad)


    # Los métodos privados de la clase no son relevantes
    # para el uso desde afuera de la clase y por
    # convención se inicia con _

    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')


    def _anadir_jabon(self, marca):
        print(f'Añadiendo jabón de marca {marca}')


    def _lavar(self, proceso):
        print(f'Lavando la ropa en {proceso}')


    def _centrifugar(self, velocidad):
        print(f'Centrifugando la ropa a {velocidad}')


if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar() # Ejecutamos el método publico de nuestra instancia.
#----------------------#