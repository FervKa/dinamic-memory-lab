class Queue:
    def __init__(self, n):
        self.capacity = n
        self.queue_list = []

    def empty_queue(self):
        return len(self.queue_list) == 0

    def full_queue(self):
        return len(self.queue_list) == self.capacity

    def enqueue(self, value):
        if self.full_queue():
            print(f"The Queue is full! Cannot add the value: {value}")
            return
        else:
            new_queue = self.queue_list + [value]
            self.queue_list[:] = new_queue

    def dequeue(self):
        if self.empty_queue():
            print("The queue is empty!")
            return []
        else:
            first_deleted = self.queue_list[0]
            new_queue = self.queue_list[1:]
            self.queue_list[:] = new_queue
            return self.queue_list, first_deleted

    def show_queue(self):
        if self.empty_queue():
            print("The queue is empty!")
        else:
            vector = []
            for x in self.queue_list:
                vector.append(x)
            return vector