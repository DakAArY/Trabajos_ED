from nodo import Nodo
class listaEnlazada:
    def __init__(self):
        self.inicio = None

    def insertarDato(self, dato):
        nodoTemp = Nodo()
        nodoTemp.asignarDato(dato)
        nodoTemp.siguiente = self.inicio
        self.inicio = nodoTemp

    def mostrarElementos(self):
        if(self.inicio is None):
            print("No hay nada en la lista")
        else:
            nodoTemp = self.inicio
            dato = ""
            while(nodoTemp is not None):
                #nodoTemp.recuperarDato()
                dato += str(nodoTemp.obtenerDato()) + ","
                nodoTemp = nodoTemp.siguiente
            return dato
       
    def insertarDatoFinal(self, dato):
        nodoTemp = Nodo()
        nodoTemp.asignarDato(dato)
        nodoAux = self.inicio
        while(nodoAux.siguiente is not None):
            nodoAux = nodoAux.siguiente
        nodoAux.siguiente = nodoTemp
       
    def eliminarElemento(self):
        if(self.inicio is None):
            print("La lista esta vacia")
        else:
            temp = self.inicio
            print("El elemento a eliminar sera: ", temp.obtenerDato())
            self.inicio = temp.siguiente