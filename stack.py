from inputs import Inputs

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self, item):
        if not self.is_empty():
            return self.stack.pop(item)
        else:
            return "Stack Underflow"
            
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Empty Stack"
    
    def is_empty(self):
        return len(self.stack) == 0

    
    def display(self):
        for item in reversed(self.stack):
            print(f"| {item} |")
        print("_____\n")


class StackOperations(Stack):
    def run(self):
        s = Stack()  
        while True:
            choice = Inputs.choice_stack()
            if len(choice) == 1:
                if choice in ['1']:
                    try:    
                        item = input("Enter the number you want to push in stack: ")
                    except ValueError:
                        print("Enter a valid item to push!")
                    except Exception as e:
                        print(f"Error: {e}")
                    s.push(item)
                    print(f"Item {item} successfully pushed in STACK")
                elif choice in ['2']:
                    print(f"Item popped: {s.pop(item)}")
                    f"Current stack: \n{s.display()}"
                elif choice in ['3']:
                    print(f"Top Item: {s.peek()}")
                elif choice in ['4']:
                    print(f"STACK content:{s.display()}")    
                elif choice in ['5']:
                    print("Exiting...\n\n")
                    break
