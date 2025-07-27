from inputs import Inputs

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        place = int(input("Enter the position of the item to dequeue 'f' for first item or 'l' for last item: "))
        if not self.is_empty():
            if place == 'f':
                return self.items.pop(0)
            elif place == 'l':
                return self.items.pop(-1)
            else:
                return "Invalid Position! Enter input from 'f' or 'l'."
        else:
            return "Queue is empty!"
            
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "Queue is empty"
    
    def is_empty(self):
        return len(self.items) == 0

    
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            for item in self.items:
                print(f"{item}")
        

class QueueOperations(Queue):
    def run(self):
        q = Queue()  
        while True:
            choice = Inputs.choice_queue()
            if len(choice) == 1:
                if choice in ['1']:
                    try:    
                        item = input("Enter the number you want to enqueue: ")
                        q.enqueue(item)
                        print(f"Item {item} successfully enqueued in Queue")
                    except ValueError:
                        print("Enter a valid item to enqueue!")
                    except Exception as e:
                        print(f"Error: {e}")
                elif choice in ['2']:
                    print(f"Item dequeued: {q.dequeue(item)}")
                    f"Current Queue: \n{q.display()}"
                elif choice in ['3']:
                    print(f"First Item: {q.peek()}")
                elif choice in ['4']:
                    print(f"Queue content:")    
                    q.display()
                elif choice in ['5']:
                    print("Exiting...")
                    break
