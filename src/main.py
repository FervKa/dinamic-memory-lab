# This file is for testing all the exercices!
# Here are all the proposed cases.
import random
from point_four.Pilas import Pila
from commons import separator_string, cases_string
from point_five.Queue import Queue
from point_five.Stack_with_queue import Stack_with_Queue
from point_one.Lists import LSL
from point_two.Lists_Double import LDL
from point_three.Lists_Double import LDL as second_LDL



separator_string("First exercise")

lista_1 = LSL()
lista_2 = LSL()
lista_3 = LSL()

for valor in range (0, 20):
    lista_1.insertar(random.randint(1, 50))
    lista_2.insertar(random.randint(1, 50))

lista_3 = lista_1.concatenar_listas(lista_2)

cases_string("lista 1")
lista_1.imprimir()
cases_string("lista 2")
lista_2.imprimir()
cases_string("lista 3")
lista_3.imprimir()

lista_3.ordenar()
cases_string("lista 3 ordenada")
lista_3.imprimir()

separator_string("Second exercise")
cases_string("Test 1")
# Prueba 1:
Lista = LDL()
Lista.insertar(10)
Lista.insertar(8)
Lista.insertar(8)
Lista.insertar(8)
Lista.insertar(9)

Lista.ordenar_y_mostrar(ascendente=True)
Lista.ordenar_y_mostrar(ascendente=False)

cases_string("Test 2")
# Prueba 2:
Lista = LDL()
Lista.insertar(1)
Lista.insertar(1)
Lista.insertar(1)
Lista.insertar(1)
Lista.insertar(1)

Lista.ordenar_y_mostrar(ascendente=True)
Lista.ordenar_y_mostrar(ascendente=False)

cases_string("Test 3")
# Prueba 3:
Lista = LDL()
Lista.insertar(8)
Lista.insertar(7)
Lista.insertar(6)
Lista.insertar(-4)
Lista.insertar(-4)
Lista.insertar(-3)
Lista.insertar(-2)
Lista.insertar(-1)

Lista.ordenar_y_mostrar(ascendente=True)
Lista.ordenar_y_mostrar(ascendente=False)

separator_string("Third exercise")
cases_string("Test 1")
# Prueba 1:
Lista = second_LDL()
Lista.encolar(1)
Lista.encolar(5)
Lista.encolar(6)
Lista.encolar(9)
Lista.encolar(10)
Lista.mostrar()
# Respuesta esperada: 1 <-> 5 <-> 6 <-> 9 <-> 10 <-> NULL

cases_string("Test 3")
#Prueba adicional
Lista = second_LDL()
Lista.encolar(3)
Lista.encolar(4)
Lista.mostrar()

cases_string("Test 2")
# Prueba 2:
Lista = second_LDL()
Lista.encolar(8)
Lista.encolar(8)
Lista.encolar(10)
Lista.encolar(10)
Lista.encolar(20)
Lista.mostrar()
# Respuesta esperada: 8 <-> 8 <-> 10 <-> 10 <-> 20 <-> NULL

# Prueba 1:
# Lista = [2, 7, 9, 5, 7, 5]
# Colocar la función principal para solucionar y la respuesta generada
separator_string('Fourth exercise')
pila = Pila(6)
lista = [2, 7, 9, 5, 7, 5]
cases_string(lista)
pila.ApilarLista(lista)
pila.Mostrar()
pila.DesapilarLista()
pila.Mostrar()

lista_dos = [1, 1, 1, 1, 1, 1]
cases_string(lista_dos)
pila_dos = Pila(6)
pila_dos.ApilarLista(lista_dos)
pila_dos.Mostrar()
pila_dos.DesapilarLista()
pila_dos.Mostrar()

lista_tres = [5, 5, 7, 7, 1, 1]
cases_string(lista_tres)
pila_tres = Pila(6)
pila_tres.ApilarLista(lista_tres)
pila_tres.Mostrar()
pila_tres.DesapilarLista()
pila_tres.Mostrar()


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
stack_queue_test_2 = Stack_with_Queue(stack_queue_capacity, Queue)
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
stack_queue_test_3 = Stack_with_Queue(stack_queue_capacity, Queue)
stack_queue_test_3.stack(50)
stack_queue_test_3.stack(40)
stack_queue_test_3.stack(30)
stack_queue_test_3.stack(20)
stack_queue_test_3.stack(10)
stack_queue_test_3.stack(0)
stack_queue_test_3.show_stack_queue()
stack_queue_test_3.unstack_stack_with_queue()
stack_queue_test_3.show_stack_queue()
