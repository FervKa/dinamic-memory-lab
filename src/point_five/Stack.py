class Stack:
    def __init__(self, n):
        self.stack_list = [None] * n
        self.top = -1

    def empty_stack(self):
        if self.top == -1:
            print("The stack is empty!")
            return True

    def full_stack(self):
        if self.top == len(self.stack_list) - 1:
            return True

    def stack_item(self, value):
        if self.full_stack():
            print(f"The Stack is full! Cannot add the value: {value}")
            return
        else:
            self.top += 1
            self.stack_list[self.top] = value

    def unstack(self):
        if self.empty_stack():
            return
        else:
            value_to_delete = self.stack_list.pop(self.top)
            self.top -= 1
            return value_to_delete

    def show_stack(self):
        print(f"The stack container is: {self.stack_list}")
