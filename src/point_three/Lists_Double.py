class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None


class LDL:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def encolar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:  # Si la lista está vacía
            self.cabeza = self.cola = nuevo_nodo
        else:  # Si la lista ya tiene elementos
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

    def mostrar(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(
                nodo_actual.valor,
                end=" <-> " if nodo_actual.siguiente else " <-> NULL\n",
            )
            nodo_actual = nodo_actual.siguiente


# Explicación:
# •	Encolar un nodo: Cada vez que se llama al método encolar, se crea un nuevo nodo con
# el valor proporcionado. Si la lista está vacía, este nodo se convierte en la cabeza y la cola.
# Si ya existen nodos en la lista, el nuevo nodo se enlaza al final y la cola se actualiza para
# que apunte a este nuevo nodo.

# •	Mostrar la lista: Después de encolar los nodos, se recorre la lista desde la cabeza hasta
# la cola, imprimiendo los valores en el orden FIFO.
