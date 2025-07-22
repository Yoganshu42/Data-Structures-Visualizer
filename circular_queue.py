queue = [input("Enter the size of the Queue: ")]

class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.queue = [None]*size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if len(self.items) == self.size:
            print("FULL!!")
        else:
            return "Queue isn't full!"         

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty!"
            
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "Queue is empty"
    
    def is_empty(self):
        return len(self.items) == 0
    
    def is_full(self):
        if len(self.items) == self.size:
            print("FULL!!")
        else:
            return "Queue isn't full!"

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            for item in self.items:
                print(f"{item}")
