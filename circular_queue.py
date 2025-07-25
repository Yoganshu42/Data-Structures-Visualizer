from inputs import Inputs

class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.queue = [None]*size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear+1) % self.size == self.front
    
    def enqueue(self,item):
        if self.is_full():
            print("Queue is Full! Cannot Enqueue.")
            return
        
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = item
        print(f"Enqueued {item}")

    def dequeue(self):
        if self.is_empty():
           print("Queue is Empty! Nothing to dequeue.")
           return None

        removed_item = self.queue[self.front]
        self.queue[self.front] = None
        
        if self.rear == self.front:
            self.rear = -1
            self.front = -1
        else:
            self.front = (self.front + 1) % self.size
        
        print(f"Dequeued:{removed_item}")
        return removed_item
            
    def peek(self):
        if self.is_empty():
           print("Queue is Empty!")
           return None
        else: 
            print("Front item: ") 
            return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            i = self.front
            while True:
                print(self.queue[i])
                if i == self.rear:
                    break
                i = (i+1)%self.size


class CircularQueueOperations:
    def run(self):
        try:
            size = int(input("Enter the size of the Queue: "))
        except Exception:
            return "Size can only be a positive integer"
        
        cq = CircularQueue(size)         

        while True:
            choice = Inputs.choice_queue()
            if len(choice) == 1:
                if choice in ['1']:
                    try:    
                        item = input("Enter the number you want to enqueue: ")
                        cq.enqueue(item)
                    except ValueError:
                        print("Enter a valid item to enqueue!")
                    except Exception as e:
                        print(f"Error: {e}")
                elif choice in ['2']:
                    print(f"Item dequeued: {cq.dequeue()}")
                    print("Current Queue: ") 
                    cq.display()
                elif choice in ['3']:
                    print(cq.peek())
                elif choice in ['4']:
                    print(f"Queue content:")    
                    cq.display()
                elif choice in ['5']:
                    print("Exiting...")
                    break
