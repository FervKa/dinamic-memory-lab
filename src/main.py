# This file is for testing all the exercices!
# Here are all the proposed cases.
from point_four.Pilas import Pila
from commons import separator_string, cases_string
from point_five.Stack import Stack
from point_five.Queue import Queue
from point_five.Stack_with_queue import Stack_with_Queue



# Prueba 1:
# Lista = [2, 7, 9, 5, 7, 5]
# Colocar la función principal para solucionar y la respuesta generada
separator_string('Fourth exercise')
pila = Pila(6)
lista = [2, 7, 9, 5, 7, 5]
pila.ApilarLista(lista)
pila.Mostrar() 
pila.DesapilarLista()
pila.Mostrar()



separator_string('Fifth  exercise')
cases_string([10, 11, 12, 13, 14, 15])
stack_queue_capacity = 6
stack_queue = Stack_with_Queue(stack_queue_capacity, Queue)
stack_queue.stack(10)
stack_queue.stack(11)
stack_queue.stack(12)
stack_queue.stack(13)
stack_queue.stack(14)
stack_queue.stack(15)
stack_queue.show_stack_queue()
stack_queue.unstack_stack_with_queue()
stack_queue.show_stack_queue()

cases_string([1, 2, 3, 4, 5, 6])
stack_queue_capacity_test_2 = 6
stack_queue_test_2 = Stack_with_Queue(stack_queue_capacity_test_2, Queue)
stack_queue_test_2.stack(1)
stack_queue_test_2.stack(2)
stack_queue_test_2.stack(3)
stack_queue_test_2.stack(4)
stack_queue_test_2.stack(5)
stack_queue_test_2.stack(6)
stack_queue_test_2.show_stack_queue()
stack_queue_test_2.unstack_stack_with_queue()
stack_queue_test_2.show_stack_queue()


cases_string([50, 40, 30, 20, 10, 0])
stack_queue_capacity_test_3 = 6
stack_queue_test_3 = Stack_with_Queue(stack_queue_capacity_test_3, Queue)
stack_queue_test_3.stack(50)
stack_queue_test_3.stack(40)
stack_queue_test_3.stack(30)
stack_queue_test_3.stack(20)
stack_queue_test_3.stack(10)
stack_queue_test_3.stack(0)
stack_queue_test_3.show_stack_queue()
stack_queue_test_3.unstack_stack_with_queue()
stack_queue_test_3.show_stack_queue()
