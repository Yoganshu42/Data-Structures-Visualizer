class Inputs:
    @staticmethod
    def inputs_main():

        print("\'1\' STACK")
        print("\'2\' Queue")
        print("\'3\' Circular Queue")
        print("\'4\' LinkedList")
        print("\'5\' Decision Tree")
        print("\'6\' Graph")
        print("\'7\' Exit")

        while True:
            try:
                choice = input("\nEnter the Data structure you want to visualize: ")
                if choice in ['1','2','3','4','5','6']:
                    return int(choice)
                else:
                    print("Plese enter a number between 1-5.")
            except Exception:
                print("Error: Invalid Input! Please enter a valid number.")

    @staticmethod
    def choice_stack():
        print("\n\t\t--- STACK OPERATIONS ---")
        
        print("\'1\' PUSH")
        print("\'2\' POP")
        print("\'3\' PEEK")
        print("\'4\' DISPLAY")
        print("\'5\' EXIT")
        return input("\nEnter your choice of operation from (1-5) in numerics: ")
    
    @staticmethod
    def choice_queue():
        print("\n\t\t--- QUEUE OPERATIONS ---")
        
        print("\'1\' ENQUEUE")
        print("\'2\' DEQUEUE")
        print("\'3\' PEEK")
        print("\'4\' DISPLAY")
        print("\'5\' EXIT")
        return input("\nEnter your choice of operation from (1-5) in numerics: ")

    @staticmethod
    def choice_queue():
        print("\n\t\t--- QUEUE OPERATIONS ---")
        print("\'1\' ENQUEUE")
        print("\'2\' DEQUEUE")
        print("\'3\' PEEK")
        print("\'4\' DISPLAY")
        print("\'5\' EXIT")
        return input("\nEnter your choice of operation from (1-5) in numerics: ")
        