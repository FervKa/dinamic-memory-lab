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
