from Stack import Stack
from Queue import Queue
from Stack_with_queue import Stack_with_Queue

""" print("Stack <--------------->")
stack_one = Stack(5)
stack_one.stack_item(2)
stack_one.stack_item(9)
stack_one.stack_item(6)
stack_one.stack_item(29)
stack_one.stack_item(23)
stack_one.stack_item(14)
stack_one.stack_item(28)
stack_one.stack_item(3)
stack_one.stack_item(5)
stack_one.show_stack()
stack_one.unstack()
stack_one.show_stack()


print("Queue <---------------->")
n = 5
queue_one = Queue(n)
queue_one.enqueue(2)
queue_one.enqueue(9)
queue_one.enqueue(6)
queue_one.enqueue(29)
queue_one.enqueue(23)
queue_one.enqueue(14)
queue_one.show_queue()
queue_one.dequeue()
queue_one.show_queue() """


print("Stack with Queue (Test 1) <--------------->")
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

print("Stack with Queue (Test 2) <--------------->")
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


print("Stack with Queue (Test 3) <--------------->")
stack_queue_capacity_test_3 = 6
stack_queue_test_3 = Stack_with_Queue(stack_queue_capacity_test_3, Queue)
stack_queue_test_3.stack(50)
stack_queue_test_3.stack(40)
stack_queue_test_3.stack(30)
stack_queue_test_3.stack(20)
stack_queue_test_3.stack(10)
stack_queue_test_3.stack(0)
stack_queue_test_3.show_stack_queue()
stack_queue_test_2.unstack_stack_with_queue()
stack_queue_test_3.show_stack_queue()


#Pilas -> LIFO
#Colas -> FIFO

# [50, 40, 30, 20, 10, 0]
# [0, 10, 20, 30, 40, 50]
