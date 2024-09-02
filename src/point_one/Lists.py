class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class LSL:
    def __init__(self):
        self.cabecera = None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabecera is None:
            self.cabecera = nuevo_nodo # Primer nodo
        else:
            nodo_actual = self.cabecera
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente # Asignas Espacio de memoria
            nodo_actual.siguiente = nuevo_nodo # Reemplazar nuevo nodo en el espacio disponible de memoria           

    def intercambio(self, nodo_1, nodo_2):
        nodo_1, nodo_2 = self.get_nodo(nodo_1), self.get_nodo(nodo_2)
        nodo_1.valor, nodo_2.valor = nodo_2.valor, nodo_1.valor

    def get_nodo(self, nodo):             
        nodo_actual = self.cabecera
        for i in range(1, self.obtener_tamano()+1):
            if i == nodo:
                return nodo_actual
            nodo_actual = nodo_actual.siguiente
            
    def obtener_tamano(self):
        nodo_actual = self.cabecera
        tamaño = 0
        while nodo_actual:
            tamaño += 1
            nodo_actual = nodo_actual.siguiente
        return tamaño            

    def imprimir(self):
        if self.cabecera is None:
            print("La LSL está vacía")
        else:
            nodo_actual = self.cabecera
            while nodo_actual:
                print(nodo_actual.valor, end=" -> ")
                nodo_actual = nodo_actual.siguiente
            print("Null")
            
    def concatenar_listas(self, lista_2):
        lista_3 = LSL()
        nodo_actual = self.cabecera
        nodo_actual2 = lista_2.cabecera
        
        while nodo_actual:
            lista_3.insertar(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente # Primera lista
        while nodo_actual2:
            lista_3.insertar(nodo_actual2.valor)
            nodo_actual2 = nodo_actual2.siguiente # Segunda lista

        return lista_3

    def ordenar(self):
        if self.cabecera is None or self.cabecera.siguiente is None:
            return

        nodo_actual = self.cabecera

        while nodo_actual:
            nodo_comparar = nodo_actual.siguiente
            while nodo_comparar:
                if nodo_actual.valor > nodo_comparar.valor:
                    nodo_actual.valor, nodo_comparar.valor = nodo_comparar.valor, nodo_actual.valor
                nodo_comparar = nodo_comparar.siguiente
            nodo_actual = nodo_actual.siguiente
