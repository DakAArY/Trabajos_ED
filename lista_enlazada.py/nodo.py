class Nodo:
    def __init__(self):
        self.dato = 0
        self.siguiente = None

    def asignarDato(self,dato):
        self.dato = dato

    def recuperarDato(self):
        print(self.dato)

    def obtenerDato(self):
        return self.dato