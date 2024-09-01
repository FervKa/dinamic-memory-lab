# Diseño del algoritmo
# //
class Pila:
    def __init__(self, n):
        self.V = [None] * n  # Inicializa la pila con tamaño n
        self.Vdes = []  # Lista para almacenar los elementos desapilados
        self.cima = -1  # Indica que la pila está vacía al inicio

    def pilaVacia(self):
        return self.cima == -1

    def PilaLlena(self):
        return self.cima == len(self.V) - 1

    def Apilar(self, valor):
        if self.PilaLlena():
            print("Pila llena")
        else:
            self.cima += 1
            self.V[self.cima] = valor

    def Desapilar(self):
        if self.pilaVacia():
            print("Pila vacía")
            return None
        else:
            valor_Eliminar = self.V.pop(self.cima)
            self.cima -= 1
            self.Vdes.append(valor_Eliminar)
            return valor_Eliminar

    def ApilarLista(self, l):
        self.V = [None] * len(l)
        self.Vdes = []
        for valor in l:
            self.Apilar(valor)

    def DesapilarLista(self):
        self.Vdes = []
        while not self.pilaVacia():
            self.Desapilar()

    def Mostrar(self):
        print("Pila actual:", self.V[:self.cima + 1])
        print("Elementos desapilados:", self.Vdes) 

# //