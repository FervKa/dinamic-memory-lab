class Stack_with_Queue:
    def __init__(self, n:int, Queue:object):
        self.queue_one = Queue(n)
        self.queue_two = Queue(n)

    def is_empty(self):
        return self.queue_one.empty_queue()
    
    def is_full(self):
        return self.queue_one.full_queue()

    def stack(self, value):
        if self.is_empty():
            self.queue_one.enqueue(value)
        else:
            while not self.queue_one.empty_queue():
                self.queue_two.enqueue(self.queue_one.dequeue()[1])
            self.queue_one.enqueue(value)
            while not self.queue_two.empty_queue():
                self.queue_one.enqueue(self.queue_two.dequeue()[1])

    def unstack_stack_with_queue(self):
        if self.is_empty():
            print("The stack is empty!")
            return
        return self.queue_one.dequeue()

    def show_stack_queue(self, get_array=False):
        if self.queue_one.empty_queue():
            print("The stack queue is empty!")
            return
        else:
            vector = []
            for x in self.queue_one.show_queue():
                vector.append(x)

            if not get_array: 
                print(f"The stack queue is: {vector}")
            else:
                return vector


# Explicación:
# La clase Stack_with_Queue utiliza dos colas para implementar una pila.
# La cola one se utiliza para almacenar los elementos de la pila, y la cola two 
# se utiliza para almacenar los elementos que se van a agregar a la pila.
# La función is_empty() verifica si la pila está vacía.
# La función is_full() verifica si la pila está llena.
# La función stack() agrega un elemento a la pila. -> Esta verifica en primera instancia si la
# cola one está vacía, si es así, agrega el elemento a la cola one, 
# si no, se desplazan todos los elementos de la cola one a la cola two
# y luego se agrega el elemento a la cola one en la primera posición. Luego,
# se desplazan todos los elementos de la cola two a la cola one en orden invertido, así, el primer
# elemento de la cola two es el último elemento de la cola one, por consiguiente, el primer elemento
# de la cola one es el último elemento agregado a la pila, manteniendo el FIFO de las colas..
# La función unstack_stack_with_queue() elimina el elemento superior de la pila.
# La función show_stack_queue() muestra los elementos de la pila.
